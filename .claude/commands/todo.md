---
description: PM 액션 빠르게 추가 → Nexus Todo(공식) + Notion PM Action Hub(백업) dual 저장
argument-hint: [프로젝트] [할 일]
allowed-tools: Read, Glob, Grep, mcp__notion-cigro__notion-create-pages, mcp__notion-cigro__notion-fetch, mcp__notion-cigro__notion-update-data-source, mcp__nexus-os__internal_todos_create, mcp__nexus-os__projects_list
---

# Quick Todo Add

## Arguments
사용자 입력: $ARGUMENTS

## Context
- PM이 빠르게 할 일을 추가하는 스킬
- 최소한의 입력으로 **Nexus "Todo" 페이지(사내 공식)** + **Notion PM Action Hub(개인 백업)** 에 동시 저장
- 러프하게 입력해도 프로젝트/액션 유형/우선순위를 자동 감지

## Output Destination (dual-write)
- **Nexus internal_todos** (공식 primary) — `mcp__nexus-os__internal_todos_create`
  - 사내 "Todo" 페이지에 등록, TEAM 가시성, nexus-daily 흐름과 연결
- **Notion PM Action Hub** (`ff43aae9a89482ea8c57815a65ac9f5b`) — `mcp__notion-cigro__notion-create-pages`
  - `/today-brief`(매일 10:30 자동) + Telegram bot 호환용 개인 백업 미러
- **터미널**: 추가된 항목 확인

## Instructions

0. **프로젝트 옵션 sync prelude (항상 먼저 실행)**:
   - 목적: Projects DB가 source of truth, PM Action Hub `프로젝트` select가 자동으로 따라오게 보강
   - 절차:
     1. Projects DB (`collection://98c3ff93-01f1-4b2e-a490-d827ac079ffc`)에서 프로젝트 제목 목록 조회 (`mcp__notion-cigro__notion-fetch`)
     2. PM Action Hub data source (`collection://a183aae9-a894-8379-8708-87cf507ec8e8`)의 `프로젝트` select 현재 옵션 추출
     3. Projects DB ⊖ select 옵션 = 누락 프로젝트 (case-sensitive exact diff)
     4. 누락 있으면 `mcp__notion-cigro__notion-update-data-source` 로 `ALTER COLUMN "프로젝트" SET SELECT(<기존 옵션 + color 보존, 누락분은 default color>)` 실행
     5. 누락 없으면 즉시 다음 단계로
   - **안정성 룰**:
     - Sync prelude 실패(Projects DB fetch 실패 등)는 hard-fail ❌ — 경고 1줄 출력 후 기존 select 옵션 기준으로 Step 1 진행
     - 기존 옵션 손실 금지 — ALTER 문에는 반드시 fetch한 기존 옵션 전부 포함
     - 같은 세션 내 다회 호출 시 1회만 실행 (cache)

1. **입력 파싱**:
   - **프로젝트명 감지 (보수적 자동 확정 — B2)**:
     1. 입력에서 `[대괄호]` 추출 시도
     2. 대괄호가 있으면 그 값을 Notion `프로젝트` select 옵션과 **exact match**로 비교 (대소문자·공백 완전 일치)
        - Exact match 성공 → **자동 확정** + 사용자에게 1줄 명시:
          > `[Koboom] 으로 인식했습니다`
        - Exact match 실패 → 숫자 선택지로 이동 (아래)
     3. 대괄호가 없으면 → 숫자 선택지로 이동 (아래)
     4. **substring / 유사도 / case-insensitive 매칭 자동 확정 금지.** 후보가 1개여도 exact가 아니면 사용자 확인 필수
   - **매칭 실패 시 숫자 선택지**:
     ```
     프로젝트를 지정해주세요:
     1. 최근 사용 프로젝트 (activity-log 또는 최근 PM Action Hub 기록 기준)
     2. 전체 목록 보기
     3. 취소
     추천: 1
     ```
     - 1 선택 → 최근 프로젝트 3~5개 숫자 선택지
     - 2 선택 → Notion select 옵션 전체 목록 숫자 선택지
     - 3 선택 → 중단
   - **액션 유형 감지** (Notion `액션 유형` select용):
     - "회신", "전달", "공유", "카톡", "메시지" → 고객 커뮤니케이션
     - "sync", "확인", "체크", "follow-up" → 내부 follow-up
     - "등록", "업데이트", "정리", "작성" → 운영 체크
   - **우선순위 감지** (Nexus `priority`용):
     - "긴급", "ASAP", "asap", "즉시", "바로" → `HIGH`
     - "오늘 중", "중요" → `MEDIUM`
     - 그 외 → `NO_PRIORITY` (기본값, 사용자가 Nexus에서 later 조정)
   - **오늘 여부 감지** (Nexus `plannedDate` + Notion `상태`용):
     - "오늘" 토큰 포함 → `plannedDate` = 오늘 00:00 Asia/Seoul (epoch ms), Notion 상태 = "오늘"
     - 미포함 → `plannedDate` 생략, Notion 상태 = "미착수"
   - 나머지 = 제목

2. **중복 체크 (C1 멱등성 가드 — dual-write 전체 게이트)** — 저장 직전에 반드시 실행:
   - **Notion이 전역 멱등 게이트**. Nexus는 별도 dedup 쿼리 없이 Notion 결과에 연동 (dual-write invariant: Notion에 있으면 Nexus에도 이미 있다고 간주).
   - **Unique key**: 제목(title exact) + 프로젝트 + 작성일(오늘)
   - PM Action Hub DB(`data_source_url: collection://a183aae9-a894-8379-8708-87cf507ec8e8`)에서 `mcp__notion-cigro__notion-fetch`로 필터 조회:
     ```json
     {"and": [
       {"property": "제목", "title": {"equals": "<title with [ProjectName] prefix>"}},
       {"property": "프로젝트", "select": {"equals": "<project>"}},
       {"property": "작성일", "date": {"equals": "<today YYYY-MM-DD>"}}
     ]}
     ```
   - **결과 분기**:
     - **0건** → Step 3 dual-write (Nexus + Notion 둘 다 신규 생성)
     - **1건 이상** → **skip + 알림** (Nexus/Notion 모두 write 금지):
       ```
       ⏭️ 같은 항목이 오늘 이미 등록됨: [Koboom] 피드백 업데이트
         → 기존(Notion): [링크]
         추가하지 않음. 필요하면 수정: /todo [Koboom] 피드백 업데이트 - 추가 (다른 제목)
       ```
   - **재시도 루프 대응 원칙**: 동일 세션에서 Bash/MCP timeout으로 재호출되는 경우에도 중복 페이지 생성 방지. Notion 게이트가 Nexus까지 막음.
   - 여러 줄 입력 시 각 줄마다 개별적으로 중복 체크 (한 줄만 중복이어도 나머지는 정상 생성).

3. **Dual-write** — Step 2에서 신규로 판단된 항목만. 두 write는 독립 partial-skip (어느 하나 실패해도 나머지는 진행, hard-fail 금지).

   **3a. Nexus projectId 해석 (best-effort, 생략 가능)**:
   - `mcp__nexus-os__projects_list` 에 `search=<감지된 프로젝트명>`, `limit=100` 1페이지만 조회 (pagination 미반복 — /todo 속도 우선)
   - 응답 items 중 `name`이 **case-insensitive exact match**인 항목 → `projectId` 확정
   - 매칭 없으면 `projectId` 생략 (Nexus todo는 프로젝트 미연결로 등록, 경고 없이 진행)
   - 프로젝트 자체가 없는 입력(전체 목록 보기 등에서 미선택)도 `projectId` 생략

   **3b. Nexus Todo 등록** (`mcp__nexus-os__internal_todos_create`):
   - `title`: `[ProjectName] short description` (Notion 제목과 동일 — today-brief 형식 일치). 프로젝트 미연결 시 description만.
   - `description`: 생략 (최소 입력 원칙)
   - `priority`: Step 1 감지값 (`NO_PRIORITY` 기본)
   - `plannedDate`: "오늘" 감지 시에만 — **오늘 00:00 Asia/Seoul을 epoch ms로 계산** (예: context의 오늘 날짜 `<YYYY-MM-DD>T00:00:00+09:00` 을 epoch ms 변환). 미감지 시 생략 → Nexus INBOX view에 적재, TODAY view는 아님.
   - `projectId`: 3a에서 확정된 경우만
   - `assignee`는 입력하지 않음 — 현재 사용자(Yoona)에게 자동 배정
   - **실패 시**: 경고 1줄(`⚠️ Nexus 등록 실패: <에러> — Notion만 저장`) 출력 후 3c 진행

   **3c. Notion PM Action Hub 저장** (`mcp__notion-cigro__notion-create-pages` — DB ID: `ff43aae9a89482ea8c57815a65ac9f5b`):
   - 제목: **반드시 `[ProjectName] short description` 형태**. 프로젝트명은 대괄호, 설명은 짧고 명확하게.
   - parent: `{"type": "data_source_id", "data_source_id": "a183aae9-a894-8379-8708-87cf507ec8e8"}`
   - properties:
     - `제목` (title): `[ProjectName] short description`
     - `프로젝트` (select): 감지된 프로젝트 (미연결 시 생략)
     - `상태` (select): "오늘" 감지 시 "오늘", 그 외 "미착수"
     - `액션 유형` (select): 감지된 유형 / 없으면 생략
     - `출처` (select): "manual"
   - **실패 시**: 경고 1줄(`⚠️ Notion 백업 저장 실패: <에러> — Nexus는 등록됨`) 출력. today-brief 호환성이 끊기므로 사용자에게 수동 확인 권장.

4. **터미널 출력**:
   ```
   ✅ 추가 완료: [프로젝트] 할 일 내용
   - Nexus Todo: priority NO_PRIORITY, plannedDate <있을 경우만>
   - Notion(백업): 상태 미착수
   ```
   부분 실패 시 해당 줄을 ⚠️ 표기:
   ```
   ⚠️ 부분 저장: [프로젝트] 할 일 내용
   - Nexus Todo: 등록 완료
   - Notion(백업): 실패 — 수동 확인 필요
   ```
   중복 skip 있으면 별도 블록으로 표시:
   ```
   ⏭️ Skip: [Koboom] 피드백 업데이트 (오늘 이미 등록됨 — Notion/Notion 모두 skip)
   ```

## Examples

**단일 항목:**
```
/todo [Koboom] 피드백 업데이트 전달
→ Nexus title: [Koboom] 피드백 업데이트 전달, priority NO_PRIORITY
→ Notion: 프로젝트 Koboom, 상태 미착수, 액션 유형 고객 커뮤니케이션
```

**오늘 할 일 (plannedDate + 상태 오늘):**
```
/todo 오늘 [RCK] 타임라인 정리해서 고객에게 공유
→ Nexus title: [RCK] 타임라인 정리해서 고객에게 공유, plannedDate 오늘 00:00 KST, priority NO_PRIORITY
→ Notion: 프로젝트 RCK, 상태 오늘, 액션 유형 고객 커뮤니케이션
```

**긴급 (priority HIGH):**
```
/todo [DSA] 긴급 — 빌드 에러 핫픽스 배포
→ Nexus priority HIGH
→ Notion 상태 미착수
```

**여러 개 한번에:**
```
/todo
[Koboom] admin figma update
[RCK] timeline 정리
[BaraeCNP] 문의내용 회신
→ 3개 항목 각각 dual-write (각각 Notion 중복 체크)
```

## Rules

- 프로젝트명이 없거나 Notion select 옵션과 exact match가 아니면 **절대 자동 확정 금지** — 숫자 선택지로 PM에게 확인
- 자동 확정된 경우에만 `[Koboom] 으로 인식했습니다` 명시 통보
- 여러 줄 입력 시 각 줄을 별도 항목으로 추가 (각각 중복 체크 + dual-write)
- **중복 체크 (C1)**: Notion이 전역 게이트. 같은 제목+프로젝트+작성일이 이미 있으면 Nexus/Notion 모두 skip. 덮어쓰기/업데이트 금지. 다른 항목으로 추가하려면 제목을 바꿔서 재실행.
- **Nexus projectId 매칭은 best-effort** — 1페이지 search + exact match, 실패 시 projectId 생략(partial-skip). hard-fail 금지.
- **dual-write 부분 실패 허용** — 한쪽 실패해도 다른 쪽은 저장, ⚠️ 경고로 사용자 통보. 롤백 금지.
- 한국어 입력 → 한국어로 저장
- 최대한 빠르게 — 불필요한 확인 질문 없이 바로 추가
