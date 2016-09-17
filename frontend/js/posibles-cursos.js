$(document).ready(function(){
    $('.button-collapse').sideNav();
    
    var user = JSON.parse(localStorage.getItem('user')) || { id: 1, user: { username: "ruso", first_name: "Diego", last_name: "Perez", email: "diego@diego.com"} };
    $('#user-name').text('Hola, ' + user.user.first_name);

    var parameters = {};
  	parameters.usuarioId = user.id;

  	var columns = [
	  { title: "Codigo" },
	  { title: "Nombre" },
	  { title: "Creditos" },
	  { title: "Validez" }
	];

	var tablaMisCursos = [];

    Requests.posiblesCursos(parameters, function(response){
    	if (response.length) {
    		cursosPosibles = [];

		    response.forEach(function(item) {

		        cursosPosibles.push([
		          item.codigo,
		          item.nombre,
		          item.creditos,
		          item.validez
		        ]);

		    });

		    tablaMisCursos = $('#results').DataTable({
		        data: cursosPosibles,
		        columns: columns,
		        columnDefs: [
		            {
		                "searchable": true
		            }
		        ]
		      });


    	}
    });
    
});