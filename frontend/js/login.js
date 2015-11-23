$(document).ready(function(){

	var successCallback = function(response){
		console.info('STATUS 200 ok');
		console.info(response);

		window.location.href = './home.html';
	}

	$('#login-button-submit').click(function(){

		var parameters = {};
		parameters.username = $('#username').val();
		parameters.password = $('#password').val();

		console.info(parameters);

		return successCallback();

		Requests.login(parameters, successCallback);

	});

});
