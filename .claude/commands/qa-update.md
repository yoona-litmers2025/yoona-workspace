---
description: 양방향 QA 상태 동기화 — 고객 QA "대기중" → 내부 영문 티켓 (intake) + 내부 "Ready for QA" → 고객 QA "검수요청"/"재검수요청" (review-sync)
argument-hint: <project-name> [--internal <URL>] [--client <URL>]
allowed-tools: Read, Glob, Grep, Bash, Write
---

# QA Update — Bidirectional Status Sync

## Arguments
사용자 입력: $ARGUMENTS

## 핵심 원칙 (이 스킬은 단순해야 한다)

PM이 매일 반복하는 단순 작업이다. 과한 분석·다단계 confirm·confidence tier 같은 ceremony는 ❌.

흐름 한 줄 요약:
> client "대기중" → 영문 티켓으로 내부 DB로 옮기고, 내부 "Ready for QA"는 client status를 "검수요청"/"재검수요청"으로 업데이트한다. 미리보기 한 번 보여주고 PM이 1 누르면 양쪽 한 번에 적용.

원칙:
- **확인 게이트는 단 1개** — 통합 미리보기 후 단일 confirm. Mode 분리 게이트 ❌, "intake 먼저 적용 후 review-sync 게이트" 같은 sequencing ❌
- **URL 매칭만** — internal row의 `[source: <URL>]` 또는 source URL property로 client row 매칭. Semantic matching·confidence tier ❌
- **비용 보고 ❌** — "20+ fetch 필요합니다" 같은 보고는 PM이 안 듣는다. 그냥 batch fetch로 처리
- **자동 chain 호출 ❌** — `/qa-plan`, `/issue-ticket`, `/to-spec`, `/client-chat`, `/dev-chat` 절대 호출 ❌

## Step 0: Project + Links 확인

1. `$ARGUMENTS`에서 `<project-name>` 추출 (첫 비-flag 토큰). 없으면 cwd가 `clients/<name>/` 패턴이면 자동, 아니면 PM에게 자유 입력 질문.
2. **링크 lookup (순서대로, 첫 hit에서 중단)**:
   - `--internal` / `--client` 인자 둘 다 있으면 즉시 채택
   - `memory/project_<name>_qa_links.md` (`internal_url:` / `client_url:` 추출)
   - `clients/<name>/CLAUDE.md` 의 `## QA Links` 섹션
   - PM에게 자유 입력 질문 (URL 형식 → 선택지 형식 불가)
3. PM 직접 입력으로 확보된 경우 즉시 `memory/project_<name>_qa_links.md` 자동 생성/갱신

링크 fetch 실패 → 해당 side mode 비활성화. 둘 다 실패 → 중단.

## Step 1: 양쪽 DB 스키마 + 후보 row 동시 수집

병렬로 한 번에:
1. `mcp__notion-cigro__notion-fetch` — internal Tasks DB (data_source 추출)
2. `mcp__notion-cigro__notion-fetch` — client QA DB (data_source 추출)
3. `mcp__notion-cigro__notion-search` data_source_url로 양쪽 DB의 page 목록 enumerate
4. enumerate된 candidate page id를 **한 batch parallel call**로 모두 fetch

**Enumeration 강화 룰 (중요)** — `notion-search`는 semantic 결과(최대 ~25/query)만 surface하므로 단일 query로는 row가 누락된다. 최소 **5개 이상의 다양한 keyword**로 동시 search 실행 + 결과 union해서 candidate 풀 구성:
- 일반 한국어 ("수정", "페이지", "버튼", "변경 필요", "추가")
- 도메인 단어 (project별 — 예: Booktails는 "결제", "활동지", "로그인", "어드민", "프로모션", "콜렉션", "햄버거", "드롭다운")
- 클라이언트명 / 프로젝트명 ("Booktails", "MapTails")

5번 search로도 surface 안 된 row가 의심되면 **PM에게 "혹시 누락된 row가 있다면 URL 알려주세요"라고 1회 확인**. PM이 추가로 발견한 row가 있으면 그 source URL을 다음 실행 keyword pool에 추가하도록 memory에 기록.

**비용 보고 ❌** — "10건 더 필요합니다" 같은 단계별 보고하지 말고 그냥 batch로 처리.

스키마에서 다음 자동 감지:
- Internal: title 필드명, status 필드명, "Ready" 포함 status 옵션 (1개면 자동, 2개면 1회 PM 확인 후 memory 저장)
- Client: title 필드명 (예: `페이지`), text 필드명 (예: `수정내용`), Status 필드, 검수회차 옵션

## Step 2: 분류

수집된 row를 분류:
- **Mode 1 후보**: client DB status == "대기중"
- **Mode 2 후보**: internal DB status == "Ready for QA" (Step 1에서 감지된 명칭)

Mode 1 → 각 client row의 페이지+수정내용을 읽고 영문 ticket draft 생성:
- Title: `[Page] Issue description` (영문, 간결)
- Description **rich_text property에 직접 채워 넣음** (notion-create-pages `properties.Description`):
  ```
  Issue: <원문 핵심 — 한글 UI 요소 그대로 + 영어 괄호 병기>
  Expected: <client가 원하는 결과>

  [source: <client row URL>]
  ```
- ⚠️ **중요 — 본문(content) 대신 Description property를 사용해야 함**. `notion-create-pages` 호출 시 `content` 파라미터에 본문으로 넣으면 DB view의 Description column이 빈 칸으로 보임 → "안 생긴 것처럼" 보이는 버그. 반드시 `properties.Description`에 텍스트를 넣고, `content`는 비워둘 것 (또는 페이지 본문에 별도로 의미 있을 때만 사용)
- Issue가 명백히 없고 새 기능 요청이면 `Expected:` 만
- Priority: 영향도 기반 (High/Medium/Low). 임의 공수 산정 ❌
- App / Screen / Feature multi_select — schema에 옵션 있고 row 내용에서 명확하면 채움, 모호하면 비움
- 검수회차 ≥ 2 → Title 앞 `[Round N]` 접두사
- glossary `glossary/<client>.md` 있으면 용어 일관성 유지
- 멱등성: internal DB의 기존 row 중 description에 동일 client URL 포함 → skip (덮어쓰기 ❌)

Mode 2 → 각 internal row의 source URL 추출 (Description의 `[source: <URL>]` 정규식 또는 source URL property):
- source URL → client row 직접 lookup
- client row status에 따라:
  - `해결안됨` / `검수요청` / `재검수요청` → 새 status: **재검수요청**
  - `진행중` / `대기중` / `기획 필요` / `추가개발` → 새 status: **검수요청**
  - `완료` / `취소` → skip (이미 종료)
  - 이미 동일 → skip (멱등성)
- source URL 없거나 lookup 실패 → skip + 결과 표에 "no match" 표시. Semantic matching ❌

## Step 3: 통합 미리보기 + 단일 Confirm Gate

```
## QA Update Preview (<project>)

### Mode 1 — Intake: N건
| # | Client page | English ticket | Priority |
|---|---|---|---|
| 1 | ...         | [Title]        | High     |
...
(이미 동일 source URL 있는 row가 있으면 별도 "중복 skip" 섹션에 표시)

### Mode 2 — Review-Sync: A apply / B skip
**Apply**:
| Internal title | → Client row | Current → New |
| ...            | ...          | 진행중 → 검수요청 |

**Skip**:
- 완료 (already done): X건
- No client match: Y건
```

**단일 confirm**:
```
1. 양방향 실행 (intake N + review-sync A) (추천)
2. Intake만 (Mode 1)
3. Review-Sync만 (Mode 2)
4. 취소

추천: 1
```

N=0 이면 옵션 1·2 disabled. A=0 이면 옵션 1·3 disabled. 4 (취소) → 외부 write ❌, 종료.

## Step 4: 적용 (선택 시)

선택된 mode를 **batch parallel**로 한 번에 실행:
- Mode 1: `mcp__notion-cigro__notion-create-pages` 한 번 호출에 N개 모두 (parent: internal data_source_id)
- Mode 1 (이어서): 생성한 N개 client row를 `mcp__notion-cigro__notion-update-page` 병렬 호출로 status "진행중"
- Mode 2: 매칭된 client row를 `mcp__notion-cigro__notion-update-page` 병렬 호출로 status "검수요청"/"재검수요청"

**Mode 1 결과는 Mode 2 매칭에 반영되지 ❌** (Step 2 snapshot 사용 — race 방지)

## Step 5: 결과 보고

```
## QA Update 결과 (<project>)

### Intake
- 생성: {n}건 / 중복 skip: {m}건
- 고객 DB "진행중" 변경: ✅
- 생성 ticket:
  1. [Title] — Priority — [링크]
  ...

### Review-Sync
- 적용: {p}건 (검수요청 {a} / 재검수요청 {b})
- skip: {c}건 (완료 / 매칭 실패)
- 변경 client row:
  1. "수정내용 요약" — 진행중 → 검수요청 — [링크]
  ...
```

## Hard Boundaries

- Confirm gate 우회 / 자동 발송 ❌ — gate=4 또는 비응답 시 외부 write 절대 ❌
- Notion schema 변경 ❌ — read-only schema discovery, property 신설 ❌
- 종료 상태 (`완료`) client row 변경 ❌
- Mode 2 매칭은 URL only — semantic matching·confidence tier ❌
- 자동 chain 호출 (`/qa-plan` 등) ❌
- 스크린샷 자동 이전 ❌ (원본 페이지에 그대로 둠 — source URL로 참조)
- AI 임의 공수 산정 (MD/hour/day) ❌
- 비용·단계 진척 중계 보고 ❌ — PM은 결과만 원함. "20개 더 fetch 필요합니다" 같은 진척 보고 ❌, 그냥 처리하고 결과만

## Memory format

PM 직접 입력 또는 발견된 링크 자동 저장:

```markdown
---
name: project-<name>-qa-links
description: <name> QA links — internal Live-QA + client QA DB
metadata:
  type: reference
---
- internal_url: <URL>
- internal_data_source: collection://<id>
- client_url: <URL>
- client_data_source: collection://<id>
- "Ready for QA" status 옵션명: <감지값>
- last_used: <YYYY-MM-DD>
```

MEMORY.md 인덱스에 한 줄 추가.
