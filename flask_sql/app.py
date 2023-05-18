from flask import Flask, render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aerolineas'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listado')
def listado():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM VUELOS')
    respuesta = cursor.fetchall()
    return render_template('listado.html',vuelos = respuesta)

@app.route('/agregarVuelos',methods = ['POST'])
def registrar():
    if request.method == 'POST':
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
        return redirect(url_for('index'))
    
@app.route('/editarVuelos/<id>')  #el id es lo que le pase entre llaves en el html
def obtenerVuelo(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM VUELOS WHERE nro = %s' % (id)) #el numero que tengo en id lo igualo a nro
    respuesta = cursor.fetchall()
    return render_template('editar.html',vuelos = respuesta[0])

@app.route('/actualizarVuelo/<nro>',methods = ['POST'])#pasarle la variable como esta escrita en la base de datos
def actualizar(nro):
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        ciudad = request.form['ciudad']
        personal = request.form['personal']
        patente = request.form['patente']
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE VUELOS SET
        fecha = %s,
        hora = %s,
        ciudad = %s,
        personal = %s,
        patente = %s
        WHERE nro =%s""",(fecha,hora,ciudad,personal,patente,nro)) #traigo los valores que tengo en la base de datos
        mysql.connection.commit()
        print(nro,ciudad,patente)
        return redirect(url_for('index'))
    
@app.route('/eliminarVuelo/<string:nro>')  #el id es lo que le pase entre llaves en el html lo convierto en string
def eliminar(nro):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM VUELOS WHERE nro = {0}'.format(nro)) #el numero que tengo en id lo igualo a nro
    mysql.connection.commit()#lo elimino
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)