from flask  import Flask, redirect, url_for, render_template, request,session, send_from_directory, flash, json
import time
from datetime import timedelta
import services.encryptionModule as encrypt

app = Flask(__name__, static_url_path='/static')
app.secret_key =b"y@4^U8MCRvo5dIOYmRZ*axIObW$Te6yL^X706$32e0q1XSN0rI1Oz!K$As7ckzfx%AWNr2Y&WJaP!5q8DrRxNhOgOMtO1*OJcFM"
app.permanent_session_lifetime = timedelta(minutes=60) # time before session data gets Cleared 
app.session_cookie_name ="PWD"



@app.route("/login", methods =["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "" or password == "":
            flash(u"Login Info can not be blank." , "error")
            return render_template("Login.html")   
        elif username =='admin' and password =='admin':
            session["Manager"] = True
            session["user"] = username
            # session.permanent = True
            return redirect(url_for("login"))
    else:
        if "user" in session:
            return redirect(url_for("home")) 
        else:      
            return render_template("Login.html")        
# Home screen

@app.route("/")
@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html")    
    else:
        return redirect(url_for("login"))  
    
     
# ===============================
# Logout Will session
@app.route("/logout")        
def logout():
    session.clear() #Clear the entire Session and force Relode 
    return redirect(url_for("login"))

#css path
@app.route('/CSS/<path:path>')
def send_css(path):
    return send_from_directory('CSS', path)
#Image path
@app.route('/Images/<path:path>')
def send_images(path):
    return send_from_directory('Images', path)

@app.route('/JS/<path:path>')
def send_JS(path):
    return send_from_directory('JS', path)


def pop_SessionData():
    session.pop()

#     username ='2317'
# strength =35
# # Encryption Serice 
# encryptedString = encrypt.stringEncrypt(username,strength)
# print(encryptedString)
# print(len(encryptedString))
# #  Decryption Service
# decryptedString = encrypt.strinDecrypt(encryptedString,strength)
# print(decryptedString)

if __name__ == "__main__":
    app.debug =True
    app.run()



