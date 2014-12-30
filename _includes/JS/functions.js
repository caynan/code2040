function get_token(email, github) {
    var url = 'http://challenge.code2040.org/api/register';
    var data = {email: email, github: github};
    data = JSON.stringify(data);
    var token;
    $.ajax({
        type: 'POST',
        url: url,
        async: false,
        data: data,
        dataType: 'json'
    })
    .done(function(data) {
        token = data.result;
    });

    return token;
}


function change_login_box(email, github, token) {
    $('#login-box').html(
        '<div id="login-box" class="col-sm-8 text-right">' +
            '<strong>Email: </strong>' + email + '<br />' +
            'Github: ' + github + '<br />' +
            'Token: ' + token +' <br />' +
        '</div>');
}

$(function () {
    // Get login info
    $('#login-btn').click(function () {
        var email = $('#email-form').val();
        var github = $('#github-form').val();
        var token = get_token(email, github);
        change_login_box(email, github, token);
    });




});
