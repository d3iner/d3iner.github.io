#import for flask
from flask import Flask, render_template, request, redirect, url_for, send_file

#objects
from Graph import Graph, Graph2, Graph3


# Constants



# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# assign domain where we are
app = Flask(__name__)



#routes

@app.route("/")
def home():
    return redirect(url_for("Mecanicanewtoniana"))


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
def Leyesdenewton(range2=1, range3=1):
    return render_template("Leyesdenewton.html", range2=range2, range3=range3)

@app.route("/Modelos")
def Modelos():
    return render_template("Modelos.html")

@app.route("/Recursos")
def Recursos():
    return render_template("Recursos.html")

@app.route("/Temario")
def Temario():
    return render_template("Temario.html")

@app.route("/test", methods=["post"])
def test():
    array=[]
    for i in request.form:
        if request.form[i] == "":
            array.append(1.0)
        else:
            array.append(float(request.form[i]))
    print("hi")
    print(array)
    graph = Graph(L1=array[0], L2=array[1], M1=array[2], M2=array[3])
    graph.show()
    return redirect(url_for("Leyesdenewton"))

@app.route("/test2", methods=["post"])
def test2():
    print("hi")
    if request.form["force2"] == "":
        force=0.0
    else:
        force=float(request.form["force2"])
    #graph = Graph2(range=force)
    return Leyesdenewton(range2=request.form["force2"])

@app.route("/test3", methods=["post"])
def test3():
    print("hi")
    #graph = Graph3(range=int(request.form["range3"]))
    #print(request.form["range3"])
    return Leyesdenewton(range2=request.form["range3"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
