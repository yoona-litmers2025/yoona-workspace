# Template: Kickoff Preparation

## Input
- Translated SRS (English, from `srs-translation` template)
- Client context from `clients/{client-name}/CLAUDE.md`
- Glossary from `glossary/{client-name}.md`

## Process
1. Extract key discussion points from the translated SRS
2. Identify all items from the Ambiguities section — these become kickoff agenda items
3. Identify scope boundaries that need client confirmation
4. Prepare questions grouped by topic
5. Draft agenda in Korean (for the client) AND English (for internal reference)

## Output Format

### Part A: Kickoff Agenda (Korean, for client)
```
[프로젝트명] 킥오프 미팅 안건

일시: [날짜/시간]
참석자: [참석자 목록]

## 1. 프로젝트 개요 확인
- 프로젝트 목적 및 범위 확인
- 주요 일정 확인

## 2. 요구사항 확인 사항
- [확인이 필요한 항목 1]
  → 배경: [왜 확인이 필요한지]
- [확인이 필요한 항목 2]
  → 배경: [왜 확인이 필요한지]

## 3. 기술/디자인 관련 논의
- [논의 항목]

## 4. 커뮤니케이션 및 진행 방식
- 보고 주기 및 방식
- 피드백 프로세스
- 주요 연락 채널

## 5. 다음 단계
- [액션 아이템]
```

### Part B: Internal Prep Notes (English, for PM)
```
## Key Risks to Raise
- [Risk from SRS ambiguity analysis]

## Questions That Must Be Answered Before Development
- [Blocking question 1] — blocks: [which feature/requirement]
- [Blocking question 2] — blocks: [which feature/requirement]

## Glossary Gaps
- [Terms that need client confirmation]

## Suggested Timeline Discussion Points
- [Milestone or deadline that seems unrealistic, if any]
```
