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
	var url = '/usuario/' + parameters.userId + '/cursos'; 
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.otrosCursos = function(parameters, successCallback, errorCallback){
	var url = '/usuario/' + parameters.userId + '/otros_cursos'; 
	Requests.ajax(url, 'GET', successCallback, errorCallback);
};

Requests.getAllCourses = function(parameters, successCallback, errorCallback){
	Requests.ajax('/getAllCourses', 'GET', successCallback, errorCallback, parameters);
};

Requests.getDoableCourses = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/getDoableCourses', 'GET', successCallback, errorCallback, parameters);
};

Requests.getFaculties = function(parameters, successCallback, errorCallback){
	Requests.ajax('/facultades', 'GET', successCallback, errorCallback, parameters);
};
// +--------------+
// | POST methods |
// +--------------+

Requests.signup = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/create', 'POST', successCallback, errorCallback, parameters);
};

Requests.addCourse = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/addCourse', 'POST', successCallback, errorCallback, parameters);
};

// +-------------+
// | PUT methods |
// +-------------+

Requests.updateProfile = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/update', 'PUT', successCallback, errorCallback, parameters);
};

// +----------------+
// | DELETE methods |
// +----------------+

Requests.removeCourse = function(parameters, successCallback, errorCallback){
	Requests.ajax('/user/removeCourse', 'DELETE', successCallback, errorCallback, parameters);
};

// +----------------+
// | DELETE methods |
// +----------------+

Requests.ajax = function(relativePath, type, successCallback, errorCallback, parameters){

	if(!errorCallback){
		errorCallback = Requests.defaultErrorCallback;
	}

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
};
