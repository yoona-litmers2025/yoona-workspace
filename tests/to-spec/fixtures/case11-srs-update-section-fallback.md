---
case: case11
description: SRS Living Doc — REQ ID 없음 + 도메인 코드 명시 → 섹션 6 그룹 끝에 신규 REQ 자동 채번 (2순위 fallback)
client: Connectory
project: Connectory-1
source: meeting-note
expected:
  bucket: In-Round
  pm_gate_choice: "1"
  srs_update_count: 1
  changelog_entries_added: 1
notes: |
  P2 신규 — In-Round 항목이 REQ ID는 명시 안 했지만 도메인(AUTH)이 명확.
  매칭 알고리즘 2순위(섹션 헤더 fallback) 활성화 — AUTH 그룹 끝에 신규 REQ 자동 채번.
  Change Log entry에는 신규 REQ ID (예: REQ-CON-AUTH-04) 명시.
---

# Source memo (KR, meeting decision)
미팅에서 "로그인 시 2단계 인증(OTP) 추가하기로 결정" 합의됨.
SRS의 어느 REQ에 해당하는지 명시는 없지만 AUTH 도메인 신규 기능.
