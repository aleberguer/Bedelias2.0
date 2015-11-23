var otherCourses = [
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1234", "Calculo 2", "Si", "16", "2009/01/12"]
];

var myCourses = [
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1022", "Webir", "Si", "10", "2011/04/25"],
    [ "1120", "Algebra lineal 1", "No", "9", "2011/07/25"],
    [ "1234", "Calculo 2", "Si", "16", "2009/01/12"]
];

var columns = [
  { title: "#" },
  { title: "Curso" },
  { title: "Tipo" },
  { title: "Creditos" },
  { title: "Eliminar" }
];

$(document).ready(function() {

  var user = localStorage.getItem('user') || { userId: 1};

  Requests.misCursos(user, function(response){
    
    alert("mis cursos success");
    console.log("cursos", response);

    var myCourses = [];
    var data = JSON.parse(response);

    if (data.results.length) {
      data.results.forEach(function(item) {
        console.log("-----");
        console.info(item.curso);
        console.log("-----");

        // TODO: add checkbox
        var salvado = (item.tipo === 'curso_aprobado') ? 'Curso Aprobado' : 'Examen Salvado';

        myCourses.push([
          item.curso.codigo, 
          item.curso.nombre, 
          salvado, 
          item.curso.creditos, 
          "Hola"
        ]);
        
      });

      $('#my-courses').DataTable({
        data: myCourses,
        columns: columns
      });

    }

  });

  var $otherCoursesTable = $('#other-courses').DataTable({
    data: otherCourses,
    columns: columns
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

  bindRowsClick();
  $otherCoursesTable.on('draw.dt', function() {

    bindRowsClick();

  });

});
