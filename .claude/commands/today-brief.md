---
description: 아침 브리핑 — 오늘 할 일, blocker, 프로젝트 현황 요약
argument-hint: (인자 없이 실행)
allowed-tools: Read, Glob, Grep, mcp__notion__*, mcp__google-workspace__*
---

# Today Brief

## Arguments
사용자 입력: $ARGUMENTS

## Context
- 매일 아침 출근 후 첫 번째로 실행하는 브리핑 스킬
- PM이 "오늘 뭐해야하지?" 한마디로 전체 상황을 파악할 수 있게
- 여러 데이터 소스에서 오늘 관련 정보를 모아서 한 화면에 정리
- 터미널 출력만 — Notion 저장 없음

## Data Sources

1. **PM Action Hub DB** (collection://3a13db31-882c-4a6c-bddf-660e15ea9cdd)
   - 상태 = "오늘" → 오늘 처리할 액션
   - 상태 = "대기" → 확인/응답 대기 중인 항목
   - 상태 = "진행 중" + 오래된 항목 → 멈춘 것 감지
2. **Daily Scrum Log DB** (collection://eb2f7df2-0359-4c2c-85bb-6e12e3d73afc)
   - 어제자 로그에서 blocker 확인
3. **Google Calendar** (가능한 경우)
   - 오늘 미팅 목록

## Output Structure

```
☀️ {YYYY-MM-DD} ({요일}) — 오늘 브리핑

🔴 바로 처리할 것 (High 우선순위)
- [Koboom] 피드백 업데이트
- [RCK] timeline 정리

📋 오늘 할 일 (전체)
- [BaraeCNP] 문의내용 회신
- [Koboom] admin figma update
- ...

📅 오늘 미팅
- 14:00 [DSA] sync (내부)
- 16:00 [Koboom] 고객사 피드백 미팅 (외부)
(캘린더 연결 안 되어 있으면 이 섹션 생략)

⚠️ Blocker / 대기
- [Booktails] BE: 클라이언트 이미지 파일 대기 중
- [Koboom] 수수료 정책 고객 컨펌 대기

🔄 진행 중 (참고)
- [RCK] 질문지 안정화 — 진행 중
- [21gram] self QA — 진행 중
```

## Instructions

1. **PM Action Hub 조회**:
   - 상태 = "오늘" 인 항목 전체 가져오기
   - 상태 = "대기" 인 항목 전체 가져오기
   - 상태 = "진행 중" 인 항목 전체 가져오기
   - 우선순위 High 항목은 "바로 처리할 것"으로 분리

2. **Daily Scrum Log 조회**:
   - 어제 날짜 기준 로그에서 blocker 확인
   - blocker가 있으면 "Blocker / 대기" 섹션에 포함

3. **Google Calendar 조회** (연결되어 있는 경우):
   - 오늘 날짜 이벤트 목록
   - 시간순 정렬
   - 연결 안 되어 있으면 미팅 섹션 생략 (에러 표시 안 함)

4. **출력 구성**:
   - 🔴 바로 처리할 것: 상태=오늘 + 우선순위=High
   - 📋 오늘 할 일: 상태=오늘 전체 (High 포함)
   - 📅 오늘 미팅: Google Calendar 오늘 일정
   - ⚠️ Blocker / 대기: 상태=대기 + Daily Scrum blocker
   - 🔄 진행 중: 상태=진행 중 (참고용)

## Rules

- 각 섹션에 항목이 없으면 해당 섹션 생략
- 항목이 하나도 없으면 "오늘은 등록된 액션이 없습니다. /todo로 추가하거나 PM Action Hub를 확인하세요." 출력
- 프로젝트명은 [대괄호]로 표시
- 우선순위 High는 🔴 마커
- 간결하게 — bullet당 1줄
- 한국어 출력
- 인자 없이 실행 가능 (오늘 날짜 자동)
