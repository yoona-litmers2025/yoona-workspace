# Client: Reference Korea (RCK)

## Overview
- **고객사명**: Reference Korea (RCK)
- **프로젝트명**: RCK
- **설명**: 레퍼런스 체크 플랫폼. 기업이 채용 후보자의 평판을 온라인/오프라인으로 조회하고, AI 요약 리포트를 받을 수 있는 서비스.
- **담당자**: 윤재혁 매니저
- **Tech Stack**: Bubble (no-code)

## Communication Style
- 일정에 굉장히 민감하심
- 개발을 거의 모르심 — 기술 용어 사용 자제, 비즈니스 언어로 변환 필수
- 온도 자체는 괜찮지만 약간의 불신이 항상 있음 — 신뢰 회복이 핵심
- 꼼꼼히 확인하려 하시고 실행력이 빠르신 것 같지만 현실적으로는 아님 — 약속 일정에 여유를 두고 잡아야 함
- 대면 미팅을 선호하심
- 사소한 버그에도 "기본 기능도 안 된다"고 인식할 수 있음 — 전달 전 반드시 내부 QA 필수

## Tone
- 기본: 해요체 (카톡/메시지)
- 공식 문서: 합쇼체
- 기술 설명 시: 비유나 일상 언어로 풀어서 전달
- 이슈 보고 시: 문제 + 대응방안을 반드시 함께 전달 (문제만 보고하면 불안감 증가)

## Domain Context
- **비즈니스 도메인**: 채용 레퍼런스 체크 (reference check)
- **주요 사용자 권한**: Admin, Company, Candidate, Reference Writer
- **주요 서비스 유형**:
  - 온라인 평판조회 (online reference check)
  - 오프라인 평판조회 (offline reference check)
  - 사전심사 조회 (pre-screening)
- **핵심 기능**: 질문지/설문지 CRUD (Questionnaire/Template), AI 요약 리포트, 결제(Payple), SMS 알림(NHN)
- **외부 연동**: NHN (SMS), Payple (결제), OpenAI (AI 요약)

## Current Status
- **프로젝트 단계**: 외부 QA 마무리 → 프로젝트 종료 → 잔금 처리 → 1개월 무상 유지보수
- **핵심 우선순위**: 금일 나온 QA 티켓까지 해결 후 외부 QA 종료
- **Payple/AI**: 일정 지연 가능성 고객사에 이미 고지됨
