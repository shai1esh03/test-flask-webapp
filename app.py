from flask import Flask, render_template
# flask is module and FLask is Class

app = Flask(__name__)  
# app is an object of Class Flask. Variable __name__ 

@app.route("/")  
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)