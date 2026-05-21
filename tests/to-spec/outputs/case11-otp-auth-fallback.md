---
status: In-Round-only
client: Connectory
project: Connectory-1
created: 2026-05-21
source: meeting-note
source_ref: "tests/to-spec/fixtures/case11-srs-update-section-fallback.md (test fixture)"
srs_ref: clients/connectory/Connectory-1/srs.md
design_md: missing
spec_pages:
  - "https://www.notion.so/cigroio/mock-spec-page-url-2fa-otp"
srs_update_count: 1
changelog_entries_added: 1
---

# Request Triage — 로그인 2단계 인증(OTP) 추가 (AUTH 도메인 fallback 채번)

> Reference draft — official spec lives in Nexus / PM Notion. In-Round 항목은 PM confirm 후 커뮤니케이션 DB / 태스크 DB / SRS 본문 / Change Log에 자동 반영됩니다.

## 1. 변경 요청 요약
- 누가 / 언제 / 어떤 채널: Connectory 고객사 + Dev, 2026-05-21, 미팅 결정
- 원문 인용:
  > "미팅에서 '로그인 시 2단계 인증(OTP) 추가하기로 결정' 합의됨."
- PM 1-line 정규화: 로그인 흐름에 OTP 기반 2단계 인증 추가 — AUTH 도메인 신규 기능.

## 2. 기존 범위 대비 영향도
- SRS 참조: REQ ID 미명시 — AUTH 도메인 신규 항목. fallback (2순위) 매칭 적용.
- 영향 분류: 신규 기능 (보안 강화)
- 전체 Impact: Medium

## 3. 화면·UX 영향
- [확인 필요] design.md 부재 — UI 영향 상세 판단은 design owner / Nexus Agent 확인 필요
- design.md 갱신 필요 여부: 필요 [추론 — OTP 입력 화면 신규]
- wireframe 필요 여부: 판단 보류

## 4. 4-Bucket Triage

### In-Round
- [ ] 로그인 2단계 인증(OTP) 추가 / 미팅에서 합의 / Impact: Medium

### Next-Round
(현재 항목 없음)

### Out-of-Scope
(현재 항목 없음)

### Confirm-Needed
(현재 항목 없음)

## 5. 고객 확인 / 거절 안내
(현재 확인 필요·거절 안내 항목 없음)

## 6. 개발팀 전달 문구
- English summary: Add OTP-based 2FA on login flow. New AUTH-domain capability — see SRS REQ-CON-AUTH-04 (auto-numbered via fallback).
- 영향 SRS section: REQ-CON-AUTH-04 (신규 채번, fallback 매칭)
- AC 후보:
  - When user submits credentials, then OTP step is presented before session is granted
- Impact: Medium (구체 공수 산정은 dev 확인)

## 7. PM Confirm Gate

```
[확인 필요]
다음 In-Round 항목을 4가지 변경으로 생성합니다:

스펙 페이지: Add OTP-based 2FA to login flow
태스크: 1개 (Implement OTP challenge on login)
SRS 본문 patch: REQ-CON-AUTH-04 신규 채번 — AUTH 그룹 끝에 추가 (fallback 매칭, 2순위)
Change Log entry: 1건

1. 전체 진행 (4가지 모두 — 권장)
2. SRS 본문·Change Log skip (스펙·태스크만)
3. 수정 (4-bucket 분류 다시 검토)
4. 취소

추천: 1
```

PM 선택: **1 (전체 진행)** — fallback 매칭 적용, AUTH 그룹 끝에 REQ-CON-AUTH-04 자동 채번 + 4가지 변경 모두 생성.

## 8. Notion 스펙 + 태스크 + SRS 본문 + Change Log
- 스펙 페이지: https://www.notion.so/cigroio/mock-spec-page-url-2fa-otp
- 태스크 1개:
  - [ ] Implement OTP challenge on login (Priority: High / AC: OTP step before session / link: mock)
- SRS 본문 patch: REQ-CON-AUTH-04 신규 채번 — 매칭 알고리즘 2순위(섹션 헤더 fallback) 적용. AUTH 도메인 그룹 끝에 추가.
- Change Log entry (SRS 페이지 끝에 append):
  - `- 2026-05-21 [/to-spec] REQ-CON-AUTH-04 — 로그인 OTP 2단계 인증 신규 추가 / Source: https://www.notion.so/cigroio/mock-spec-page-url-2fa-otp / Trigger: meeting decision`
- linked view 수동 설정 안내: 스펙 페이지 하단 /linked view → 태스크 DB 추가 → 필터: 스펙 출처 = "Add OTP-based 2FA to login flow"

## 9. PM 다음 단계
- In-Round (Notion 생성됨): /dev-chat에 §6 사용 + linked view 수동 설정
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

---

> ⚠️ **In-Round로 분류·생성된 Notion 스펙은 PM이 §7 confirm gate에서 명시 진행한 항목만 포함합니다. PM 미확인 In-Round 항목은 Notion으로 가지 않았습니다.**
