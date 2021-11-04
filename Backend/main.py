from flask import Flask,jsonify,request
from flask_cors import CORS
from xml.dom import minidom
import datetime

from Autorizaciones import autorizacion
from Datos import datos

listado=[]
texto=""

app=Flask(__name__)
CORS(app)

def isNumero(C):
    if ((ord(C) >= 48 and ord(C) <= 57)):
        return True
    else:
        return False

def isEspacio(C):
    if (ord(C)==32 or ord(C)==9 or ord(C)==10):
        return True
    else:
        return False

def registrar(objeto):
    global listado
    f=objeto.fecha
    print(f)
    for l in listado:
        if l.fecha==objeto.fecha:
            l.comprobar(objeto)
            print("repetido")
            return
    
    nuevo=autorizacion()
    nuevo.comprobar(objeto)
    nuevo.fecha=objeto.fecha
    listado.append(nuevo)
    print("Autorizacion nueva")
    return

def generarXml():
    global listado,texto
    texto=""
    texto+="<LISTAAUTORIZACIONES>"
    for l in listado:
        texto+="\n\t<AUTORIZACION>"
        texto+="\n\t\t<FECHA>"+l.fecha+"</FECHA>"
        texto+="\n\t\t<FACTURASRECIBIDAS>"+str(l.cantidad)+"</FACTURASRECIBIDAS>"

        texto+="\n\t\t<ERRORES>"
        texto+="\n\t\t\t<NIT_EMISOR>"+str(l.errorEmisor)+"</NIT_EMISOR>"
        texto+="\n\t\t\t<NIT_RECEPTOR>"+str(l.errorReceptor)+"</NIT_RECEPTOR>"
        texto+="\n\t\t\t<IVA>"+str(l.errorIva)+"</IVA>"
        texto+="\n\t\t\t<TOTAL>"+str(l.errorTotal)+"</TOTAL>"
        texto+="\n\t\t\t<REFERENCIA_DUPLICADA>"+str(l.refDuplicada)+"</REFERENCIA_DUPLICADA>"
        texto+="\n\t\t</ERRORES>"

        texto+="\n\t\t<FACTURAS_CORRECTAS>"+str(len(l.Aprobaciones))+"</FACTURAS_CORRECTAS>"
        texto+="\n\t\t<CANTIDAD_EMISORES>"+str(len(l.lEmisores))+"</CANTIDAD_EMISORES>"
        texto+="\n\t\t<CANTIDAD_RECEPTORES>"+str(len(l.lReceptores))+"</CANTIDAD_RECEPTORES>"

        texto+="\n\t\t<LISTADO_AUTORIZACIONES>"
        aprobaciones=l.Aprobaciones
        for a in aprobaciones:
            texto+="\n\t\t\t<APROVACION>"
            texto+=f"\n\t\t\t\t<EMISOR ref=\"{a.referencia}\">"+str(a.emisor)+"</EMISOR>"
            texto+="\n\t\t\t\t<CODIGO_APROVACION>"+str(a.codigo)+"</CODIGO_APROVACION>"
            texto+="\n\t\t\t</APROVACION>"

        texto+="\n\t\t\t</TOTAL_APROBACIONES>"+str(len(l.Aprobaciones))+"</TOTAL_APROBACIONES>"
        texto+="\n\t\t</LISTADO_AUTORIZACIONES>"


        texto+="\n\t</AUTORIZACION>"
    print(texto)
    f=open("autorizaciones.xml","w",encoding='UTF-8')
    f.write(texto)
    f.close()


@app.route('/procesar',methods=['POST'])
def procesar():
    global texto
    #print(request.json)

    archivo=str(request.json['archivo'])
    documento=minidom.parseString(archivo.upper())

    solicitidues=documento.getElementsByTagName("DTE")
    for s in solicitidues:
        tiempo=s.getElementsByTagName("TIEMPO")[0].firstChild.data
        #print(tiempo)

        arrayfecha=[]
        lexema=""
        fecha=""
        try:
            contador=0
            for c in tiempo:
                if isNumero(c):
                    if contador==3:
                        lexema+=c
                        arrayfecha.append(int(lexema))
                        lexema=""
                        contador=0
                        break
                    else:
                        lexema+=c
                        contador+=1
                elif ord(c)==47:
                    arrayfecha.append(int(lexema))
                    contador=0
                    lexema=""

            #print(str(arrayfecha[0])+"/"+str(arrayfecha[1])+"/"+str(arrayfecha[2]))
            f=datetime.datetime(arrayfecha[2],arrayfecha[1],arrayfecha[0])
            fecha=f.strftime("%d/%m/%Y")
            dia=arrayfecha[0]
            mes=arrayfecha[1]
            año=arrayfecha[2]



        except:
            print("error")
            continue



        referencia=s.getElementsByTagName("REFERENCIA")[0].firstChild.data
        #print(referencia)
        nitemisor=s.getElementsByTagName("NIT_EMISOR")[0].firstChild.data
        #print(nitemisor)
        nitreceptor=s.getElementsByTagName("NIT_RECEPTOR")[0].firstChild.data
        #print(nitreceptor)
        valor=s.getElementsByTagName("VALOR")[0].firstChild.data
        #print(valor)
        iva=s.getElementsByTagName("IVA")[0].firstChild.data
        #print(iva)
        total=s.getElementsByTagName("TOTAL")[0].firstChild.data
        #print(total)
        objeto=datos(fecha,dia,mes,año,referencia.strip(),nitemisor.strip(),nitreceptor.strip(),valor.strip(),iva.strip(),total.strip())
        registrar(objeto)

    generarXml()

    return jsonify({'Mensaje':"Archivo leido","salida":texto})

@app.route('/reset',methods=['GET'])
def reset():
    global listado,texto
    listado=[]
    texto=""

    return jsonify({'Mensaje':"Datos borrados con exito"})


@app.route('/consultar',methods=['GET'])
def consultar():
    global texto
    return jsonify({'salida':texto})


if __name__=='__main__':
    app.run(debug=True,port=5000)