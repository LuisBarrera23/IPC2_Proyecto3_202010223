from Aprobacion import aprobacion

class autorizacion:
    def __init__(self):
        self.fecha=""
        self.cantidad=0
        self.errorEmisor=0
        self.errorReceptor=0
        self.errorIva=0
        self.errorTotal=0
        self.refDuplicada=0
        self.correctas=0
        self.emisores=0
        self.receptores=0
        self.Aprobaciones=[]
        self.lEmisores=[]
        self.lReceptores=[]
        self.valores=[]
        self.Referencias=[]
        self.totales=[]
        self.correlativo=1

    def comprobar(self,objeto):
        self.cantidad+=1
        error=False
        self.fecha=objeto.fecha
        
        duplicado=False
        for i in self.Referencias:
            if i==objeto.referencia:
                error=True
                duplicado=True
                self.refDuplicada+=1
        
        if duplicado is False:
            self.Referencias.append(objeto.referencia)

        nit1=objeto.emisor
        try:
            aux=[]
            for n in nit1:
                aux.append(n)
            largo=len(nit1)
            #print(largo)
            fin=aux[largo-1]
            #print(fin)
            #print(aux)
            sumatoria=0
            for a in aux:
                if largo==1:
                    break
                #print(a)
                sumatoria+=int(a)*largo
                largo-=1
            resultado=11-(sumatoria%11)

            if resultado<10:
                esperado=str(resultado)
            elif resultado==11:
                esperado="0"
            elif resultado==10:
                esperado="k"
            print("se esperaba---")
            print(esperado)
            if esperado==fin:
                repetido=False
                for e in self.lEmisores:
                    if e == nit1:
                        repetido=True
                if repetido is False:
                    self.lEmisores.append(nit1)
                    self.emisores+=1
            else:
                #print("incorrecto")
                print(nit1)
                error=True
                self.errorEmisor+=1
        
        except:
            error=True
            self.errorEmisor+=1

        nit2=objeto.receptor
        try:
            aux=[]
            for n in nit2:
                aux.append(n)
            largo=len(nit2)
            #print(largo)
            fin=aux[largo-1]
            #print(fin)
            #print(aux)
            sumatoria=0
            for a in aux:
                if largo==1:
                    break
                #print(a)
                sumatoria+=int(a)*largo
                largo-=1
            resultado=11-(sumatoria%11)

            if resultado<10:
                esperado=str(resultado)
            elif resultado==11:
                esperado="0"
            elif resultado==10:
                esperado="k"

            #print(esperado)
            if esperado==fin:
                repetido=False
                for e in self.lReceptores:
                    if e == nit2:
                        repetido=True
                if repetido is False:
                    self.lReceptores.append(nit2)
                    self.receptores+=1
            else:
                #print("incorrecto")
                error=True
                self.errorReceptor+=1
        
        except:
            error=True
            self.errorReceptor+=1

        valor=objeto.valor
        iva=objeto.iva
        total=objeto.total

        calculoiva=valor*0.12
        if calculoiva==iva:
            print("IVA correcto")
        else:
            error=True
            self.errorIva+=1
        
        calculototal=(valor*0.12)+valor
        if calculototal==total:
            print("total correcto")
        else:
            error=True
            self.errorTotal+=1


        if error is False:
            self.valores.append(valor)
            self.totales.append(total)
            fijo=str(objeto.año)+str(objeto.mes)+str(objeto.dia)
            numero=self.correlativo

            largo=len(str(numero))
            relleno=""
            for i in range (8-largo):
                relleno+="0"

            correlativo=fijo+relleno+str(numero)
            #print(fijo+relleno+str(numero))
            self.correlativo+=1
            nueva=aprobacion(nit1,objeto.referencia,correlativo)
            self.Aprobaciones.append(nueva)

