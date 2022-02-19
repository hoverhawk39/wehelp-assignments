import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jason9987',
    database='website',
)

from flask import Flask,request,redirect,render_template,session,jsonify
app = Flask(__name__, static_folder='static', static_url_path='/static/')
app.secret_key='something secret'
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/members', methods=['GET'])
def api():
    username=(request.args.get('username'),)
    c=db.cursor()
    sql='SELECT * FROM member WHERE username=%s'
    c.execute(sql,username)
    output=c.fetchone()
    c.close()
    # print(output)
    if output is not None:
        data={
            'id':output[0],
            'name':output[1],
            'username':output[2]
        }
    else:
        data=output
    return jsonify({'data':data})

@app.route('/signup', methods=['POST'])
def signup():
    name=request.form['name']
    username=(request.form['username'],)
    password=request.form['password']
    c=db.cursor()
    sql='SELECT username FROM member WHERE username=%s'
    c.execute(sql,username)
    output=c.fetchall()
    c.close()
    if(len(output)!=0):
        return redirect('/error/?message=帳號已經被註冊')
    else:
        username=username[0]
        c=db.cursor()
        sql ='INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
        val=(name,username,password)
        c.execute(sql,val)
        db.commit()
        c.close()
        return redirect('/')

@app.route('/signin', methods=['POST'])
def signin():
    act=request.form['account']
    pwd=request.form['password']
    c=db.cursor()
    sql='SELECT name,username,password FROM member WHERE username=%s AND password=%s'
    c.execute(sql,(act,pwd))
    output=c.fetchall()
    c.close()
    if(len(output)==1):
        session['status']=output[0][0]
        return redirect('/member/')
    else:
        return redirect('/error/?message=帳號或密碼輸入錯誤')

@app.route('/member/', methods=['GET'])
def member():
    if 'status' in session:
        name=session['status']
        return render_template('member.html',member_name=name)
    else:
        return redirect('/')

@app.route('/error/', methods=['GET'])
def error():
    msg=request.args.get('message')
    return render_template('error.html',data=msg)

@app.route('/signout', methods=['GET'])
def signout():
    session.pop('status', None)
    return redirect('/')

app.run(debug=True,port=3000)