# Test Dataset — FreshMart (프레시마트)

테스트 완료 후 삭제 예정

---

## 1. Client Info (for /new-project)
- 고객사명: FreshMart (프레시마트)
- 프로젝트명: FreshMart
- 설명: 신선식품 새벽배송 스타트업의 모바일 앱 리뉴얼. 기존 앱의 주문/배송/회원 시스템 전면 개편.
- 담당자: 박지현 대리
- 커뮤니케이션 스타일: 꼼꼼하고 질문이 많으심. 답변은 빠른 편. IT 스타트업 출신이라 기술 용어 어느 정도 이해하시지만 개발 깊이는 모르심. 가끔 경쟁사 사례를 언급하시며 비교 요청하심.
- 도메인 용어:
  - 새벽배송 = dawn delivery
  - 컷오프 타임 = cutoff time (주문 마감 시간)
  - 콜드체인 = cold chain (저온 유통)
  - 픽업존 = pickup zone (무인 수령 장소)
  - 정기구독 = subscription order
  - 장바구니 = cart
  - 적립금 = reward points

---

## 2. Mock SRS (Korean, for /srs-translate)

### 프레시마트 앱 리뉴얼 기획서 (v1.0)

#### 1. 프로젝트 개요
프레시마트는 수도권 새벽배송 신선식품 스타트업입니다. 현재 웹 기반 주문 시스템을 운영 중이며, 모바일 앱으로 전환하면서 전체 시스템을 리뉴얼합니다.

#### 2. 핵심 기능

##### 2.1 주문 시스템
- 상품 검색 및 카테고리 브라우징
- 장바구니 관리 (수량 변경, 삭제, 임시저장)
- 결제: 카드, 간편결제(카카오페이, 네이버페이), 적립금 사용
- 컷오프 타임: 밤 11시까지 주문 시 익일 새벽 도착
- 정기구독: 주 1회/2회/매일 선택 가능

##### 2.2 배송 추적
- 실시간 배송 상태 확인 (준비중 → 배송출발 → 배송중 → 배송완료)
- 배송기사 위치 표시
- 배송 완료 사진 자동 촬영 및 전송
- 픽업존 배송 시 QR코드 수령 확인

##### 2.3 회원 시스템
- 소셜 로그인 (카카오, 네이버, 애플)
- 회원 등급: 일반 → 실버 → 골드 → VIP
- 등급 기준은 월간 구매 금액 (기준 금액은 아직 미정)
- 등급별 혜택: 배송비 할인, 적립금 비율 차등, 전용 쿠폰
- 포인트 적립 및 사용

##### 2.4 관리자 페이지
- 상품 등록/수정/삭제
- 주문 관리 및 배송 배정
- 매출 대시보드
- 쿠폰/프로모션 관리

#### 3. 기술 요구사항
- React Native 기반 크로스플랫폼 앱
- 백엔드는 클라우드 기반으로 해주세요
- 푸시 알림 필수
- 결제 PG 연동

#### 4. 일정
- 되도록 빨리 해주세요. 3개월 안에 가능할까요?

---

## 3. Mock Client Request (Korean, for /to-spec)

박지현 대리 카톡:
"안녕하세요~ 추가 요청 사항이 있어서요.
배송 추적 화면에서 배송기사한테 직접 전화할 수 있는 버튼 넣어주세요.
그리고 배송 예정 시간도 표시해주면 좋겠어요. 다른 앱들 보니까 다 있더라고요.
아 그리고 배송 완료되면 리뷰 남길 수 있게 해주세요. 별점이랑 사진 첨부 가능하게요.
사진은 최대 3장까지만 하면 될 것 같아요."

---

## 4. Mock Dev Question (English, for /client-chat question mode)

From dev (Minh):
"For the subscription order feature — should users be able to pause their subscription temporarily (like for vacation), or only cancel and re-subscribe? Also, if they change their delivery day mid-cycle, does it take effect immediately or from next cycle? And one more thing — for the cutoff time, should it be fixed at 11 PM or configurable per region?"

---

## 5. Mock Dev Update (English, for /client-chat update mode)

From dev (Minh):
"Weekly sync: Done — social login integration complete (Kakao, Naver, Apple), deployed to staging. Cart management API finished, frontend 90%. In progress — payment gateway integration with KG Inicis, ETA Friday. Product catalog search with Elasticsearch, about 60%. Blocked — membership tier thresholds not defined yet, can't implement upgrade logic. Also need design confirmation on the delivery tracking map UI. Next up — push notification service setup, subscription order flow."

---

## 6. Mock Client Request for Dev (Korean, for /dev-chat)

박지현 대리 카톡:
"배송 완료 사진이 흐릿하게 나온다는 고객 컴플레인이 있었어요. 사진 품질을 좀 올릴 수 있나요? 그리고 야간 배송일 때 플래시가 안 터져서 아예 안 보이는 경우도 있대요."

PM context: 사진 용량 이슈가 있을 수 있으니 개발팀한테 확인해보자. 플래시는 앱에서 제어 가능한 건지도 물어봐야 함.

---

## 7. Mock Weekly Update (for /weekly-report)

- 소셜 로그인 완료 (카카오, 네이버, 애플)
- 장바구니 API 완료, 프론트 90%
- 결제 연동(KG이니시스) 진행 중, 금요일 예상
- 상품 검색(Elasticsearch) 60%
- 회원 등급 기준 미정 — 클라이언트 확인 필요
- 배송 추적 지도 UI 디자인 확인 대기
- 다음 주: 푸시 알림, 정기구독 플로우
