from app import app
@app.route('/')
def index():
    cara_o_cruz=get_the_word_by_numbers()
    html_string='''<!DOCTYPE html>
                    <html>
                    <body>
                    <h1>Bienvenido a Masex tu resultado ha sido: '''+cara_o_cruz+'''</h1>
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


    
