var columns = [
  { title: "#" },
  { title: "Curso" },
  { title: "Tipo" },
  { title: "Creditos" },
  { title: "Acciones" }
];

var modal_columns = [
  { title: "#" },
  { title: "Curso" },
  { title: "Creditos" }
];


$(document).ready(function() {

  var user = localStorage.getItem('user') || { userId: 1};

  Requests.misCursos(user, function(response){
    
    var myCourses = [];

    if (response.results.length) {
      response.results.forEach(function(item) {

        // TODO: add checkbox
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


  Requests.otrosCursos(user, function(response){
    
    var otherCourses = [];

    if (response.length) {
      response.forEach(function(curso) {

        otherCourses.push([
          curso.codigo, 
          curso.nombre, 
          curso.creditos
        ]);
        
      });
      var $otherCoursesTable = $('#other-courses').DataTable({
        data: otherCourses,
        columns: modal_columns
      });

      bindRowsClick();
      $otherCoursesTable.on('draw.dt', function() {
          bindRowsClick();
      });

    }

  });

  var bindRowsClick = function(){

      var $rows = $('#other-courses').find("[role='row']");
      $rows.off();
      $rows.click(function(){

        var $row = $(this).find('td');
        $confirmModal = $('#confirm-course-modal');
        $confirmModal.find('#title').text($($row[1]).text());
        $confirmModal.find('#content').text();
        $confirmModal.find('#course-id').val($($row[0]).text());

        $('#add-course-modal').closeModal();
        $('#confirm-course-modal').openModal();

      });

  };

  // Add course button modal click
  $('#add-course-button').click(function(){
    $('#add-course-modal').openModal();
  });


  // Confirm course modal button click
  $('#confirm-course-btn').click(function(){

    var successCallback = function(response){
      console.info(response);
      Materialize.toast('Curso agregado con exito!', 4000);
    }

    var parameters = {};
    parameters.username = $('#username').val();
    parameters.password = $('#password').val();

    return successCallback();

    Requests.addCourse(parameters, successCallback);

  });

  // Cancel course modal button click
  $('#cancel-course-btn').click(function(){
    $('#add-course-modal').openModal();
  });

});
