# Claude Code PM Assistant — 설계 & 이용 가이드

## 1. 시스템 개요

아웃소싱 개발사 PM이 **한국 클라이언트 ↔ 베트남 개발/디자인팀** 사이에서 수행하는 반복 업무를 Claude Code로 자동화한 워크플로우 시스템입니다.

### 핵심 설계 원칙

| 원칙 | 설명 |
|------|------|
| **언어 자동 분리** | 클라이언트 방향 → 한국어(존댓말), 개발팀 방향 → 영어(간결체) |
| **모호함 절대 금지** | 번역/해석 시 애매한 부분은 반드시 플래그 처리, 임의 해석 불가 |
| **번역 vs 해석 분리** | 원문 번역과 Claude 추론을 명확히 구분 표기 |
| **용어 일관성** | 클라이언트별 용어집(glossary) 기반, 동의어 사용 금지 |
| **프로젝트별 컨텍스트** | 고객사별 커뮤니케이션 스타일·도메인 지식 자동 로드 |

---

## 2. 시스템 구조

### 로컬 워크스페이스 (`yoona-workspace/`)

```
yoona-workspace/
├── CLAUDE.md                    # 전체 시스템 규칙 (Claude가 자동 로드)
├── guide.md                     # 이 가이드 문서
│
├── clients/                     # 고객사별 컨텍스트
│   ├── CLAUDE.md                # 클라이언트 커뮤니케이션 기본 규칙
│   └── {client-name}/
│       └── CLAUDE.md            # 고객사별 상세 컨텍스트
│                                  (담당자 성향, 커뮤니케이션 스타일, 도메인)
│
├── glossary/                    # 고객사별 용어집
│   └── {client-name}.md         # Korean ↔ English 용어 매핑 테이블
│
├── .claude/commands/             # 슬래시 커맨드 (Skills)
│   ├── srs-translate.md         # /srs-translate — SRS 번역
│   ├── kickoff-prep.md          # /kickoff-prep — 킥오프 준비
│   ├── to-spec.md               # /to-spec — 요청→개발 스펙
│   ├── to-client.md             # /to-client — 개발→클라이언트 보고
│   ├── weekly-report.md         # /weekly-report — 주간 리포트
│   ├── issue-ticket.md          # /issue-ticket — Linear 이슈 티켓
│   └── new-project.md           # /new-project — 새 프로젝트 셋업
│
├── templates/                   # 문서 템플릿 (커맨드가 내부적으로 참조)
│   ├── srs-translation.md       # SRS 번역 (KR→EN)
│   ├── kickoff-prep.md          # 킥오프 미팅 준비
│   ├── request-to-spec.md       # 클라이언트 요청 → 개발 스펙
│   ├── dev-update-to-client.md  # 개발 업데이트 → 클라이언트 보고
│   ├── weekly-report.md         # 주간 리포트
│   └── issue-ticket.md          # Linear 이슈 티켓
│
└── handoffs/                    # 로컬 드래프트 (최종본은 Notion)
    └── CLAUDE.md                # Handoff 작성 규칙 & 체크리스트
```

### 핵심 파일별 역할

| 파일 | 역할 | 자동 로드 |
|------|------|-----------|
| `CLAUDE.md` (루트) | 전체 워크플로우 규칙, 번역 원칙, Notion DB 연결 정보 | ✅ 항상 |
| `clients/CLAUDE.md` | 클라이언트 커뮤니케이션 기본 톤·구조 규칙 | ✅ clients/ 진입 시 |
| `clients/{name}/CLAUDE.md` | 고객사별 담당자 성향, 도메인 컨텍스트 | ✅ 해당 디렉토리 진입 시 |
| `glossary/{name}.md` | 용어 매핑 (번역 시 자동 참조) | 번역 작업 시 |
| `templates/*.md` | 문서 구조 가이드 (프로세스 + 출력 포맷) | 해당 작업 요청 시 |
| `handoffs/CLAUDE.md` | 개발팀 전달 문서 품질 체크리스트 | ✅ handoffs/ 진입 시 |

---

## 3. Notion PM Workspace

### 구조

```
📋 PM Workspace
├── 📂 프로젝트별 현황 (토글)
│   └── 📂 Koboom (토글, 파란 배경)
│       ├── Koboom 문서 (링크드 뷰, 클라이언트=Koboom 필터)
│       └── Koboom 커뮤니케이션 (링크드 뷰, 클라이언트=Koboom 필터)
│   └── (새 프로젝트 추가 시 같은 구조로 토글 추가)
│
├── ───── (구분선) ─────
│
└── 📂 전체 DB
    ├── 프로젝트 문서 DB (원본)
    └── 커뮤니케이션 DB (원본)
```

### 프로젝트 문서 DB

프로젝트 라이프사이클 전반의 문서를 관리합니다.

| 속성 | 타입 | 용도 |
|------|------|------|
| 문서명 | Title | 문서 제목 |
| 클라이언트 | Select | 고객사 필터링 |
| 프로젝트 | Text | 프로젝트명 |
| 유형 | Select | SRS 번역 / Kickoff 자료 / 기획 확인 / 디자인 확인 / Handoff |
| 단계 | Select | SRS → Kickoff → Planning → Design → Development → QA |
| 상태 | Status | 시작 전 / 진행 중 / 완료 |
| 언어 | Select | KR / EN / KR→EN |
| 작성일 | Date | 문서 작성일 |
| 전달일 | Date | 전달 완료일 |

**뷰 구성:**
- 클라이언트별 (보드) — 고객사별 문서 현황
- 단계별 진행현황 (보드) — 칸반 형태로 단계 추적
- 상태별 (보드) — 시작 전 / 진행 중 / 완료

### 커뮤니케이션 DB

프로젝트 진행 중 오가는 모든 커뮤니케이션을 기록합니다.

| 속성 | 타입 | 용도 |
|------|------|------|
| 제목 | Title | 커뮤니케이션 제목 |
| 클라이언트 | Select | 고객사 필터링 |
| 프로젝트 | Text | 프로젝트명 |
| 유형 | Select | 주간 리포트 / 클라이언트 업데이트 / 개발 스펙 / 이슈 티켓 / 질의응답 |
| 상태 | Status | 시작 전 / 진행 중 / 완료 |
| 방향 | Select | Client→Dev / Dev→Client |
| 작성일 | Date | 작성일 |

**뷰 구성:**
- 클라이언트별 (보드) — 고객사별 커뮤니케이션
- 유형별 (보드) — 리포트, 스펙, 이슈 등 분류
- 최근순 (테이블) — 작성일 내림차순 전체 목록

---

## 4. 프로젝트 라이프사이클

프로젝트는 아래 순서를 따릅니다. 각 단계에서 사용할 템플릿과 출력 위치가 정해져 있습니다.

```
① Sales Handover     ─→  SRS/기획서 수령 (Notion, 한국어)
        ↓
② SRS Translation    ─→  templates/srs-translation.md → Notion 프로젝트 문서 DB
        ↓
③ Kickoff Prep       ─→  templates/kickoff-prep.md → Notion 프로젝트 문서 DB
        ↓
④ Planning Confirm   ─→  클라이언트 확인 (한국어) → Notion 커뮤니케이션 DB
        ↓
⑤ Design Confirm     ─→  클라이언트 확인 (한국어) → Notion 커뮤니케이션 DB
        ↓
⑥ Final Handoff      ─→  templates/request-to-spec.md → Notion 프로젝트 문서 DB
        ↓
⑦ Ongoing            ─→  weekly-report / dev-update / issue-ticket → Notion 커뮤니케이션 DB
```

---

## 5. 슬래시 커맨드 (Skills)

Claude Code에서 `/커맨드명`으로 바로 실행할 수 있는 자동화 명령어입니다.
각 커맨드는 해당 템플릿 + 용어집 + 클라이언트 컨텍스트를 자동으로 로드하고, 결과를 Notion에 저장합니다.

### 커맨드 목록

| 커맨드 | 기능 | 입력 언어 | 출력 언어 | 저장 위치 |
|--------|------|-----------|-----------|-----------|
| `/srs-translate` | SRS/기획서 번역 및 구조화 | 한국어 | 영어 | 프로젝트 문서 DB |
| `/kickoff-prep` | 킥오프 미팅 안건·내부 준비 | 영어 (SRS 번역본) | KR + EN | 프로젝트 문서 DB |
| `/to-spec` | 클라이언트 요청 → 개발 스펙 | 한국어 | 영어 | 커뮤니케이션 DB |
| `/to-client` | 개발 업데이트 → 클라이언트 보고 | 영어 | 한국어 | 커뮤니케이션 DB |
| `/weekly-report` | 주간 리포트 작성 | 한국어/영어 | 한국어 | 커뮤니케이션 DB |
| `/issue-ticket` | Linear 이슈 티켓 생성 | 한국어/영어 | 영어 | Linear |
| `/new-project` | 새 프로젝트 전체 셋업 | — | — | 로컬 + Notion |

---

### `/srs-translate` — SRS 번역

**사용 시점:** 클라이언트로부터 한국어 SRS/기획서를 받았을 때

**사용법:**
```
/srs-translate [Notion 링크 또는 텍스트] --client koboom
```

**자동 수행:**
1. 용어집(`glossary/koboom.md`) 로드
2. 클라이언트 컨텍스트(`clients/koboom/CLAUDE.md`) 로드
3. SRS 번역 (Overview → Scope → Requirements)
4. ⚠️ Ambiguities & Open Questions 섹션 생성 (필수)
5. New Terms 섹션 생성 (첫 번역 시 필수)
6. Inferred Requirements 분리 표기
7. Notion 프로젝트 문서 DB에 저장
8. 용어집 업데이트 제안

---

### `/kickoff-prep` — 킥오프 준비

**사용 시점:** SRS 번역 완료 후, 킥오프 미팅 전

**사용법:**
```
/kickoff-prep --client koboom [SRS 번역본 Notion 링크]
```

**자동 수행:**
1. SRS 번역본에서 토론 포인트·Ambiguities 추출
2. **Part A** 생성: 킥오프 안건 (한국어, 클라이언트용)
3. **Part B** 생성: Internal Prep Notes (영어, PM용) — 리스크, 블로킹 질문, 용어 갭
4. Notion 프로젝트 문서 DB에 저장

---

### `/to-spec` — 클라이언트 요청 → 개발 스펙

**사용 시점:** 클라이언트 요청/변경사항을 개발팀 스펙으로 전환할 때

**사용법:**
```
/to-spec [한국어 요청 텍스트 또는 Notion 링크] --client koboom
```

**자동 수행:**
1. 클라이언트 요청에서 실제 요구사항 추출 (불만/맥락 분리)
2. Summary → Requirements → Acceptance Criteria → Edge Cases → Open Questions
3. 한국어 원문 하단 보존
4. Notion 커뮤니케이션 DB에 저장 (방향: Client→Dev)

---

### `/to-client` — 개발 업데이트 → 클라이언트 보고

**사용 시점:** 개발팀 영어 업데이트를 클라이언트에게 한국어로 전달할 때

**사용법:**
```
/to-client [영어 개발 업데이트 내용] --client koboom
```

**자동 수행:**
1. 항목 분류: 완료 / 진행 중 / 블로킹 / 예정
2. 기술 용어 → 클라이언트 친화적 한국어 전환
3. 시간 추정 → 캘린더 날짜 변환
4. 클라이언트 톤에 맞춰 출력 (예: Koboom → 따뜻하고 안심되는 톤)
5. Notion 커뮤니케이션 DB에 저장 (방향: Dev→Client)

---

### `/weekly-report` — 주간 리포트

**사용 시점:** 매주 클라이언트에게 진행 상황 보고

**사용법:**
```
/weekly-report --client koboom [이번 주 업데이트 내용]
```

**자동 수행:**
1. Linear에서 이번 주 이슈 현황 확인 (가능 시)
2. 주요 성과 → 진행 현황 테이블 → 이슈/리스크(+대응방안) → 다음 주 계획
3. 클라이언트 확인 요청 사항 정리
4. Notion 커뮤니케이션 DB에 저장 (방향: Dev→Client)

---

### `/issue-ticket` — Linear 이슈 티켓

**사용 시점:** 버그/기능 요청을 Linear 이슈로 생성할 때

**사용법:**
```
/issue-ticket [요청 내용] --client koboom --priority high
```

**자동 수행:**
1. 영어 티켓 작성: Title / What / Why / Acceptance Criteria / Technical Notes
2. Labels 자동 분류 (bug / feature / improvement)
3. 사용자 확인 후 Linear에 이슈 생성

---

### `/new-project` — 새 프로젝트 셋업

**사용 시점:** 새 고객사/프로젝트가 들어왔을 때

**사용법:**
```
/new-project --client [client-name] --project [project-name]
```

**자동 수행:**
1. 필요 정보 수집 (고객사명, 담당자, 커뮤니케이션 스타일, 도메인 용어)
2. `clients/{name}/CLAUDE.md` 생성 (고객사 컨텍스트)
3. `glossary/{name}.md` 생성 (용어집)
4. Notion PM Workspace에 프로젝트 토글 + 링크드 뷰(필터) 추가

---

## 7. 연동 도구

| 도구 | 용도 | 연동 방식 |
|------|------|-----------|
| **Notion** | SRS, 스펙, 미팅노트, 리포트 등 문서 관리 | MCP (claude.ai Notion) |
| **Linear** | 이슈 트래킹, 티켓 생성 | MCP (claude.ai Linear) |
| **Google Sheets** | 타임라인, 대시보드, 클라이언트 공유 | MCP (google-sheets) |

---

## 8. 현재 등록된 프로젝트

| 고객사 | 프로젝트 | 설명 | 담당자 |
|--------|---------|------|--------|
| Koboom | Koboom | K-pop 포토카드 중고 거래 플랫폼 (유럽 기반) | 김혜미 대표님 |
