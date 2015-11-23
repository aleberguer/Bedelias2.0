$(document).ready(function(){

  var successCallback = function(response){
    console.info('STATUS 200 ok');
    console.info(response);

    window.location.href = './home.html';
  }

  $('#signup-button-submit').click(function(){

    if($('#password').val() == $('#password2').val()){

      var parameters = {};
      parameters.email    = $('#email').val();
      parameters.fullname = $('#fullname').val();
      parameters.username = $('#username').val();
      parameters.password = $('#password').val();

    Requests.signup(parameters, successCallback, function(error){
      console.log(error);
    });

    } else {

      Materialize.toast('Las contrase&ntilde;as no coinciden', 4000);

    }

  });

});
