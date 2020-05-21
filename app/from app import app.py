from app import app
'''creo un decorador, que es lo que lo da el comportamiento a la función cuando 
entramos en una ruta en concreto'''
@app.route('/')
def index():
    return ("hi")
@app.route('/index')
def outside():
    return("hola")