
//Javascript
var emailBox = document.querySelector('.id-outbox');
var emailInputBox = document.querySelector('#email');
emailInputBox.addEventListener('keyup', function(){
    if(emailInputBox.value !== ''){
        //빈 값이 아닌 경우
        emailBox.classList.add('existence');   
    }else{
        //빈 값인 경우
        emailBox.classList.remove('existence');   
    }
});

var PWBox = document.querySelector('.pw-outbox');
var PWInputBox = document.querySelector('#password');
PWInputBox.addEventListener('keyup', function(){
    if(PWInputBox.value !== ''){
        //빈 값이 아닌 경우
        PWBox.classList.add('existence');   
    }else{
        //빈 값인 경우
        PWBox.classList.remove('existence');   
    }
});
