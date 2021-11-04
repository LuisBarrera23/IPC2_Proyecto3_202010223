function cargarArchivo() {
    var datos = document.getElementById('archivoxml').files[0];

    var scannerxml = new FileReader();
    scannerxml.readAsText(datos);

    scannerxml.onload = function () {
        //console.log(scannerxml.result);
        contenido = scannerxml.result
        // ahora imprimimos en el textarea de entrada
        document.getElementById('entradaxml').value = contenido
    };

}

function enviararchivo() {
    texto=document.getElementById('entradaxml').value
    var objeto = {
        'archivo': texto
    }


    fetch('http://localhost:5000/procesar', {
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
            alert(response.Mensaje)
        })
};


function reset() {
    document.getElementById('entradaxml').value=""
    document.getElementById('salidaxml').value=""
    objeto=[]
    fetch(`http://localhost:5000/reset`, {
        method: 'GET',
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
            alert(response.Mensaje)
            

    })
    
};


function Consultar() {
    document.getElementById('salidaxml').value=""
    objeto=[]
    fetch(`http://localhost:5000/consultar`, {
        method: 'GET',
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
            document.getElementById('salidaxml').value=response.salida
            

    })
    
};
