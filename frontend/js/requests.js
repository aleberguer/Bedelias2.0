function Requests() {}

Requests.HOST_URL = 'http://0.0.0.0:8000/api';

// +-------------+
// | GET methods |
// +-------------+

Requests.login = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/login', 'GET', successCallback, errorCallback, parameters);
};

Requests.logout = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/logout', 'GET', successCallback, errorCallback, parameters);
};

Requests.misCursos = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/cursos';
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.misCreditos = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/creditos';
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.otrosCursos = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/otros_cursos';
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.otrosCursos = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/posibles_cursos';
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.carreras = function(parameters, successCallback, errorCallback){
	var url = '/facultades/' + parameters.id + '/carreras';
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

// +--------------+
// | POST methods |
// +--------------+

Requests.signup = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/create', 'POST', successCallback, errorCallback, parameters);
};

Requests.agregarCurso = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/agregar_curso/';
	Requests.ajax(url, 'POST', successCallback, errorCallback, parameters);
};

Requests.editarCurso = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/editar_curso/';
	Requests.ajax(url, 'POST', successCallback, errorCallback, parameters);
};

Requests.borrarCurso = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.usuarioId + '/borrar_curso/';
	Requests.ajax(url, 'POST', successCallback, errorCallback, parameters);
};

// +-------------+
// | PUT methods |
// +-------------+

Requests.updateProfile = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/update', 'PUT', successCallback, errorCallback, parameters);
};

// +-------------+
// | AUX methods |
// +-------------+

Requests.ajax = function(relativePath, type, successCallback, errorCallback, parameters){

	errorCallback = errorCallback || Requests.defaultErrorCallback;
	parameters = parameters || {};

	$.ajax({
		url: Requests.HOST_URL + relativePath,
		type: type,
		success: successCallback,
		error: errorCallback,
		dataType: 'json',
		data: JSON.stringify(parameters)
	});

};

Requests.defaultErrorCallback = function(result){
	console.error('+---------------+');
	console.error('| EXPLOTO (o.O) |');
	console.error('+---------------+');
	console.log(result);
};
