// 화면 너비//
var windowWidth = $( window ).width();


let slideNext = document.querySelector(".slide-next");
let slidePrev = document.querySelector(".slide-prev");

let qnaBox = document.querySelector(".qna-showlist");
let card = document.querySelectorAll(".qna-showlist li");
let currentIndex = 0;
let cardCount = card.length;
let cardWidth = 340;
let cardMargin = 40;

makeClone();

function makeClone() {
    for (var i = 0; i < cardCount; i++) {
        var cloneCard = card[i].cloneNode(true);
        cloneCard.classList.add('clone');
        qnaBox.appendChild(cloneCard);
    }
    for (var i =cardCount -1; i>=0; i--) {
        var cloneCard = card[i].cloneNode(true);
        cloneCard.classList.add('clone');
        qnaBox.prepend(cloneCard);
    }
    updateWidth();
    setInitialPos();
    setTimeout(function(){
        qnaBox.classList.add('animated');
    },100)
    
}

function updateWidth() {
    var currentCards = document.querySelectorAll(".qna-showlist li");
    var newCardCount = currentCards.length;

    var newWidth = (cardWidth + cardMargin) * newCardCount - cardMargin + 'px';
    qnaBox.style.width = newWidth;
}

function setInitialPos() {
    var initialTranslateValue = -(cardWidth + cardMargin)*cardCount;
    qnaBox.style.transform = 'translateX(' + initialTranslateValue+'px)';

}

slideNext.addEventListener('click', function(){
    moveSlide(currentIndex + 1)
})

slidePrev.addEventListener('click', function(){
    moveSlide(currentIndex - 1)
})

function moveSlide(num) {
    qnaBox.style.left = -num * (cardWidth + cardMargin) + 'px';
    currentIndex = num;
    console.log(currentIndex, cardCount);
    if (currentIndex == cardCount || currentIndex == -cardCount) {
        setTimeout(function(){
            qnaBox.classList.remove('animated');
            qnaBox.style.left = '0px';
            currentIndex = 0;
        },500);
        setTimeout(function(){
            qnaBox.classList.add('animated');

        },600)

        
    }
}

// 이전 버전
// qnaBox.style.width = (cardWidth + cardMargin) * cardCount - cardMargin + 'px';

// function moveSlide1(num) {
//     qnaBox.style.left = (-num * 740 + 'px');
//     currentIndex = num;
// };


// slideNext.addEventListener('click', function() {
//     if (currentIndex < 2){
//         moveSlide1(currentIndex + 1);
//         console.log(currentIndex);
//     } else {
//         moveSlide1(0);
//     }
// })

// slidePrev.addEventListener('click', function() {
//     if (currentIndex > 0){
//         moveSlide1(currentIndex - 1);
//         console.log(currentIndex);
//     } else {
//         moveSlide1(2);
//     }
// })