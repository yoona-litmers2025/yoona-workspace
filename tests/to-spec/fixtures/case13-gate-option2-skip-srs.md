---
case: case13
description: SRS Living Doc — PM이 gate 옵션 2 (SRS skip) 명시 선택 → 스펙·태스크 생성, SRS 본문·Change Log unchanged
client: Connectory
project: Connectory-1
source: free-text
expected:
  bucket: In-Round
  pm_gate_choice: "2"
  srs_update_count: 0
  changelog_entries_added: 0
notes: |
  P2 신규 — srs_ref가 정상이고 In-Round 매칭도 가능하지만 PM이 옵션 2 선택.
  스펙·태스크는 생성, SRS 본문·Change Log는 skip. escape hatch 사용 사례.
  §9에 "[확인 필요] SRS skip됨 — drift 위험" warning.
  예시 시나리오: SRS 정합성을 별도 라운드에서 일괄 정리하려고 PM이 의도적 skip.
---

# Source memo (KR, client request)
관리자 페이지에서 회원 검색 결과를 CSV로 내보내는 버튼이 필요합니다.
지금 검색은 잘 되는데, 결과를 엑셀로 받아볼 방법이 없네요.
