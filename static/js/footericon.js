
//http://www.facebook.com/sharer.php?u={페이지 제목}&t={페이지링크}
//http://twitter.com/intent/tweet?text={페이지 제목}&url={페이지링크}
//https://share.naver.com/web/shareView.nhn?url={페이지링크}&title={페이지 제목}
//https://plus.google.com/share?url={페이지링크}&t={페이지 제목}
$(".facebook").click(function(e){
e.preventDefault();
window.open('https://www.facebook.com/sharer/sharer.php?u=' +encodeURIComponent(document.URL)+'&t='+encodeURIComponent(document.title), 'facebooksharedialog', 'menubar=no, toolbar=no, resizable=yes, scrollbars=yes, height=300, width=600'); 
});
$(".twitter").click(function(e){
e.preventDefault();
window.open('https://twitter.com/intent/tweet?text=[%EA%B3%B5%EC%9C%A0]%20' +encodeURIComponent(document.URL)+'%20-%20'+encodeURIComponent(document.title), 'twittersharedialog', 'menubar=no, toolbar=no, resizable=yes, scrollbars=yes, height=300, width=600');
});


