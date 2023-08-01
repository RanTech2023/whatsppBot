
import whatsAppbot as whatsApp
from flask import Flask,render_template,request
app =Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/whatsApp",methods=["POST","GET"])
def sendWts():
    if request.method=="POST":
        try:
            phoneNumber = request.form["phoneNumber"]
            article = request.form["article"]
            print(article)
            if phoneNumber!= None and article != None:
                if len(phoneNumber)>8:
                    phoneNumber=phoneNumber.replace(" ","")
                    if len(phoneNumber)==8:
                         whatsApp.webController(phoneNumber=phoneNumber,article=article)
                        
                    else:
                        atr = phoneNumber.split(",")
                      
                        for temp in atr:
                            print("temp :"+temp)
                            whatsApp.webController(phoneNumber=temp,article=article)
                    return render_template("200.html")
                   
                else:
                    return render_template("404.html")
        except Exception as err :
            print(err)
            return render_template("404.html")
    
