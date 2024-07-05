let minutes = 0;
let seconds = 0;
let tenMillis = 0;

const appendTens = document.getElementById("tenMillis");
const appendSeconds = document.getElementById('seconds');
const appendMinutes = document.getElementById('minutes');
const buttonStart = document.getElementById('btn__start');
const buttonStop = document.getElementById('btn__stop');
const buttonReset = document.getElementById('btn__reset');


let intervalid;

//1) start버튼 구현
buttonStart.onclick = function(){
    clearInterval(intervalid);
    intervalid = setInterval(operateTimer, 10)
}

//2) stop버튼 구현
buttonStop.onclick = function(){
    clearInterval(intervalid);
}

//3) reset버튼 구현
buttonReset.onclick = function(){
    clearInterval(intervalid);
    minutes = 0;
    seconds = 0;
    tenMillis = 0;

    appendTens.textContent = "00";
    appendMinutes.textContent = "00";
    appendSeconds.textContent = "00";
}
//10ms마다 시간에 대한 숫자가 증가하는 콜백함수
function operateTimer(){
    tenMillis++;
    appendTens.textContent = tenMillis > 9 ? tenMillis : '0' + tenMillis;
    
    //초 표시
    if(tenMillis > 99){
        seconds++;
        appendSeconds.textContent = seconds > 9 ? seconds : '0' + seconds;
        tenMillis = 0;
        appendTens = "00";
    }
    //분 표시
    if(seconds > 59){
        minutes++;
        appendMinutes.textContent = minutes > 9 ? minutes : '0' + minutes;
        appendSeconds.textContent = "00";
    }
}

//구간기록, 삭제 기능 추가

const lapList = document.getElementById('lap_list');
const deleteIcon = document.querySelector('.ri-file-reduce-fill');
let lapCount = 0;

// 시간을 2자리 숫자로 패딩하는 함수
function padTime(time) {
    return time.toString().padStart(2, '0');
}

// Stop 버튼에 구간 기록 기능 추가
buttonStop.onclick = function() {
    clearInterval(intervalid);
    recordLap();
}

// 구간 기록 함수
function recordLap() {
    const lapTime = `${padTime(minutes)}:${padTime(seconds)}:${padTime(tenMillis)}`;
    const lapItem = document.createElement('li');
    lapItem.className = 'lap-item';
    lapItem.innerHTML = `
        <i class="ri-checkbox-blank-circle-line lap-checkbox"></i>
        <span>${lapTime}</span>
    `;
    lapList.insertBefore(lapItem, lapList.firstChild);  // 새 기록을 목록 맨 위에 추가

    const checkbox = lapItem.querySelector('.lap-checkbox');
    checkbox.addEventListener('click', function() {
        this.classList.toggle('checked');
        this.classList.toggle('ri-checkbox-blank-circle-line');
        this.classList.toggle('ri-checkbox-circle-line');
        updateSelectAllCheckbox();
    });

    updateSelectAllCheckbox();
}

// 삭제 아이콘 클릭 이벤트
deleteIcon.onclick = function() {
    const checkedItems = lapList.querySelectorAll('.lap-checkbox.checked');
    
    if (checkedItems.length === 0) {
        // 선택된 항목이 없으면 모든 기록 삭제
        lapList.innerHTML = '';
    } else {
        // 선택된 항목만 삭제
        checkedItems.forEach(item => {
            lapList.removeChild(item.parentNode);
        });
    }
    updateSelectAllCheckbox();
}


// Reset 버튼에 구간 기록 초기화 추가
buttonReset.onclick = function() {
    clearInterval(intervalid);
    minutes = 0;
    seconds = 0;
    tenMillis = 0;

    appendTens.textContent = "00";
    appendMinutes.textContent = "00";
    appendSeconds.textContent = "00";

    // 구간 기록 초기화 추가
    lapList.innerHTML = '';
    lapCount = 0;
}

// 전체 선택 기능 추가
const selectAllCheckbox = document.getElementById('selectAll');

selectAllCheckbox.addEventListener('change', function() {
    const checkboxes = lapList.querySelectorAll('.lap-checkbox');
    checkboxes.forEach(checkbox => {
        if (this.checked) {
            checkbox.classList.add('checked', 'ri-checkbox-circle-line');
            checkbox.classList.remove('ri-checkbox-blank-circle-line');
        } else {
            checkbox.classList.remove('checked', 'ri-checkbox-circle-line');
            checkbox.classList.add('ri-checkbox-blank-circle-line');
        }
    });
});

// 새로운 구간 기록이 추가될 때마다 전체 선택 체크박스 상태 업데이트
function updateSelectAllCheckbox() {
    const totalItems = lapList.querySelectorAll('.lap-checkbox').length;
    const checkedItems = lapList.querySelectorAll('.lap-checkbox.checked').length;
    selectAllCheckbox.checked = totalItems > 0 && totalItems === checkedItems;
}
