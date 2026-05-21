---
status: Confirmed-1
case: case07
client: rck
project: Rck-Migration
created: 2026-05-21
source_type: notion
source_ref: notion://mock-rck-srs-kr-v1
project_doc_db: collection://bd33aae9-a894-82a9-b8e2-87387e7fbf47
gate_choice: "0"
existing_match_count: 0
archive_target: none
new_page_url: https://notion.so/cigroio/rck-migration-srs-en-v1
version_suffix: none
new_terms_count: 0
translation_section_count: 4
glossary_terms_used: 6
---

## 1. Source Summary

- Source: notion://mock-rck-srs-kr-v1 (RCK migration KR SRS, freshly created)
- Sections detected: 1. Overview / 2. Scope / 3. Functional Requirements / 4. Non-functional Requirements
- KR SRS Change Log: v1 entry only (no prior /to-spec changes yet)

## 2. Glossary Lookup

- glossary/rck.md found — 6 terms loaded
- Notable mappings used: 관리자 → admin / 사용자 → user / 게이트웨이 → gateway

## 3. Confirm Gate

(중복 체크) 같은 프로젝트+유형="SRS 번역"+언어="KR→EN" 매치 0건 → gate prompt 미발동, 바로 생성.

## 4. PM Choice

- gate_choice: "0"
- Resulting actions: Notion 프로젝트 문서 DB 새 페이지 생성

## 5. Translation Output

(preview — Notion에 동일 본문 저장됨)

```
# SRS — Rck-Migration (EN translation, v1)

## 1. Overview
RCK migration replaces the legacy ERP integration path with a new gateway.

## 2. Scope
- In-scope: gateway integration, admin reconciliation, audit log
- Out-of-scope: legacy ERP UI refresh

## 3. Functional Requirements
### 3.1 Gateway Integration
### 3.2 Admin Reconciliation
### 3.3 Audit Log

## 4. Non-functional Requirements
(translated as-is from source — no invention)

## Change Log
> KR SRS is canonical. This English doc tracks updates via pointer-stubs.

- 2026-05-21 [/srs-translate] v1 generated from KR SRS — notion://mock-rck-srs-kr-v1
```

## 6. New Terms

- 0건 — glossary에 모두 매핑됨.

## 7. Notes

- P1 SRS Living Doc — EN Change Log pointer-stub seed 검증 케이스.
- KR SRS Change Log에 v1 entry만 있는 상태 → EN pointer-stub도 v1 1줄.
- 이후 KR SRS에 [/to-spec] entry가 추가될 때마다 EN에는 1줄 pointer-stub 자동 append (canonical writer는 KR, 번역 X — 포인터만).
