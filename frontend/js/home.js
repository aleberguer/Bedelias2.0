/*===========================================
  Declarations
===========================================*/
var misCursos = [];
var otrosCursos = [];
var tablaMisCursos = [];
var tablaOtroscursos = [];

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

var user = localStorage.getItem('user') || { id: 1, nombre: 'Diego Perez' };

/*===========================================
  Event handlers
===========================================*/
function rowClick(evt){

  var $columns = $(evt.currentTarget).parent().parent().find('td');
  $confirmModal = $('#confirm-course-modal');
  $confirmModal.find('#title').text($($columns[2]).text());
  $confirmModal.find('#content').text();
  $confirmModal.find('#course-id').val($($columns[0]).text());

  $('#add-course-modal').closeModal();
  $('#confirm-course-modal').openModal();

}

function borrarCurso(cursoId, cursoNombre) {

  var $deleteModal = $('#delete-course-modal');
  $deleteModal.openModal();
  $deleteModal.find('#title').text(cursoNombre);
  $deleteModal.find('#course-id').val(cursoId);

  $('#confirm-delete-btn').click(function() {

    var parameters = {};
    parameters.usuarioId = user.id;
    parameters.cursoId = $('#delete-course-modal #course-id').val();

    Requests.borrarCurso(parameters, function(response){
      cargarDatosUsuario(true);
      Materialize.toast('Se ha eliminado el curso correctamente.', 4000);
    });

  });

}

function editarCurso(cursoId, cursoNombre, cursoTipo) {

  var $editModal = $('#edit-course-modal');
  $editModal.openModal();
  $editModal.find('#title').text(cursoNombre);
  $editModal.find('#course-id').val(cursoId);

  if (cursoTipo === 'curso_aprobado') {
    $editModal.find('#checkbox-examen-edit').removeAttr('checked');
  } else {
    $editModal.find('#checkbox-examen-edit').attr('checked','false');
  }

  // $editModal.find('#confirm-edit-btn').click(function() {

  //  var parameters = {};
  //  parameters.usuarioId = user.id;
  //  parameters.cursoId = $('#edit-course-modal #course-id').val();
  //  parameters.tipo = $('#edit-course-modal #checkbox-examen:checked').length ? 'examen_aprobado' : 'curso_aprobado';

  //  Requests.editarCurso(parameters, function(response){
  //    Materialize.toast('Se ha editado el curso correctamente.', 4000);
  //    cargarDatosUsuario(true);
  //  });

  //});

}

function cargarDatosUsuario(reload) {

  var parameters = {};
  parameters.usuarioId = user.id;

  Requests.misCreditos(parameters, function(response){
    $('#cantidad-creditos').text(response);
  });

  Requests.misCursos(parameters, function(response){

    if (response.results.length) {

      misCursos = [];

      response.results.forEach(function(item) {

        var salvado = (item.tipo === 'curso_aprobado') ? 'Curso Aprobado' : 'Examen Salvado';
        var acciones = "<a onClick=\"editarCurso('" + item.curso.id + "','" + item.curso.nombre + "','" + item.tipo + "')\"> Editar </a> <a onClick=\"borrarCurso('" + item.curso.id + "','" + item.curso.nombre + "')\"> Borrar </a>";

        misCursos.push([
          item.curso.codigo,
          item.curso.nombre,
          salvado,
          item.curso.creditos,
          acciones
        ]);

      });

      if (reload) {
        tablaMisCursos.destroy();
      }

      tablaMisCursos = $('#my-courses').DataTable({
        data: misCursos,
        columns: columns,
        columnDefs: [
            {
                "targets": [ 4 ],
                "className": "acciones-mis-cursos",
                "searchable": false
            }
        ]
      });

    }

  });

  Requests.otrosCursos(parameters, function(response){

    if (response.length) {

      otrosCursos = [];

      response.forEach(function(curso) {

        otrosCursos.push([
          curso.id,
          curso.codigo,
          curso.nombre,
          curso.creditos,
          '<a href="#" onClick="rowClick(event)"> Agregar </a>'
        ]);

      });

      if (reload) {
        tablaOtroscursos.destroy();
      }

      tablaOtroscursos = $('#other-courses').DataTable({
        data: otrosCursos,
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

}

/*===========================================
  Document Ready
===========================================*/
$(document).ready(function() {

  cargarDatosUsuario();

  // Add course button modal click
  $('#add-course-button').click(function(){
    $('#add-course-modal').openModal();
  });

  // Confirm course modal button click
  $('#confirm-course-btn').click(function(){

    var successCallback = function(response) {
      Materialize.toast('Curso agregado con exito!', 4000);
      cargarDatosUsuario(true);
    };

    var parameters = {};
    parameters.usuarioId = user.id;
    parameters.cursoId = $('#course-id').val();
    parameters.tipo = $('#confirm-course-modal #checkbox-examen:checked').length ? 'examen_aprobado' : 'curso_aprobado';

    Requests.agregarCurso(parameters, successCallback);

  });

  // Cancel course modal button click
  $('#cancel-course-btn').click(function(){
    $('#add-course-modal').openModal();
  });

});
