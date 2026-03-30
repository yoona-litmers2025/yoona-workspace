# Client: DSA

## Overview
- **고객사명**: DSA
- **프로젝트명**: DSA
- **설명**: 건설 기술지도 관리 SaaS 플랫폼. 기술지도 보고서 작성/검수, 차량 관리, 성과 관리, 손익 관리, 입찰/협력사 관리 등 건설 기술지도 업무 전반을 다루는 서비스. AI 보고서 평가, 법령 QnA 챗봇, 결제(토스페이먼츠) 연동 예정.
- **담당자**: (추후 업데이트)
- **우리 역할**: Figma Make + Supabase → Native FE + Supabase 마이그레이션 + Base44 제품 병합 + AI 기능 개발
- **현재 단계**: 기획/디자인 리뉴얼 (4월) → 개발 + 결제 연동 (5월) → AI 기능 도입 (6월)

## Communication Style
- (추후 업데이트)

## Tone
- 해요체 기본, 공식 문서는 합쇼체
- 노션 문서는 간결체 (도입/마무리만 합니다체)

## Domain Context
- **비즈니스 도메인**: 건설 기술지도 (Construction Technical Guidance)
- **핵심 서비스**: 기술지도 보고서 자동화 + AI 평가 + 법령 QnA 챗봇
- **주요 사용자 권한**:
  - 조직관리자 (Org Admin): 프로젝트/차량/기술지도/성과/조직/사업 관리 전체
  - 기술지도위원 (Technical Advisory): 기술지도 현황, 운행일지, 나의 성과, 시스템
- **주요 기능 영역**:
  - 프로젝트 관리: 프로젝트 목록/상세, 기술지도 현황 (보고서 작성/미리보기/편집)
  - 차량 관리: 차량 목록/상세, 운행일지 작성/리스트, 운행 리포트
  - 기술지도 관리: 계약현황, 손익관리
  - 성과 관리: 전체 성과 / 나의 성과
  - 조직 관리: 조직 정보, 사용자 관리
  - 사업 관리: 입찰 관리, 협력사 관리
  - 시스템: 프로필, 드라이브, 문서대장
- **기술 스택**: Figma Make (현재 FE) → Native FE로 마이그레이션 예정, Supabase (DB/Auth), Base44 (손익관리 모듈), 토스페이먼츠 (결제 예정)
- **AI 도입 계획**:
  - 보고서 자동 평가 (사진-내용 불일치, 위험요인 누락, 우수/양호/불량 판정)
  - 법령 기반 QnA 챗봇 (웹 채팅 UI, 근거 링크 포함)
  - 도면 PDF 분석, OCR 이미지 인식
  - 데이터: JSON/Markdown 기반 처리
- **SaaS 플랜 구조**: Free / Standard / Pro / Enterprise
- **과금**: 사용자 수 + 조직 단위, AI 사용량은 질문 횟수 기준
- **외부 시스템**: 인세프 (기존 기술지도 시스템), 홈택스 연동 없음

## Key References
- 도메인 URL: https://ggom.me
- Figma 디자인: https://www.figma.com/design/T0Uaxzt6jJGhw8aO2QvSGC/DSA
- Figma Make (개발): https://www.figma.com/make/EvLtdY91fSkMgfT7KQ3QZT/DSA-dev
- Base44 손익관리: https://performance-fleet-management-suit-c3c3fbf7.base44.app
- 테스트 계정:
  - 조직관리자: team0@test.co.kr / team123!@#
  - 기술지도위원: tech0@test.co.kr / tech123!@#
