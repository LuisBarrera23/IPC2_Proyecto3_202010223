function cargarArchivo(){
    var datos=document.getElementById('archivoxml').files[0];
    console.log(datos);

    var scannerxml=new FileReader();
    scannerxml.readAsText(datos);
    console.log(scannerxml.result);

    scannerxml.onload=function(){
        //console.log(scannerxml.result);
        contenido=scannerxml.result
        // ahora imprimimos en el textarea de entrada
        document.getElementById('entradaxml').value=contenido
    };

    
}
