---
status: In-Round-only
client: Koboom
project: Koboom
created: 2026-05-21
source: free-text
source_ref: "tests/to-spec/fixtures/case12-srs-missing-page-skip.md (test fixture)"
srs_ref: missing
design_md: missing
spec_pages:
  - "https://www.notion.so/cigroio/mock-spec-page-url-koboom-refund-email"
srs_update_count: 0
changelog_entries_added: 0
---

# Request Triage — 크레딧 환불 안내 메일 자동 발송 (SRS 미연결, Part E skip)

> Reference draft — official spec lives in Nexus / PM Notion. In-Round 항목은 PM confirm 후 커뮤니케이션 DB / 태스크 DB / SRS 본문 / Change Log에 자동 반영됩니다.

## 1. 변경 요청 요약
- 누가 / 언제 / 어떤 채널: Koboom 고객사, 2026-05-21, 직접 피드백
- 원문 인용:
  > "크레딧 결제 환불 안내 메일 발송 기능 추가 부탁드립니다. 환불 처리 완료 시 자동으로 안내 메일이 가도록 해주세요."
- PM 1-line 정규화: 크레딧 환불 처리 완료 시 안내 메일 자동 발송 — 신규 알림 기능.

## 2. 기존 범위 대비 영향도
- SRS 참조: [확인 필요] SRS 미연결 — Nexus Agent / PM 확인 필요
- 영향 분류: 신규 기능 (알림 발송)
- 전체 Impact: Medium

## 3. 화면·UX 영향
- [확인 필요] design.md 부재 — UI 영향 상세 판단은 design owner / Nexus Agent 확인 필요
- design.md 갱신 필요 여부: 불필요 (백엔드 자동 발송)
- wireframe 필요 여부: 불필요

## 4. 4-Bucket Triage

### In-Round
- [ ] 환불 처리 완료 시 안내 메일 자동 발송 / 명확 근거 / Impact: Medium

### Next-Round
(현재 항목 없음)

### Out-of-Scope
(현재 항목 없음)

### Confirm-Needed
(현재 항목 없음)

## 5. 고객 확인 / 거절 안내
(현재 확인 필요·거절 안내 항목 없음)

## 6. 개발팀 전달 문구
- English summary: Send automated refund-completion notification email when a credit refund is processed.
- 영향 SRS section: no SRS impact recorded (SRS missing — see §9 warning)
- AC 후보:
  - When refund is processed, then notification email is sent to the user's registered address
- Impact: Medium (구체 공수 산정은 dev 확인)

## 7. PM Confirm Gate

```
[확인 필요]
다음 In-Round 항목을 4가지 변경으로 생성합니다:

스펙 페이지: Send refund-completion notification email
태스크: 1개 (Implement refund-completion email trigger)
SRS 본문 patch: (skip — srs_ref: missing)
Change Log entry: (skip — srs_ref: missing)

1. 전체 진행 (4가지 모두 — 권장)
2. SRS 본문·Change Log skip (스펙·태스크만)
3. 수정 (4-bucket 분류 다시 검토)
4. 취소

추천: 1
```

PM 선택: **1 (전체 진행)** — srs_ref: missing이라 Part E 자동 skip. 스펙·태스크만 생성, SRS 본문·Change Log unchanged.

## 8. Notion 스펙 + 태스크 + SRS 본문 + Change Log
- 스펙 페이지: https://www.notion.so/cigroio/mock-spec-page-url-koboom-refund-email
- 태스크 1개:
  - [ ] Implement refund-completion email trigger (Priority: Medium / AC: Email sent on refund processed / link: mock)
- SRS 본문 patch: (skip — srs_ref: missing, Part E 자동 skip)
- Change Log entry: (skip — srs_ref: missing)
- linked view 수동 설정 안내: 스펙 페이지 하단 /linked view → 태스크 DB 추가 → 필터: 스펙 출처 = "Send refund-completion notification email"

## 9. PM 다음 단계
- In-Round (Notion 생성됨, SRS skip): /dev-chat에 §6 사용 + linked view 수동 설정
- [확인 필요] SRS 페이지 미연결 — /create-srs로 신규 생성 또는 PM이 수동으로 srs_ref 연결 필요. 본 라운드 In-Round 변경은 스펙·태스크만 반영됨 (Part E skip).
- Confirm-Needed: (없음)
- Out-of-Scope: (없음)
- Next-Round: (없음)

---

## 다음 단계 (자동 실행 안 함, 안내만)

- In-Round 페이지: /dev-chat에 §6 사용 + linked view 수동 설정
- Confirm-Needed: /client-chat에 §5 사용
- Out-of-Scope: /client-chat에 거절 안내 사용
- Next-Round: 다음 라운드 진입 시 본 triage 파일 재검토
- 상태 변경: triage 파일 frontmatter status 직접 수정 (Triaged → Dev-Handoff)
- SRS 연결 후 재호출: /create-srs 또는 PM 수동 연결 → 본 triage 항목을 다음 /to-spec 호출 시 SRS 반영 가능

---

> ⚠️ **In-Round로 분류·생성된 Notion 스펙은 PM이 §7 confirm gate에서 명시 진행한 항목만 포함합니다. PM 미확인 In-Round 항목은 Notion으로 가지 않았습니다.**
