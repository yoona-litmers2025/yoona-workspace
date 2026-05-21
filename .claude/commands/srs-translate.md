---
description: SRS/기획서를 한국어에서 영어로 번역 및 구조화
argument-hint: --client <name> [Notion 링크 또는 텍스트]
allowed-tools: Read, Glob, Grep, mcp__notion-cigro__notion-create-pages, mcp__notion-cigro__notion-fetch, mcp__notion-cigro__notion-update-page
---

# SRS Translation (KR → EN)

## Arguments
사용자 입력: $ARGUMENTS

## Context
- SRS 번역 템플릿: !`cat /Users/yoona/Documents/yoona-workspace/templates/srs-translation.md`

## Instructions

### 기본 원칙 — 비창작 원칙 (Non-Invention Rule)
소스에 없는 내용은 출력에 포함하지 않는다. Claude의 분석, 의견, 추론, 제안을 번역 결과물에 섞지 않는다.

**예외**: 사용자가 Notion 링크를 첨부하면서 "이 내용도 반영해줘", "이 부분 추가해줘" 등 명시적 지시를 함께 제공한 경우에만 해당 내용을 반영한다.

---

1. **인자 파싱**: 사용자 입력에서 소스(Notion 링크 또는 텍스트)와 클라이언트명을 추출
   - 추가 지시(링크 + 업데이트 요청)가 있는지 확인
2. **컨텍스트 로드 + 소스 가져오기** (아래 3개는 병렬 호출 가능 — 서로 독립):
   - **용어집**: `glossary/{client-name}.md` 파일이 있으면 읽어서 번역 시 참조
   - **클라이언트 컨텍스트**: `clients/{client-name}/CLAUDE.md` 파일이 있으면 읽어서 도메인 이해에 활용
   - **소스**: Notion 링크면 `mcp__notion-cigro__notion-fetch`으로 블록 읽기, 텍스트면 그대로 사용
5. **번역 실행**: `templates/srs-translation.md`의 프로세스와 출력 포맷을 따름
   - 전체 SRS를 먼저 읽고 구조와 범위 파악
   - 용어집 기반으로 일관된 용어 사용
   - 충실한 번역 — 요구사항 추가/제거/재해석 금지
   - 소스 구조를 그대로 반영 — Claude가 구조를 재구성하거나 섹션을 임의로 추가하지 않음
   - **Change Log pointer-stub 필수**: 영문 SRS 본문 마지막에 다음 형식 자동 추가 (KR SRS Change Log를 canonical로 가리키는 stub):
     ```
     ## Change Log
     - YYYY-MM-DD [/srs-translate] v1 generated from KR SRS — <KR SRS Notion URL>
     ```
     - 한국어 SRS에 v1 외 추가 Change Log entry가 이미 있으면, 각 entry마다 1줄 pointer-stub 생성 (번역 X, 포인터만):
       `- YYYY-MM-DD [/to-spec via KR-SRS] <REQ ID 또는 섹션> updated — see KR SRS Change Log for diff`
     - 영문 본문 자체는 한국어 Change Log를 번역하지 않음. 진실은 KR SRS에 있음.
6. **중복 체크 (C1 멱등성 가드)** — 저장 직전에 반드시 실행:
   - **Unique key**: 프로젝트 + 유형="SRS 번역" + 언어="KR→EN"
   - 프로젝트 문서 DB(`data_source_url: collection://bd33aae9-a894-82a9-b8e2-87387e7fbf47`)에서 `mcp__notion-cigro__notion-fetch`로 필터 조회:
     ```json
     {"and": [
       {"property": "프로젝트", "select": {"equals": "<project>"}},
       {"property": "유형", "select": {"equals": "SRS 번역"}},
       {"property": "언어", "select": {"equals": "KR→EN"}}
     ]}
     ```
   - **결과 분기**:
     - **0건** → Step 7 새로 생성
     - **1건 이상** → 사용자 확인 (Confirmation Format 준수):
       ```
       ⚠️ 같은 프로젝트의 EN 번역본이 이미 있습니다:
       - [제목] (작성일: YYYY-MM-DD) — [링크]

       1. 업데이트 (기존 archive + 새로 생성) (추천 — 번역 갱신)
       2. 새 버전으로 생성 (기존 유지, v2 등 버전 명시)
       3. 취소
       추천: 1
       ```
       - 1 → 기존 페이지 archive → 새로 생성. 제목은 동일.
       - 2 → 제목에 " (v2)", " (rev-YYYYMMDD)" 등 버전 접미사 추가하여 생성. 기존 유지.
       - 3 → 중단
   - **archive 실패 시 생성 중단**.

7. **Notion에 저장**: `mcp__notion-cigro__notion-create-pages`로 프로젝트 문서 DB (`d7f3aae9a894831a96b2013549196181`)에 페이지 생성
   - 유형: SRS 번역
   - 단계: SRS
   - 상태: 진행 중
   - 언어: KR→EN
   - 클라이언트/프로젝트 속성 설정
8. **New Terms 확인**: 처음 번역하는 클라이언트라면 도메인 신규 용어 목록을 출력하고 glossary 추가 여부를 사용자에게 확인
