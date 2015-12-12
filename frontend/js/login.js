$(document).ready(function(){

	var successCallback = function(response){

    localStorage.setItem('user', JSON.stringify(response));
    window.location.href = './home.html';

	}

	var errorCallback = function(response) {
		Materialize.toast('Usuario/password incorrectos.', 4000);
	}

	$('#login-button-submit').click(function(){

		var parameters = {};
		parameters.username = $('#username').val();
		parameters.password = $('#password').val();

		Requests.login(parameters, successCallback, errorCallback);

	});

});
