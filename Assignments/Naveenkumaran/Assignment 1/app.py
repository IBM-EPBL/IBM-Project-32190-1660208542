from flask import Flask,redirect,url_for, request,render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route('/success/<name>/<mail>/<phno>')
def success(name,mail,phno):
    return render_template('display.html', username=name, email=mail, phone=phno)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        email = request.form['email']
        phone = request.form['phone']
        return redirect(url_for('success',name = user,mail = email, phno = phone))
    else:
        user = request.args.get('uname')
        email = request.args.get('email')
        phone = request.args.get('phone')
        return redirect(url_for('success',name = user,mail = email, phno = phone))
        
if __name__ == '__main__':
    app.run("localhost", 3050)
    