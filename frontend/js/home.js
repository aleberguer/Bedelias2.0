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
  { title: "Examen?" },
  { title: "Creditos" },
  { title: "Eliminar" }
];

$(document).ready(function() {

  Requests.getFaculties("", function(response){
    console.log("llegaron ya las facultades ", response);
  });

  var $otherCoursesTable = $('#other-courses').DataTable({
    data: otherCourses,
    columns: columns
  });

  $('#my-courses').DataTable({
    data: myCourses,
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
