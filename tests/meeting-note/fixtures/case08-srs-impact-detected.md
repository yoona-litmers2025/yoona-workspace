---
case: case08
description: SRS-impact 의심 항목 감지 (Step 5.5) — 확정된 것 + 바로 진행할 일에서 키워드 매치 시 §6에 표시 (P3)
client: Connectory
project: Connectory-1
meeting_date: 2026-05-21
gate_choice: "0"
existing_match_count: 0
action_items_count: 2
expected_srs_impact_count: 2
notes: |
  P3 신규 — 미팅에서 "결제 환불 정책 변경 결정" + "회원 등급 시스템 추가 합의".
  Step 5.5가 동사 ("변경", "추가") + 신규 기능 성격 감지 → §6에 SRS-impact 의심 항목 2건 출력.
  자동 chain 금지 — PM이 /to-spec 직접 호출 시점 결정.
---

# Meeting transcript snippet
Yoona (PM): 오늘 두 가지 핵심 결정이 있었습니다.
Kim (Client): 첫째, 결제 환불 정책을 변경하기로 합의했습니다. 영업일 처리.
Tuan (Dev): 네, 그 부분 Dev에서 처리하겠습니다.
Kim: 둘째, 회원 등급 시스템을 추가하기로 했습니다. Bronze / Silver / Gold 3단계.
Tuan: 이 부분도 Dev에서 진행하면 됩니다.
