from flask import Flask, render_template
app = Flask(__name__)

@app.route('/apresentacao')
def apresentacao():
    return render_template('apresentacao.html')

@app.route('/sobre') 
def sobre():
    return render_template('sobre.html')

@app.route('/final')
def final():
    return render_template('final.html')
    
if __name__ == '__main__':
    app.run(debug=True)
