from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
Codes = ['8*Golimar*Bola*8', '0*Perereca_buceta*0', '0$_Marciano_petista_$0', '(_Cuzin0Cabeludo_)']

@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        codigo = request.form['nm']
        if codigo in Codes:
            return redirect(url_for('Sesi'))
        else:
            return redirect(url_for('fail'))
    else:
        return render_template('Login.html')
    
@app.route('/Sesi')
def Sesi():
    return render_template('Sesi.html')

@app.route('/fail')
def fail():
    return render_template('Tocando_baixo.html')

if __name__ == '__main__':
	app.run(debug=True)