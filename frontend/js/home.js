var columns = [
  { title: "#" },
  { title: "Curso" },
  { title: "Tipo" },
  { title: "Creditos" },
  { title: "Acciones" }
];

var modalColumns = [
  { title: "id" },
  { title: "#" },
  { title: "Curso" },
  { title: "Creditos" },
  { title: "Acciones" }
];

function rowClick(evt){

  var $columns = $(evt.currentTarget).parent().parent().find('td');
  $confirmModal = $('#confirm-course-modal');
  $confirmModal.find('#title').text($($columns[2]).text());
  $confirmModal.find('#content').text();
  $confirmModal.find('#course-id').val($($columns[0]).text());

  $('#add-course-modal').closeModal();
  $('#confirm-course-modal').openModal();

}

$(document).ready(function() {

  var user = localStorage.getItem('user') || { id: 1 };

  var parameters = {};
  parameters.usuarioId = user.id;

  Requests.misCursos(parameters, function(response){
    
    var myCourses = [];

    if (response.results.length) {
      response.results.forEach(function(item) {

        var salvado = (item.tipo === 'curso_aprobado') ? 'Curso Aprobado' : 'Examen Salvado';

        myCourses.push([
          item.curso.codigo, 
          item.curso.nombre, 
          salvado, 
          item.curso.creditos,
          "<a href='#'> Editar </a> <a href='#'> Borrar </a>"
        ]);
        
      });

      $('#my-courses').DataTable({
        data: myCourses,
        columns: columns
      });

    }

  });

  Requests.otrosCursos(parameters, function(response){
    
    var otherCourses = [];

    if (response.length) {

      response.forEach(function(curso) {

        otherCourses.push([
          curso.id,
          curso.codigo, 
          curso.nombre, 
          curso.creditos,
          '<a onClick="rowClick(event)"> Agregar </a>'
        ]);
        
      });

      $('#other-courses').DataTable({
        data: otherCourses,
        columns: modalColumns,
        columnDefs: [
            {
                "targets": [ 0 ],
                "className": "hidden",
                "searchable": false
            }
        ]
      });

      $('#confirm-course-modal').find('th').first().addClass('hidden');

    }

  });
  
  // Add course button modal click
  $('#add-course-button').click(function(){
    $('#add-course-modal').openModal();
  });


  // Confirm course modal button click
  $('#confirm-course-btn').click(function(){

    var successCallback = function(response) {
      // TODO: agregar curso a la tabla..
      Materialize.toast('Curso agregado con exito!', 4000);
    };

    var parameters = {};
    parameters.usuarioId = user.id;
    parameters.cursoId = $('#course-id').val();
    parameters.tipo = $('#checkbox-examen:checked').length ? 'examen_aprobado' : 'curso_aprobado';

    Requests.agregarCurso(parameters, successCallback);

  });

  // Cancel course modal button click
  $('#cancel-course-btn').click(function(){
    $('#add-course-modal').openModal();
  });

});
