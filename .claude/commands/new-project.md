---
description: 새 프로젝트 셋업 (로컬 파일 + Notion 뷰)
argument-hint: --client <client-name> --project <project-name>
allowed-tools: Read, Write, Glob, Grep, Bash(mkdir:*), mcp__claude_ai_Notion__notion-fetch, mcp__claude_ai_Notion__notion-create-pages, mcp__claude_ai_Notion__notion-update-page, mcp__claude_ai_Notion__notion-create-view, mcp__claude_ai_Notion__notion-update-view, mcp__claude_ai_Notion__notion-update-data-source
---

# New Project Setup

## Arguments
사용자 입력: $ARGUMENTS

## Instructions

새 프로젝트를 셋업합니다. 아래 4단계를 순서대로 실행하세요.

### Step 1: 고객사 정보 수집
사용자에게 아래 정보를 확인합니다 (인자로 제공되지 않은 항목만):
- 고객사명
- 프로젝트명
- 프로젝트 설명
- 담당자 (이름, 직급)
- 커뮤니케이션 스타일 (특이사항)
- 주요 도메인 용어

### Step 2: 로컬 파일 생성
1. `clients/{client-name}/CLAUDE.md` 생성
   - Overview: 고객사명, 프로젝트명, 설명, 담당자
   - Communication Style: 담당자 성향, 주의사항
   - Tone: 기본 해요체, 공식 문서 합쇼체 + 고객사 맞춤 톤
   - Domain Context: 비즈니스 도메인 설명

2. `glossary/{client-name}.md` 생성
   - Korean | English | Notes 테이블
   - 수집된 도메인 용어 매핑

### Step 3: Notion DB에 프로젝트 옵션 추가
1. 프로젝트 문서 DB (collection://58f9b49c-dd24-4ae5-a827-b954072c4b8b)의 "프로젝트" SELECT 컬럼에 새 프로젝트명 옵션 추가
2. 커뮤니케이션 DB (collection://f3ea2e0c-f3d3-40a5-8dd5-364723c2f0fb)의 "프로젝트" SELECT 컬럼에 새 프로젝트명 옵션 추가
3. 태스크 DB (collection://6406d6c7-99c8-4465-880a-40c95b94eafc)의 "클라이언트" SELECT 컬럼에 새 클라이언트명 옵션 추가
4. 필요 시 각 DB의 "클라이언트" SELECT 컬럼에도 옵션 추가

**주의:** 기존 옵션을 유지하면서 새 옵션만 추가할 것. ALTER COLUMN 시 기존 옵션도 모두 포함해야 함. **3개 DB 모두** 빠짐없이 업데이트할 것.

### Step 4: PM Workspace에 프로젝트 토글 + 필터 뷰 추가
PM Workspace (32c3aae9a8948001bf49fba5b9c4c34a) 페이지의 "프로젝트별" 섹션에:

1. **토글 추가**: `### {project-name} {toggle="true"}` 안에:
   - `#### 문서` + 링크드 뷰 (data-source-url="collection://58f9b49c-dd24-4ae5-a827-b954072c4b8b")
   - `#### 커뮤니케이션` + 링크드 뷰 (data-source-url="collection://f3ea2e0c-f3d3-40a5-8dd5-364723c2f0fb")

2. **현재 PM workspace를 fetch**하여 새로 생성된 링크드 뷰의 database_id를 확인

3. **기본 뷰(첫 번째 탭)를 update-view로 수정** — 새 뷰를 추가로 만들지 말 것!
   - 각 링크드 뷰의 첫 번째 뷰(이름 없는 기본 뷰)를 fetch로 view ID 확인
   - update-view로 아래 설정 적용:

   프로젝트 문서 뷰:
   - name: "{project-name}"
   - configure: `FILTER "프로젝트" = "{project-name}"; SORT BY "작성일" DESC; SHOW "문서명", "단계", "상태", "언어", "유형", "작성일", "전달일", "클라이언트", "프로젝트"`

   커뮤니케이션 뷰:
   - name: "{project-name}"
   - configure: `FILTER "프로젝트" = "{project-name}"; SORT BY "작성일" DESC; SHOW "제목", "방향", "상태", "유형", "작성일", "클라이언트", "프로젝트"`

**중요:** 뷰는 링크드 뷰당 딱 1개만. create-view 사용하지 말고 기본 뷰를 update-view로 수정할 것.

### Step 5: 완료 보고
생성된 파일 목록과 Notion 구조 변경 사항을 사용자에게 보고합니다.
