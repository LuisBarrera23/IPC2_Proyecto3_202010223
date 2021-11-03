from flask import Flask,jsonify,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/registrar',methods=['POST'])
def registrar():
    #print(request.json)

    archivo=str(request.json['archivo'])
    print(archivo)
    return jsonify({'Mensaje':"Archivo leido"})


if __name__=='__main__':
    app.run(debug=True,port=5000)