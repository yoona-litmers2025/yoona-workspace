---
case: case10
description: SRS Living Doc — REQ ID 1순위 매칭 → SRS 본문 patch + Change Log entry (P2 canonical writer)
client: Connectory
project: Connectory-1
source: free-text
expected:
  bucket: In-Round
  pm_gate_choice: "1"
  srs_update_count: 1
  changelog_entries_added: 1
notes: |
  P2 신규 — In-Round 항목이 기존 REQ-CON-PAY-03을 직접 참조.
  PM이 옵션 1(전체 진행) 선택 → 스펙·태스크·SRS 본문 patch·Change Log entry 4가지 모두 생성.
  핵심 검증: REQ ID 매칭으로 섹션 6의 해당 REQ가 in-place 갱신되고
  Change Log entry가 append-only 형식으로 추가됨.
---

# Source memo (KR, client request)
결제 완료 화면 환불 안내 문구를 추가해주세요. 현재 REQ-CON-PAY-03 결제 완료 화면에 환불 정책 한 줄 안내가 빠져 있어요.
"환불 신청은 영업일 이내 가능합니다" 같은 안내 문구가 필요합니다.
