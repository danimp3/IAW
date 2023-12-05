from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación


@app.route('/registro')
def registro():
    return render_template('registro.html')


@app.route('/users', methods=['POST'])
def registrarse():
    
    usuario = request.form['usuario']
    mail = request.form['email']
    contraseña = request.form['password']
    conf_pass = request.form['conf_pass']
    try:  
        if contraseña == conf_pass:
            cursor = db.database.cursor()
            sql = "INSERT INTO users (id, email, password) VALUES (%s, %s, %s)"
            data = (usuario, mail, contraseña)
            cursor.execute(sql, data)
            db.database.commit()
            return redirect(url_for('login'))
        else:
            return render_template('registro.html', error="Contraseña incorrecta")
    except:
            return render_template('registro.html', error="El usuario ya existe")

@app.route('/main')
def home():
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM pilotos")
        myresult = cursor.fetchall()
        #Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        return render_template('main.html', data=insertObject)


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        usu = request.form['usuario']
        password = request.form ['password']
        
        if usu and password:
            cursor = db.database.cursor()
            sql = "SELECT * FROM users WHERE id = %s and password = %s"
            data = (usu,password)
            cursor.execute(sql,data)
            myresult = cursor.fetchall()
           
            if len(myresult) == 1:
            
                return redirect(url_for('home'))
            else:
                return render_template('index.html', error="Usuario o contraseña incorrectos")
            
            

#Ruta para guardar usuarios en la bdd
@app.route('/pilotos', methods=['POST'])
def addpilotos():
    nombre = request.form['nombre']
    edad = request.form['edad']
    numPiloto = request.form['numPiloto']
    escuderia = request.form['escuderia']
    victorias = request.form['victorias']
    podios = request.form['podios']
    puntos = request.form['puntos']
    
    
    
    if nombre and edad and numPiloto and escuderia and victorias and podios and puntos:
        cursor = db.database.cursor()
        sql = "INSERT INTO pilotos (nombre, edad, numPiloto, escuderia, victorias, podios, puntos) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (nombre, edad, numPiloto, escuderia, victorias, podios, puntos)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:nombre>')
def delete(nombre):
    cursor = db.database.cursor()
    sql = "DELETE FROM pilotos WHERE nombre=%s"
    data = (nombre,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:nombre>', methods=['POST'])
def edit(nombre):
    nombre = request.form['nombre']
    edad = request.form['edad']
    numPiloto = request.form['numPiloto']
    escuderia = request.form['escuderia']
    victorias = request.form['victorias']
    podios = request.form['podios']
    puntos = request.form['puntos']

    if nombre and edad and numPiloto and escuderia and victorias and podios and puntos:
        cursor = db.database.cursor()
        sql = "UPDATE pilotos SET edad = %s, numPiloto = %s, escuderia = %s, victorias = %s, podios = %s, puntos = %s WHERE nombre = %s"
        data = (edad, numPiloto, escuderia, victorias , podios, puntos, nombre)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)