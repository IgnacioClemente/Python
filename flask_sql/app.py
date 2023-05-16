from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aerolineas'

mysql = MySQL(app)

@app.route('/')
def index():
    print('Hola mundo')
    return render_template('index.html')

@app.route('/agregarVuelos',methods = ['POST'])
def registrar():
    if request.methods == 'POST':
        numero = request.form['numero']
        fecha = request.form['fecha']
        hora = request.form['hora']
        ciudad = request.form['ciudad']
        personal = request.form['personal']
        patente = request.form['patente']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO VUELOS (nro,fecha,hora,ciudad,personal,patente)VALUES(%s, %s, %s, %s, %s, %s)",(numero,fecha,hora,ciudad,personal,patente))
        mysql.connection.commit()
        print(numero,ciudad,patente)
        return 'registrado'

if __name__ == '__main__':
    app.run(port=3000, debug=True)