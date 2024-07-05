# JAVASCRIPT 스톱워치 과제\_피로그래밍 21기 편선아

## 완성본\_img

<img width="519" alt="스크린샷 2024-07-05 오후 11 24 56" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/2e554a88-9fb9-4fc7-ab31-23c442cc168c">

## 디자인적 요소

- start, stop, reset 버튼 hover시 색상 변경 구현 (#ffffff->#f0f0f0)
- 아이콘은 강의 시 추천해주신 remixicon의 아이콘 사용(link 걸어 사용)
- background color는 최대한 비슷한 #BFC6BF로 사용

## 기능구현 1: 스톱워치

<img width="472" alt="스크린샷 2024-07-05 오후 11 28 02" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/8bed6b5c-4491-42ad-9a2c-bb6f2e9aebcc">

- 3가지 섹션(minutes, seconds, tenMillis)으로 나누어 구현.

### start 버튼

- operateTimer()라는 함수를 만들고, setInterval의 매개변수 자리에 넣어 10밀리초마다 시간이 증가하며, 이를 통해 밀리초, 초, 분 단위로 시간을 측정할 수 있게 만들었다.

### stop 버튼

- 클릭하면 스톱워치가 멈추고, 현재 시간을 유지하면서(초기화하지 않음) 구간 기록에 사용할 recordLap() 함수를 넣었다.

### reset 버튼

- 시간은 00:00:00으로 초기화되고, 모든 구간 기록도 삭제된다.

## 기능구현 2: 기록추가
