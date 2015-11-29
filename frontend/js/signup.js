var columns = [
  { title: "Codigo" },
  { title: "Nombre" }
];

/* {
  "id": 1058,
  "nombre": "73-0  LICENCIATURA EN COMPUTACION -LICENCIATURA EN COMPUTACION PLAN: 2012",
  "codigo": "73-0",
  "plan": null,
  "facultad": {
      "id": 17,
      "nombre": "INGENIERIA"
  }
} */

$(document).ready(function(){

var selected = [];
var facultad;
var selectedRow;
var carreraId;

/*-----------------------------------------
            CLICK ON UNIVERSITY
------------------------------------------*/

  $(".uni_logo").click(function(){
    var parameters = {};
    facultad = $(this).attr('data-id');
    parameters.id = facultad;
    // facultad = $(this).find('img').attr('alt').text();

    Requests.carreras(parameters, carrerasCallback, function(error) {
      console.log(error);
    });
  });

  var carrerasCallback = function(response){
    console.info('Carreras callback 200 OK');
    console.info(response);
    var carreras = [];

    if (response.length) {
      response.forEach(function(item) {

        carreras.push([
          item.codigo, 
          item.nombre
        ]);
      });

      $('#carreras').DataTable({
        data: carreras,
        columns: columns,
        "ajax": "scripts/ids-arrays.php",
        "rowCallback": function( row, data ) { }
      });
    };

    $('#carreras tbody').on('click', 'tr', function () {
      carreraId = $(this).find('td:first').text();
      var title = $(this).find('td:nth-child(2)').text();
      $('#collapsible-carrera').text("Seleccione una carrera (" + title + ")");
      $('#collapsible-form').trigger('click');
    });

    $('#collapsible-carrera').trigger('click');
  }

/*-----------------------------------------
          CARRERA ROW CLICKED
------------------------------------------*/



/*-----------------------------------------
          SIGN UP BUTTON CLICKED
------------------------------------------*/

  $('#signup-button-submit').click(function(){

    if($('#password').val() == $('#password2').val()){

      var carrera = {};
      carrera.facultad = facultad; 
      carrera.codigo = carreraId;

      var parameters = {};
      parameters.carrera = carrera;
      parameters.email    = $('#email').val();
      parameters.fullname = $('#fullname').val();
      parameters.username = $('#username').val();
      parameters.password = $('#password').val();

      alert(JSON.stringify(parameters));


    Requests.signup(parameters, successCallback, function(error){
      console.log(error);
    });
    } else {
      Materialize.toast('Las contrase&ntilde;as no coinciden', 4000);
    }
  });

  var successCallback = function(response){
    console.info('STATUS 200 ok');
    console.info(response);

    window.location.href = './home.html';
  }

});
