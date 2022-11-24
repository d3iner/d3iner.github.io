#import for flask
from flask import Flask, render_template, request, redirect, url_for, send_file

#objects
from Graph import Graph, Graph2


# Constants



# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# assign domain where we are
app = Flask(__name__)



#routes

@app.route("/")
def home():
    return render_template("Temario.html")



@app.route("/Mecanicanewtoniana")
def Mecanicanewtoniana():
    return render_template("Mecanicanewtoniana.html")

@app.route("/Aplicacion")
def Aplicacion():
    return render_template("Aplicacion.html")

@app.route("/Cinematica")
def Cinematica():
    return render_template("Cinematica.html")

@app.route("/Contactar")
def Contactar():
    return render_template("Contactar.html")

@app.route("/Cursos")
def Cursos():
    return render_template("Cursos.html")

@app.route("/Leyesdenewton")
def Leyesdenewton():
    return render_template("Leyesdenewton.html")

@app.route("/Modelos")
def Modelos():
    return render_template("Modelos.html")

@app.route("/Recursos")
def Recursos():
    return render_template("Recursos.html")

@app.route("/Temario")
def Temario():
    return render_template("Temario.html")

@app.route("/test")
def test():
    print("hi")
    graph = Graph()
    graph.show()
    return redirect(url_for("Leyesdenewton"))

@app.route("/test2")
def test2():
    print("hi")
    graph = Graph2()
    return redirect(url_for("Leyesdenewton"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
