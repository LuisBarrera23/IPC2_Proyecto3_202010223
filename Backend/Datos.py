class datos:
    def __init__(self,fecha,dia,mes,año,referencia,emisor,receptor,valor,iva,total):
        self.fecha=fecha
        self.dia=dia
        self.mes=mes
        self.año=año
        self.referencia=referencia
        self.emisor=emisor
        self.receptor=receptor
        self.valor=float(valor)
        self.iva=float(iva)
        self.total=float(total)