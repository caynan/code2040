function get_token(n,t){var a="http://challenge.code2040.org/api/register",e={email:n,github:t};e=JSON.stringify(e);var i;return $.ajax({type:"POST",url:a,async:!1,data:e,dataType:"json"}).done(function(n){i=n.result}),i}$(function(){$("#login-btn").click(function(){var n=$("#email-form").val(),t=$("#github-form").val(),a=get_token(n,t);change_login_box(n,t,a)})});