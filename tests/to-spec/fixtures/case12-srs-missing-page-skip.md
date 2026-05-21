---
case: case12
description: SRS Living Doc — srs_ref missing → Part E auto-skip + §9 warning (P2 safe-fail)
client: Koboom
project: Koboom
source: free-text
expected:
  bucket: In-Round
  pm_gate_choice: "1"
  srs_update_count: 0
  changelog_entries_added: 0
notes: |
  P2 신규 — In-Round 항목은 있지만 srs_ref가 missing (SRS 페이지 미연결).
  PM이 옵션 1(전체 진행) 선택해도 Part E는 자동 skip — 스펙·태스크만 생성.
  §9에 "[확인 필요] SRS 미연결 — /create-srs 또는 PM 수동 연결 권장" 명시.
  Hard-fail 금지 — partial-skip으로 처리.
---

# Source memo (KR, client request)
크레딧 결제 환불 안내 메일 발송 기능 추가 부탁드립니다.
환불 처리 완료 시 자동으로 안내 메일이 가도록 해주세요.
