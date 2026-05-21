---
status: Confirmed-1
case: case07
client: Connectory
project: Connectory-3
created: 2026-05-21
source_type: text
source_ref: text inline (간결한 회원·결제 메모)
project_doc_db: collection://bd33aae9-a894-82a9-b8e2-87387e7fbf47
preview_gate_choice: "1"
save_gate_choice: "1"
new_page_url: https://notion.so/cigroio/connectory-3-srs-draft
req_total: 6
confirm_needed_count: 1
out_of_scope_count: 0
output_mode: full
custom_domain_codes: []
---

## 1. Source Summary

- Source: text inline (간결한 회원·결제 메모, KR)
- Coverage: 회원 가입·로그인·비밀번호 변경 / 크레딧 충전·환불

## 2. REQ Extraction Summary

| 그룹 | 도메인 코드 | REQ 개수 |
|---|---|---|
| 인증·회원 | AUTH | 3 |
| 결제·크레딧 | PAY | 3 |
| **합계** | | **6건** |

- 확인 필요: 1건
- 커스텀 도메인 코드: 없음

## 3. Step 3 Preview

```
## SRS 초안 미리보기
프로젝트: Connectory-3 / 클라이언트: Connectory

기능 그룹: 2개, REQ 6건
확인 필요: 1건 / 제외사항: 0건
출력 모드: full
섹션 구조: 1. 개요 / 2. 배경 / 3. 범위 / 4. IA / 5. 요약 / 6. 상세 / 7. 확인 필요 / 9. Change Log (v1 시드)

진행 / 수정 / 취소?
```

## 4. Preview Gate Choice

- preview_gate_choice: "1" (진행)

## 5. SRS Draft

### 5. 기능명세 요약 (인덱스)
| REQ ID | 요구사항 |
|---|---|
| REQ-AUTH-01 | 회원 가입 |
| REQ-AUTH-02 | 로그인 |
| REQ-AUTH-03 | 비밀번호 변경 |
| REQ-PAY-01 | 크레딧 충전 (카카오페이) |
| REQ-PAY-02 | 결제 검증 [추론] |
| REQ-PAY-03 | 환불 정책 |

### 7. 확인 필요 사항
| 분류 | 질문 |
|---|---|
| 정책 확인 | 환불 정책 세부 룰 미정 (REQ-PAY-03) |

## 6. Step 6 Save Gate

```
Notion 프로젝트 문서 DB에 저장할까요?
1. 저장 (추천)
2. 수정 후 저장
3. 저장 안 함
```

## 7. Save Gate Choice

- save_gate_choice: "1" (저장)
- Resulting actions: Notion 프로젝트 문서 DB에 SRS 초안 저장 — https://notion.so/cigroio/connectory-3-srs-draft

## 8. Notes

- P1 SRS Living Doc seed 검증 케이스. v1 시드 entry가 §9에 1건만 들어가는지 확인.
- 이후 변경은 /to-spec In-Round bucket이 entry 추가 (canonical writer). 본 라운드는 v1 시드만.

## 9. Change Log

(SRS 본문 마지막 섹션 — Notion 페이지에 동일 본문 저장됨. append-only — 이후 /to-spec이 entry 추가.)

- 2026-05-21 [/create-srs] v1 초안 생성
  Source: text inline (간결한 회원·결제 메모, KR)
