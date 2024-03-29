<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <div id="padre">
        <input type="text" id="txt1" name="txt1">
        <input type="text" id="txt2" name="txt2">
        <input type="text" id="txt3" name="txt3">
    </div>
    <script>
        function test () {
            let section = document.getElementById("padre");
            let colention = section.querySelectorAll("input[type=text]")
            colention.forEach(element => {
                if(element.value.length == 0){
                    element.style.backgroundColor="red";
                }
                
            });
        }



var miDiv = document.getElementById("miDiv"); // Reemplaza "miDiv" con el ID de tu div
var elementos = miDiv.querySelectorAll("input, select");

elementos.forEach(function(elemento) {
    if (elemento.hasAttribute("required")) {
        if (elemento.tagName.toLowerCase() === "input") {
            if (elemento.type === "text") {
                console.log("Es un input de texto requerido.");
                // Realiza acciones específicas para input de texto requerido
            } else if (elemento.type === "number") {
                console.log("Es un input de número requerido.");
                // Realiza acciones específicas para input de número requerido
            } else if (elemento.type === "date") {
                console.log("Es un input de fecha requerido.");
                // Realiza acciones específicas para input de fecha requerido
            } else if (elemento.type === "radio") {
                console.log("Es un radio button requerido.");
                // Realiza acciones específicas para radio button requerido
            }
        } else if (elemento.tagName.toLowerCase() === "select") {
            console.log("Es un elemento select requerido.");
            // Realiza acciones específicas para elementos select requeridos
        }
    }
});


//esto funciona
$(document).ready(function () {
          $('#myTable').DataTable({
            "ajax":{
                "url":"@Url.Action("GetDataJson", "Home")",
                "type":"GET",
                "datatype":"json"
            },
            "columns":[
                {"data":"userID"},
                {"data":"nombreUsuario"},
                {"data":"contrasenaHash"},
                {"data":"email"},
                {"data":"fechaRegistro"},
                { 
                    "data": "userID", "width":"50px", "render": function (data) {
                        return '<button type="button" id="'+data+'" class="btn btn-primary btnEdit">Algo</button>'
                    }
                }
            ]
          });

          $(document).on("click", ".btnEdit", function () {
            var id = $(this).attr("id");

            alert(id);
          });

      });

//esto obtiene la row como objeto
$('#myTable').DataTable({
    "ajax":{
        "url":"@Url.Action("GetDataJson", "Home")",
        "type":"GET",
        "datatype":"json"
    },
    "columns":[
        {"data":"userID"},
        {"data":"nombreUsuario"},
        {"data":"contrasenaHash"},
        {"data":"email"},
        {"data":"fechaRegistro"},
        { 'data': null, title: 'Action', "render": function (data, type, row, meta) { return '<div class="btn-group"> <button type="button" class="btn btn-primary" >Memo</button></div>' } }

    ]
});

//function to write actual data of a table row
$('#myTable tbody').on('click', 'tr', function () {
    var tr = $(this).closest('tr');
    var data = $('#myTable').DataTable().row(tr).data();
    console.log(data);
});

    </script>
</body>
</html>
