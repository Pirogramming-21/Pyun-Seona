// 2. 게임 초기화
let secretNumbers = [];

function initializeGame() {
    // a. 시도 가능 횟수를 설정합니다.
    let attempts = 10;

    // b. 중복되지 않는 3개의 랜덤한 숫자를 설정합니다.
    secretNumbers = [];
    while (secretNumbers.length < 3) {
        let randomNum = Math.floor(Math.random() * 10);
        if (!secretNumbers.includes(randomNum)) {
            secretNumbers.push(randomNum);
        }
    }

    // c. html의 input과 결과창의 내용을 비웁니다.
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
    document.querySelector('.result-display').innerHTML = '';
}

// 3. 숫자 확인
function check_numbers() {
    // submit-button에 onclick 이벤트로 연결되어 있는 check_numbers() 를 구현
    
    // 1. 입력되지 않은 input이 있다면 숫자를 확인하지 않고 input 창만 비웁니다.
    let input1 = document.getElementById('number1').value;
    let input2 = document.getElementById('number2').value;
    let input3 = document.getElementById('number3').value;


     // input에 값이 하나라도 없다면 입력 값 초기화
    if (!input1 || !input2 || !input3) {
        document.getElementById('number1').value = '';
        document.getElementById('number2').value = '';
        document.getElementById('number3').value = '';
        return;
    }

    // 2. 숫자 3개가 입력되었다면 결과를 확인합니다.
    let inputNumbers = [parseInt(input1), parseInt(input2), parseInt(input3)];
    
    // a. 입력된 숫자들과 정답을 비교하여 결과를 생성하는 로직 만들기
    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (inputNumbers[i] === secretNumbers[i]) {
            strikes++;
        } else if (secretNumbers.includes(inputNumbers[i])) {
            balls++;
        }
    }


    // b. 생성된 결과에 따라 html 업데이트하기
    let resultDisplay = document.querySelector('.result-display');
    let resultHtml = `
        <div class="check-result">
            <div class="left">${input1} ${input2} ${input3}</div>
            :
            <div class="right">
    `;

    if (strikes === 0 && balls === 0) {
        resultHtml += `<div class="out num-result">O</div>`;
    } else {
        if (strikes > 0) {
            resultHtml += `${strikes} <div class="strike num-result">S</div> `;
        }
        if (balls > 0) {
            resultHtml += `${balls} <div class="ball num-result">B</div>`;
        }
    }

    resultHtml += `
            </div>
        </div>
    `;

    resultDisplay.innerHTML = resultHtml + resultDisplay.innerHTML;

    // c. 게임이 끝났는지 체크하고 결과에 따라 이미지를 출력합니다. 게임이 끝나면 확인하기 버튼은 비활성화 합니다.
    let gameResultImg = document.getElementById('game-result-img');
    if (strikes === 3) {
        gameResultImg.src = 'success.png';
        document.querySelector('.submit-button').disabled = true;
    } else if (document.querySelectorAll('.check-result').length >= 9) {
        gameResultImg.src = 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }

    // 입력 값 초기화
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
}

// 게임 초기화 함수 호출
initializeGame();