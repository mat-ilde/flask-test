from app import app

@app.route('/')
def greeting():
    return "Hello, World!"
''' Esto es una función que cree usando flask para obtener según si el número par 
o impar de manera random cara o cruz.'''
from app import app
@app.route('/luck')
def luck():
    cara_o_cruz=get_the_word_by_numbers()
    html_string='''<!DOCTYPE html>
                    <html>
                    <body>
                    <h1>Bienvenido a mat-ilde tu resultado ha sido: '''+cara_o_cruz+'''</h1>
                    </body>
                    </html>'''
    return html_string

def get_random_number():
    import random
    number=random.randrange(10)
    return number

def get_the_word_by_numbers():
    random_number=get_random_number()
    if random_number==random_number%2:
        return("Cara")
    return ("Cruz")

'''Función para obtener la hora actual al acceder a la página web.'''
from app import app
@app.route('/time')
def get_time():
    actual_time=get_actual_time()
    html_string='''<!DOCTYPE html>
                    <html>
                    <body>
                    <h1>Bienvenido a mat-ilde la hora es : '''+actual_time+'''</h1>
                    </body>
                    </html>'''
    return html_string
import time 
def get_actual_time():
    hora=time.strftime("%H:%M:%S")
    return hora

    
