<!--로그아웃 알림, 로그아웃 -->
 function confirmLogout() {
        if( confirm("정말 로그아웃 하시겠습니까?") ) {
            location.href = "<c:url value ='/member/logout'/>";
        }
    }
<!--내가 쓴 글 -->
function showmyqna() {
	$ajax({
		type: "GET",
		url: "/myqna",
		data:{},
		success: function (response){
			let myqnas = response['all_myqnas']
			for(let i = 0; i < myqnas.lenght; i++) {
				let question = myqnas[i]['question']
				let answer = myqnas[i]['answer']
				
				let temp_html = `<div id="QnA" class="myqna">
					<div class="cardlist" href="">
						<p id="Question" class="question">Q.${question}
						<p id="Answer" class="answer">A.${answer}`
				$('#QnA').append(temp_html)
				}
			}
		})
	}

<!--다른사람이 쓴 글-->