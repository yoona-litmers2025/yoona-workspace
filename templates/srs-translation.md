# Template: SRS Translation (KR → EN)

This is the highest-volume, highest-impact template.
Errors here propagate to kickoff, planning, design, and development.

## Input
Korean SRS document (from Notion or pasted text)

## Process
1. Read the full SRS before translating — understand structure and scope first
2. Check `glossary/{client-name}.md` for established term mappings
3. Translate faithfully — do NOT add, remove, or reinterpret requirements
4. Restructure for English readability if the Korean structure is hard to follow
5. Flag every ambiguity — never resolve silently
6. List all new domain terms you translated (for glossary review)

## Output Format
```
# [Project Name] — SRS (English Translation)

> Source: [Notion link or reference]
> Translated: [Date]
> Client: [Client name]
> Status: Draft — pending PM review

---

## 1. Overview
[Translated project overview / background]

## 2. Scope
[What is included and excluded]

## 3. Functional Requirements
### 3.1 [Feature Area]
- FR-001: [Requirement]
- FR-002: [Requirement]
(Maintain original numbering if the SRS has it)

### 3.2 [Feature Area]
- FR-003: [Requirement]

## 4. Non-Functional Requirements
- [Performance, security, compatibility, etc.]

## 5. Ambiguities & Open Questions
⚠️ These items need clarification before kickoff or handoff:
- [ ] [Section X]: "[Korean original]" — could mean [A] or [B]. Which is intended?
- [ ] [Section Y]: No detail on [topic]. Developers will need [specific info].
- [ ] [Section Z]: Contradicts [other section]. Which takes priority?

## 6. New Terms (for glossary review)
| Korean | English (used in this doc) | Confidence | Notes |
|--------|---------------------------|------------|-------|
| [term] | [translation] | High/Medium/Low | [why low confidence, if applicable] |

## 7. Inferred Requirements
These are NOT in the original SRS but seem implied. PM should confirm before including in handoff:
- [Inferred requirement] — inferred because [reason]

## 8. Original Reference
> [Key Korean sections preserved for cross-reference, especially ambiguous parts]
```

## Key Rules
- Section 5 (Ambiguities) is MANDATORY. If you think there are zero ambiguities in an SRS, you are wrong — look harder.
- Section 6 (New Terms) is MANDATORY on first translation for a client.
- Section 7 (Inferred) keeps Claude's additions visibly separate from the client's actual requirements.
- Mark the whole document as "Draft — pending PM review" until the PM confirms.
