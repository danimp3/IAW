from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hola():
    indice = ""
    try:
        if request.method == "POST":
            imc = 0
            altura = float(request.form.get("altura"))        
            peso = float(request.form.get("peso"))
        
            imc = round(peso / (altura**2),2)
  
            if imc < 18.5:
                    indice = "Tiene falta de peso, Su imc es",imc
            elif imc >= 18.5 and imc <= 24.99:
               indice = "Esta en su peso, Su imc es",imc
            elif imc >= 25 and imc <= 29.99:
                    indice = "Tiene sobrepeso, Su imc es",imc
            elif imc >= 30:
                indice = "Tiene obesidad, Su imc es",imc
    
    except ValueError:
        indice = "Error introduzca valores numericos validos para peso y/o altura"
    except ZeroDivisionError:
        indice = "Error, la altura es 0"
    except imc == 0:
            indice = "Error, el peso no puede ser 0"
    except imc < 0:
        indice = "Error, no puede introducir valores negativos"
    
        
            
    return render_template("index.html", indice=indice)
    

app.run()