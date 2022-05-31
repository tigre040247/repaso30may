#importar la libreria flask
from flask import Flask, render_template, abort


#instanciar la aplicación
#incializacion de la variable
app = Flask(__name__, template_folder= 'templates')



# Definicion de rutas cualquiera de las dos rutas se encuentran bien ('/) o la ruta (/index/')
@app.route('/')
@app.route('/index/')
# Llamar a hello
def hello():
    return'<h1>Hello, world</h1>'

# Definicion de rutas para mostrar string en otra ruta 

@app.route('/about/')
# Llamar a about
def about():


        return '<h3>PRUEBA 2</h3>'

# Definicion de rutas ESCRIBIMOS HASTA CAPITALIZE Y LO QUE VA ENTRE LOS SIGNOS DE MAYOR Y MENOR SE EMPRIME 
@app.route('/capitalize/<word>/')
# Llamar a ruta
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))



# Definicion de rutas para sumar o dividir o multiplicar 
@ app.route('/suma/<int:numero1>/<int:numero2>/') #En la parte de <int:numero 1> se coloca el numero en el browser
# Llamar a ruta
def suma(numero1, numero2):
    return '<h1>{}</h1>'.format(numero1 + numero2) #aqui se puede cambiar la suma resta o multiplicacion 


# Definicion de rutas para unir palabras
@ app.route('/concatenar/<string:pala1>/<string:pala2>/') #En la parte de <concatenar/pala1> se coloca el numero en el browser
# Llamar a ruta
def concatenar(pala1, pala2):
    return '<h1>{}</h1>'.format(pala1 + pala2) 




# Definicion de rutas
#@ app.route('/concatenar/<str:n1>/<str:n2>/')
# Llamar a ruta
#def concatenar(n1, n2):
  #  return '<h1>{}</h1>'.format(n1, n2)

# Definicion de rutas por id llamamos con un numero empezando desde el cero hasta el dos 

@ app.route('/users/<int:user_id>/')
# Llamar a ruta
def greet_users(user_id):
    usuario=['Lucas', 'Pato', 'Donal']
    try:
        return '<h2>{}</h2>'.format(usuario[user_id])
    except IndexError:
        abort(404)

#ruta principal
#ruta - Página principal, para llamar a un archivo de html
@app.route('/indexrepaso')
#Llamar a index.html en la ruta principal
def principal():
    return render_template('index.html')

#ruta inicio
@app.route('/menu')
#Llamar a index.html en la ruta principal
def menuNaturaleza():
    return render_template('inicio.html')

#main del programa
if __name__ == '__main__':
    #debug = True, para reiniciar automáticamente el servidor
    app.run(debug=True)