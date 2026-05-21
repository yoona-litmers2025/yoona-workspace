---
case: case07
description: SRS Living Doc v1 시드 — Change Log 섹션이 본문 마지막에 자동 추가되고 v1 시드 entry 1건이 들어가는지 검증 (P1 SRS Living Doc seed)
client: Connectory
project: Connectory-3
source_type: text
source_ref: text inline (간결한 회원·결제 메모)
preview_gate_choice: "1"
save_gate_choice: "1"
expected_buckets:
  req_total: 6
  confirm_needed_count: 1
  output_mode: full
notes: |
  P1 신규 — Change Log seed 검증.
  비창작 원칙·REQ 분류·게이트 흐름은 case01과 동일, 핵심 검증은 §9 Change Log v1 entry.
  v1 시드 entry는 [/create-srs] v1 초안 생성 패턴이어야 하며 source 한 줄 요약을 동반.
---

# Source memo (KR)
회원가입 / 로그인 / 비밀번호 변경. 크레딧 충전(카카오페이) + 환불 정책 1건.
