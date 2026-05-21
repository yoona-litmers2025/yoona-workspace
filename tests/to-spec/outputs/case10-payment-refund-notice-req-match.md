---
status: In-Round-only
client: Connectory
project: Connectory-1
created: 2026-05-21
source: free-text
source_ref: "tests/to-spec/fixtures/case10-srs-update-by-req-id.md (test fixture)"
srs_ref: clients/connectory/Connectory-1/srs.md
design_md: missing
spec_pages:
  - "https://www.notion.so/cigroio/mock-spec-page-url-payment-refund-notice"
srs_update_count: 1
changelog_entries_added: 1
---

# Request Triage — 결제 완료 화면 환불 안내 문구 추가 (REQ-CON-PAY-03 직접 참조)

> Reference draft — official spec lives in Nexus / PM Notion. In-Round 항목은 PM confirm 후 커뮤니케이션 DB / 태스크 DB / SRS 본문 / Change Log에 자동 반영됩니다.

## 1. 변경 요청 요약
- 누가 / 언제 / 어떤 채널: Connectory 고객사, 2026-05-21, 직접 피드백
- 원문 인용:
  > "결제 완료 화면 환불 안내 문구를 추가해주세요. 현재 REQ-CON-PAY-03 결제 완료 화면에 환불 정책 한 줄 안내가 빠져 있어요. '환불 신청은 영업일 이내 가능합니다' 같은 안내 문구가 필요합니다."
- PM 1-line 정규화: 결제 완료 화면에 환불 정책 안내 문구 1줄 추가 — REQ-CON-PAY-03 확장.

## 2. 기존 범위 대비 영향도
- SRS 참조: REQ-CON-PAY-03 (결제 완료 표시) — client가 직접 REQ ID 명시
- 영향 분류: 기존 변경 (안내 문구 추가)
- 전체 Impact: Low

## 3. 화면·UX 영향
- [확인 필요] design.md 부재 — UI 영향 상세 판단은 design owner / Nexus Agent 확인 필요
- design.md 갱신 필요 여부: 판단 보류
- wireframe 필요 여부: 불필요 (텍스트 추가만)

## 4. 4-Bucket Triage

### In-Round
- [ ] 결제 완료 화면 환불 안내 문구 추가 (REQ-CON-PAY-03) / 기존 REQ 직접 확장, 명확 근거 / Impact: Low

### Next-Round
(현재 항목 없음)

### Out-of-Scope
(현재 항목 없음)

### Confirm-Needed
(현재 항목 없음)

## 5. 고객 확인 / 거절 안내
(현재 확인 필요·거절 안내 항목 없음)

## 6. 개발팀 전달 문구
- English summary: Add refund-policy notice line on payment completion screen (extends REQ-CON-PAY-03). Suggested text: "Refund requests accepted within the business-day window per policy."
- 영향 SRS section: REQ-CON-PAY-03
- AC 후보:
  - When user completes payment, then a single-line refund-policy notice is visible on the completion screen
- Impact: Low (구체 공수 산정은 dev 확인)

## 7. PM Confirm Gate

```
[확인 필요]
다음 In-Round 항목을 4가지 변경으로 생성합니다:

스펙 페이지: Add refund-policy notice on payment completion screen
태스크: 1개 (Add refund notice line to payment-complete screen)
SRS 본문 patch: REQ-CON-PAY-03 — 환불 정책 안내 문구 1줄 추가
Change Log entry: 1건

1. 전체 진행 (4가지 모두 — 권장)
2. SRS 본문·Change Log skip (스펙·태스크만)
3. 수정 (4-bucket 분류 다시 검토)
4. 취소

추천: 1
```

PM 선택: **1 (전체 진행)** — 스펙 + 태스크 + SRS 본문 patch + Change Log entry 모두 생성됨. REQ ID 매칭 (1순위) 적용.

## 8. Notion 스펙 + 태스크 + SRS 본문 + Change Log
- 스펙 페이지: https://www.notion.so/cigroio/mock-spec-page-url-payment-refund-notice
- 태스크 1개:
  - [ ] Add refund notice line to payment-complete screen (Priority: Medium / AC: Refund-policy notice visible / link: mock)
- SRS 본문 patch: REQ-CON-PAY-03 — 결제 완료 화면 본문에 환불 정책 안내 1줄 추가 (in-place, 섹션 6 해당 REQ 직하단)
- Change Log entry (SRS 페이지 끝에 append):
  - `- 2026-05-21 [/to-spec] REQ-CON-PAY-03 — 결제 완료 화면 환불 정책 안내 문구 1줄 추가 / Source: https://www.notion.so/cigroio/mock-spec-page-url-payment-refund-notice / Trigger: client request`
- linked view 수동 설정 안내: 스펙 페이지 하단 /linked view → 태스크 DB 추가 → 필터: 스펙 출처 = "Add refund-policy notice on payment completion screen"

## 9. PM 다음 단계
- In-Round (Notion 생성됨): /dev-chat에 §6 사용 + linked view 수동 설정
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

---

> ⚠️ **In-Round로 분류·생성된 Notion 스펙은 PM이 §7 confirm gate에서 명시 진행한 항목만 포함합니다. PM 미확인 In-Round 항목은 Notion으로 가지 않았습니다.**
