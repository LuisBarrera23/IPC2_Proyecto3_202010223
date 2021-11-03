function cargarArchivo() {
    var datos = document.getElementById('archivoxml').files[0];
    console.log(datos);

    var scannerxml = new FileReader();
    scannerxml.readAsText(datos);
    console.log(scannerxml.result);

    scannerxml.onload = function () {
        //console.log(scannerxml.result);
        contenido = scannerxml.result
        // ahora imprimimos en el textarea de entrada
        document.getElementById('entradaxml').value = contenido
    };

}

function enviararchivo() {
    texto=document.getElementById('entradaxml').value
    console.log(texto)
    var objeto = {
        'archivo': texto
    }
    console.log(objeto)


    fetch('http://localhost:5000/registrar', {
        method: 'POST',
        body: JSON.stringify(objeto),
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        }
    })
        .then(res => res.json())
        .catch(err => {
            console.error('Error:', err)
            alert("Ocurrio un error, ver la consola")
        })
        .then(response => {
            console.log(response.Mensaje)
        })
};
