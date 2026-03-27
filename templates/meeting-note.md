# Template: Meeting Note

## Design Principle
Part 1은 source of truth. Part 2 (dev-chat)와 Part 3 (client-chat)는 Part 1에서 직접 추출.
각 항목은 하나의 섹션에만 존재. 중복 없음.

## Part 1: 미팅 노트 (Notion 저장)

```
## 미팅 정보
- 일시: [날짜/시간]
- 참석자: [이름들]
- 장소: [장소]
- 기준 문서: [있을 때만]

## 핵심 요약
- [가장 중요한 결정/방향]
- [블로커/일정 영향]
- [이번 라운드 vs 유지보수 구분]
- [고객 영향/타임라인]
(3-4줄. 이것만 읽어도 미팅 결과 파악 가능.)

## 이번 라운드 반영사항
- 🔴 [긴급] — [왜 긴급한지 inline]. [담당/기한]
- 🔴 [긴급] — [context]. [담당/기한]
- [일반 항목] — [필요시 context inline]
- [일반 항목]
- [일반 항목]
(메인 섹션. 긴급·결정·액션을 하나로 통합.
 🔴 = 블로커, 고장난 것, 수정 안 된 것.
 각 항목은 짧고 실행 가능하게.)

## 후순위 / 유지보수
- [미룬 항목] — [이유 inline if needed]
(명시적으로 나중에 하기로 한 것만.)

## 고객/PM 확인 필요
- Client: [고객이 해야 할 것]
- PM: [PM이 판단/처리할 것]
- [미결 사항 — 누가 확인해야 하는지]
(고객 액션 + PM 내부 액션 + 미결 질문.)
```

### 항목 배치 규칙
하나의 항목은 하나의 섹션에만:
- 개발팀이 이번에 반영 → `이번 라운드 반영사항`
- 나중에 하기로 함 → `후순위/유지보수`
- 고객/PM이 해야 함 → `고객/PM 확인 필요`
- 겹치면 가장 실행에 가까운 섹션에

### 핵심 요약 vs 이번 라운드 반영사항
- 핵심 요약 = 미팅의 결론 (방향, 영향, 큰 그림)
- 이번 라운드 = 구체적 항목 리스트 (무엇을, 왜, 누가)
- 요약에 나온 내용을 반영사항에서 한 줄씩 다시 쓰지 않음

## Part 1 → Part 2 매핑 (dev-chat)

Part 1에서 직접 추출. 새로 분석하지 않음.

```
📌 [{project}] Meeting follow-up — {date}

Critical context:
- ← Part 1 `이번 라운드 반영사항`의 🔴 항목에서 추출
- 상황 + 왜 긴급한지 포함

This round:
- ← Part 1 `이번 라운드 반영사항`의 일반 항목에서 dev 항목만
- PM 항목, Client 항목 제외
- 직접 서술: "Change X to Y" (not "This likely means...")

Maintenance later:
- ← Part 1 `후순위/유지보수`에서 dev 항목만

Please review and let me know if anything needs more effort than expected.
```

제외: `고객/PM 확인 필요` 항목 (dev 대상이 아님)

## Part 1 → Part 3 매핑 (client-chat)

Part 1에서 직접 추출. 새로 분석하지 않음.

```
안녕하세요, 오늘 미팅 감사드립니다!
말씀 나눈 내용 정리해서 공유드립니다.

** 오늘 논의된 핵심 내용
- ← Part 1 `핵심 요약`에서 고객이 알아야 하는 항목만

** 확정된 사항
- ← Part 1 `이번 라운드 반영사항`에서 고객 가시 항목만
- 내부 버그 디테일 제외 (결과만: "수정 후 안내드리겠습니다")

** 진행 예정 사항
- ← Part 1 `이번 라운드 반영사항`에서 "우리가 할 예정" 항목
- 고객이 알아야 하는 수준으로만

** 추가 확인 부탁드리는 사항
1. ← Part 1 `고객/PM 확인 필요`에서 Client 항목만
2. PM 내부 항목 제외

감사합니다!
```

제외: PM 내부 액션, 기술 디테일, 일정 지연 사유, 팀 리소스

## Example

**Input:**
```
RCK 미팅
매니저 계정 알림 버그 — 한 계정만 알림 안 옴, 테스트 블로킹
설문 완료 버튼 수정했다고 했는데 고객이 테스트하니 아직 안됨
타임라인 공정표 달라고 강하게 요청
질문지 안정화 최우선
객관식 7개로, 직책은 주관식으로
비번 10자, 잔액 문구 수정
카톡 전환은 유지보수때
직원 4명이 다음주 화요일까지 테스트
```

**Part 1:**
```
## 미팅 정보
- 일시: 2026-03-26
- 참석자: [확인 필요]
- 장소: [확인 필요]

## 핵심 요약
- 질문지 안정화 + 매니저 계정 버그 수정이 최우선, 고객사 테스트 일부 블로킹 중
- 타임라인 미제공에 대한 고객사 불만 강함 — PM 즉시 대응 필요
- 대부분 간단 수정 범위, 카톡 전환은 유지보수로 확정

## 이번 라운드 반영사항
- 🔴 매니저 계정 알림 버그 — 한 계정만 알림 안 옴, 고객사 테스트 블로킹. 오늘 수정 필요
- 🔴 설문 완료 버튼 재확인 — 수정했다고 했으나 고객사 테스트 시 미반영
- PM: 타임라인/공정표 엑셀 정리 후 고객사 전달 — 최우선
- 객관식 선택지 최대 7개로 조정
- '근무 당시 직책' → text field 변경
- 비밀번호 12자 → 10자 완화
- '결제 금액' → '잔액' 문구 수정

## 후순위 / 유지보수
- 링크발송 카톡+이메일 전환

## 고객/PM 확인 필요
- Client: 직원 4명 레퍼런스 체크 테스트 진행 (다음 주 화요일까지)
```

**Part 2 (extracted from Part 1):**
```
📌 [RCK] Meeting follow-up — 2026-03-26

Critical context:
- Manager account notification bug — one account not receiving alerts, blocking client test. Fix today.
- Questionnaire submit button — was said to be fixed but client tested and it's still broken.

This round:
- Questionnaire CRUD stabilization is top priority.
- Limit max options per question to 7.
- Change "Position at the time" to text input.
- Password minimum 12 → 10 chars.
- Update label "결제 금액" → "잔액".

Maintenance later:
- Switch link delivery to KakaoTalk + email.

Please review and let me know if anything needs more effort than expected.
```

**Part 3 (extracted from Part 1):**
```
안녕하세요, 오늘 미팅 감사드립니다!
말씀 나눈 내용 정리해서 공유드립니다.

** 확정된 사항
- 질문지 기능 안정화를 최우선으로 진행합니다
- 알림 관련 확인된 문제를 금일 중 수정합니다
- 설문지 선택지, 비밀번호 규칙 등 수정 사항을 이번 주 내 반영합니다

** 진행 예정 사항
- 전체 프로젝트 타임라인을 정리하여 빠른 시일 내 전달드리겠습니다

** 추가 확인 부탁드리는 사항
1. 직원분들 레퍼런스 체크 테스트를 다음 주 화요일까지 진행 부탁드립니다

감사합니다!
```
