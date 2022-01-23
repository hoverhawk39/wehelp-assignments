from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app = Flask(__name__,
            static_folder="static",
            static_url_path="/static/"
)
app.secret_key="something secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    act=request.form["account"]
    pwd=request.form["password"]
    if((act=="test") and (pwd=="test")):
        session["status"]="success"
        return redirect("/member/")
    elif((act=="") or (pwd=="")):
        return redirect("/error/?message=請輸入帳號、密碼")
    elif((act!="test") or (pwd!="test")):
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/member/", methods=["GET"])
def member():
    if(session["status"] != "success"):
        return redirect("/")
    else:
        return render_template("member.html")

@app.route("/error/", methods=["GET"])
def error():
    msg=request.args.get("message")
    return render_template("error.html",data=msg)

@app.route("/signout", methods=["GET"])
def signout():
    session["status"]="fail"
    return redirect("/")

app.run(debug=True,port=3000)