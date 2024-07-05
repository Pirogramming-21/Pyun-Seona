# 🍀 JAVASCRIPT 스톱워치 과제\_피로그래밍 21기 편선아 🍀

## 🍀 완성본\_img

<img width="519" alt="스크린샷 2024-07-05 오후 11 24 56" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/2e554a88-9fb9-4fc7-ab31-23c442cc168c">

## 🍀 디자인적 요소

- start, stop, reset 버튼 hover시 색상 변경 구현 (#ffffff->#f0f0f0)
- 아이콘은 강의 시 추천해주신 remixicon의 아이콘 사용(link 걸어 사용)
- background color는 최대한 비슷한 #BFC6BF로 사용

## ☑️ 기능구현 1: 스톱워치

<img width="472" alt="스크린샷 2024-07-05 오후 11 28 02" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/8bed6b5c-4491-42ad-9a2c-bb6f2e9aebcc">

- 3가지 섹션(minutes, seconds, tenMillis)으로 나누어 구현.

### 🕰️ start 버튼

- operateTimer()라는 함수를 만들고, setInterval의 매개변수 자리에 넣어 10밀리초마다 시간이 증가하며, 이를 통해 밀리초, 초, 분 단위로 시간을 측정할 수 있게 만들었다.

### 🕰️ stop 버튼

- 클릭하면 스톱워치가 멈추고, 현재 시간을 유지하면서(초기화하지 않음) 구간 기록에 사용할 recordLap() 함수를 넣었다.

### 🕰️ reset 버튼

- 시간은 00:00:00으로 초기화되고, 모든 구간 기록도 삭제된다.

## ☑️ 기능구현 2: 기록추가

<img width="553" alt="스크린샷 2024-07-06 오전 12 08 08" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/f41a9f4e-71b0-43c3-8269-bc0a3f6d26e5">

- 스톱워치에 stop 버튼을 누를때마다 구간 기록을 저쟝할 수 있도록 Javascript에 recordLap() 함수를 구현하였고 기록된 구간 시간은 목록 맨 위에 추가된다.

## ☑️ 기능구현 3: 전체 삭제

<img width="541" alt="스크린샷 2024-07-06 오전 1 16 36" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/330ae95d-1834-4150-9c7a-f7fdf46d34dd">

<img width="482" alt="스크린샷 2024-07-06 오전 1 21 52" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/bcf1d0fc-1b8c-43f5-8323-79fe420af71d">

- '전체 선택' 후 휴지통 아이콘을 눌렀을 경우 전체 구간 기록이 삭제된다.

## ☑️ 기능구현 4: 선택 삭제

<img width="507" alt="스크린샷 2024-07-06 오전 12 16 31" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/e18907a2-428b-415c-bf36-70f5e6f32812">

<img width="468" alt="스크린샷 2024-07-06 오전 12 17 20" src="https://github.com/Pirogramming-21/Pyun-Seona/assets/139514905/e9373720-c0af-4d8d-b4d7-7f496bc677e9">

- 선택 전 아이콘(구간기록 시 기본 생성 아이콘), 선택 시 아이콘을 다르게 표기하였으며 사용한 아이콘은 remixicon에서 얻어왔다.

- 선택 후 삭제버튼을 누르면 해당 부분만 삭제가 된다. 이는 deleteIcon.onclick 시에 else문에 forEach문을 사용해 체크박스 아이콘의 부모요소, 즉 구간 기록을 나타내는 li 요소를 삭제하는 방식으로 구현하였다.

## ☑️ 추가 기능구현 5: 전체 선택

- 구간기록의 '전체 선택'부분 체크박스를 선택할 경우 구간 기록 전체가 선택되고, 사진 속 구간 기록의 1,2를 선택할 경우 구간기록의 '전체 선택'부분 체크박스가 체크표시로 바뀐다.

### 🍀 아쉬웠던 점.. 다짐..

시간상 추가 기능은 한 가지만 구현할 수 있어 아쉬웠고 스톱워치 과제 진행하면서 자바스크립트의 내장함수를 잘만 사용하면 구현하지 못할 이벤트가 없을 것 같다는 생각이 들었다.
추후 프로젝트 진행 시.. 이벤트 부분은 빠지는 부분 없이 다 구현하고싶다는 다짐.. 해봅니다..😇
