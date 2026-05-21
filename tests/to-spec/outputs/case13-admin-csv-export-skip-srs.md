---
status: In-Round-only
client: Connectory
project: Connectory-1
created: 2026-05-21
source: free-text
source_ref: "tests/to-spec/fixtures/case13-gate-option2-skip-srs.md (test fixture)"
srs_ref: clients/connectory/Connectory-1/srs.md
design_md: missing
spec_pages:
  - "https://www.notion.so/cigroio/mock-spec-page-url-admin-csv-export"
srs_update_count: 0
changelog_entries_added: 0
---

# Request Triage — 관리자 회원 검색 CSV 내보내기 (PM 의도적 SRS skip)

> Reference draft — official spec lives in Nexus / PM Notion. In-Round 항목은 PM confirm 후 커뮤니케이션 DB / 태스크 DB / SRS 본문 / Change Log에 자동 반영됩니다.

## 1. 변경 요청 요약
- 누가 / 언제 / 어떤 채널: Connectory 고객사, 2026-05-21, 직접 피드백
- 원문 인용:
  > "관리자 페이지에서 회원 검색 결과를 CSV로 내보내는 버튼이 필요합니다. 지금 검색은 잘 되는데, 결과를 엑셀로 받아볼 방법이 없네요."
- PM 1-line 정규화: 관리자 회원 검색 결과 CSV 내보내기 버튼 추가 — ADMIN 기능 확장.

## 2. 기존 범위 대비 영향도
- SRS 참조: REQ-CON-ADMIN-02 (회원 검색) 관련 — CSV 내보내기는 신규
- 영향 분류: 기존 기능 확장
- 전체 Impact: Low

## 3. 화면·UX 영향
- [확인 필요] design.md 부재 — UI 영향 상세 판단은 design owner / Nexus Agent 확인 필요
- design.md 갱신 필요 여부: 판단 보류
- wireframe 필요 여부: 불필요

## 4. 4-Bucket Triage

### In-Round
- [ ] 관리자 회원 검색 결과 CSV 내보내기 / 기존 ADMIN 검색 확장, 명확 근거 / Impact: Low

### Next-Round
(현재 항목 없음)

### Out-of-Scope
(현재 항목 없음)

### Confirm-Needed
(현재 항목 없음)

## 5. 고객 확인 / 거절 안내
(현재 확인 필요·거절 안내 항목 없음)

## 6. 개발팀 전달 문구
- English summary: Add CSV export button on admin member search result. Extends ADMIN search capability.
- 영향 SRS section: REQ-CON-ADMIN-02 (참조만, SRS 본문 patch 안 함 — PM 의도적 skip)
- AC 후보:
  - When admin clicks export button on search result, then a CSV file is downloaded with the visible columns
- Impact: Low (구체 공수 산정은 dev 확인)

## 7. PM Confirm Gate

```
[확인 필요]
다음 In-Round 항목을 4가지 변경으로 생성합니다:

스펙 페이지: Add CSV export button on admin member search result
태스크: 1개 (Implement CSV export endpoint + button)
SRS 본문 patch: REQ-CON-ADMIN-02 — CSV 내보내기 capability 확장
Change Log entry: 1건

1. 전체 진행 (4가지 모두 — 권장)
2. SRS 본문·Change Log skip (스펙·태스크만)
3. 수정 (4-bucket 분류 다시 검토)
4. 취소

추천: 1
```

PM 선택: **2 (SRS 본문·Change Log skip)** — PM이 SRS 정합성을 별도 라운드에서 일괄 정리할 계획. 본 라운드는 스펙·태스크만 생성. SRS 본문·Change Log unchanged.

## 8. Notion 스펙 + 태스크 + SRS 본문 + Change Log
- 스펙 페이지: https://www.notion.so/cigroio/mock-spec-page-url-admin-csv-export
- 태스크 1개:
  - [ ] Implement CSV export endpoint + button (Priority: Medium / AC: CSV downloaded with visible columns / link: mock)
- SRS 본문 patch: (skip — PM gate option 2 선택)
- Change Log entry: (skip — PM gate option 2 선택)
- linked view 수동 설정 안내: 스펙 페이지 하단 /linked view → 태스크 DB 추가 → 필터: 스펙 출처 = "Add CSV export button on admin member search result"

## 9. PM 다음 단계
- In-Round (Notion 생성됨, SRS skip): /dev-chat에 §6 사용 + linked view 수동 설정
- [확인 필요] SRS 본문·Change Log 반영 skip됨 — SRS와 실제 코드 drift 위험. 추후 정리 시점에 본 triage 파일 재검토 권장.
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
- SRS 정합성 정리: 별도 라운드에서 본 triage + 다른 skip 항목을 일괄 SRS 반영 (재호출 시 PM 옵션 1 선택)

---

> ⚠️ **In-Round로 분류·생성된 Notion 스펙은 PM이 §7 confirm gate에서 명시 진행한 항목만 포함합니다. PM 미확인 In-Round 항목은 Notion으로 가지 않았습니다.**
