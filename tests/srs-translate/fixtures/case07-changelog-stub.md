---
case: case07
description: SRS Living Doc — 영문 SRS Change Log pointer-stub 시드 검증 (P1)
client: rck
project: Rck-Migration
source_type: notion
source_ref: notion://mock-rck-srs-kr-v1
gate_choice: "0"
expected:
  existing_match_count: 0
  new_terms_count: 0
  translation_section_count: 4
notes: |
  P1 신규 — 영문 SRS 본문 끝에 `## Change Log` 섹션이 자동 추가되고
  v1 generation pointer-stub 1줄이 들어가는지 검증.
  한국어 SRS는 v1 단계라 추가 Change Log entry 없음 — pointer-stub도 v1 1줄만.
---

# Source memo
RCK migration KR SRS v1 (newly created), no prior EN translation exists.
Translation should produce a fresh EN SRS with the Change Log pointer-stub seeded.
