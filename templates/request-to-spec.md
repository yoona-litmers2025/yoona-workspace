# Template: Client Request → Dev Spec

## Input
Korean client request (message, email, screenshot, or Notion page)

## Process
1. Extract what the client actually wants (separate requests from complaints/context)
2. Identify implicit requirements the client assumes but didn't state
3. Structure into spec page (overview) + individual tasks (DB entries)
4. Flag ambiguities as questions

## Output: Two Parts

### Part 1 — Spec Page (커뮤니케이션 DB)
Overview document for context and reference.
```
## [Title] — 한 줄로 뭘 해야 하는지

**Context**
왜 이걸 해야 하는지 1-2문장

**Scope Summary**
| Area | Description |
|------|-------------|
| [기능 영역 1] | [무엇을 구현하는지 설명] |
| [기능 영역 2] | [무엇을 구현하는지 설명] |

**Constraints** (있을 때만)
- 제한사항/주의사항

**Open Questions** (있을 때만)
- 개발팀 확인 필요사항

**SRS Impact**
- Affects: [REQ ID] / Type: [Scope change|Clarification|New]

**Ref**
> 원문 (한국어)
```

### Part 2 — Tasks (태스크 DB)
Scope의 각 구현 항목을 개별 태스크로 생성. 개발팀이 상태를 추적하고 관리할 수 있음.

Each task entry:
- 태스크: 구체적 구현 항목 (한 줄)
- 상태: 시작 전 (default)
- 우선순위: High / Medium / Low
- 클라이언트: (자동 설정)
- 프로젝트: (자동 설정)
- 스펙 출처: (Part 1 페이지 URL)
- AC: When [action], then [result] — 이 태스크만의 acceptance criteria
- 비고: edge cases, technical notes (있을 때만)
