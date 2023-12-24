import os
from flask import Flask , redirect , render_template, request,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user,current_user
app=Flask(__name__,template_folder="./",static_url_path='',static_folder='./')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SECRET_KEY']='what_the_fuck'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    data_loc = db.Column(db.String(256))

    def set_data_loc(self,data_path):
        self.data_loc = data_path
    
#intialize all database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def get(id):
    return User.query.get(id)

def get_cur_user():
    if "user_id" in session:
        user = get(session["user_id"])
    else:
        user = None
    return user

@app.context_processor
def page_dict():
    user = get_cur_user()
    if user is not None:
        return dict(user_name=user.username,
            data_loc = user.data_loc)
    else:
        return dict(user_name="None",
            data_loc = "None")

@app.route('/',methods=['GET'])
@login_required
def get_home():
    #return render_template('home.html')
    return render_template('index.html')

@app.route('/lookglass',methods=['GET'])
@login_required
def get_lookglass():
    #return render_template('home.html')
    return render_template('lookglass.html')

@app.route('/login',methods=['GET'])
def get_login():
    return render_template('login.html')

#test data change
@app.route('/test',methods=['GET'])
def test():
    user = get_cur_user()
    user.data_loc = "this is a fake path"
    db.session.commit()
    return redirect("/")

# @app.route('/up_file', methods=['GET', 'POST'])
# def up_file():
#     if request.method == "POST":
#         file = request.files['file']
#         #file_name = "test.csv"
#         file_name = file.filename
#         file.save(os.path.join('userfiles', file_name))

#         return '上传成功'

@app.route('/upjson', methods=['GET', 'POST'])
def up_json():
    if request.method == "POST":
        jsondata = request.get_json()
        #print(jsondata)
        #1 save json to file
        jsondatastr = str(jsondata)
        cur_usr = get_cur_user()
        cur_usr.data_loc = os.path.join('userfiles', cur_usr.username+'.json')
        with open(cur_usr.data_loc,'w') as file:
            file.write(jsondatastr)
            file.flush()
        #2 record user json file to database
        db.session.commit()
        print(jsondata)

        return "data transfer succeed"
@app.route('/getjson', methods=['GET', 'POST'])
def get_json():
    if request.method == "GET":
        cur_usr = get_cur_user()
        jsondata = ''
        with open(cur_usr.data_loc,'r') as file:
            jsondata = file.readline()
        print(jsondata)
        return jsondata

@app.login_manager.unauthorized_handler
def unauth_handler():
    # if request.is_xhr:
    #     return jsonify(success=False,
    #                    data={'login_required': True},
    #                    message='Authorize please to access this page.'), 401
    # else:
    return redirect("/login")
#render_template('401.html'), 401

@app.route('/signup',methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login',methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    login_user(user)
    session['user_id'] = user.id
    return redirect('/')

@app.route('/signup',methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(username=username,email=email,password=password)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    login_user(user)
    session['user_id'] = user.id
    return redirect('/')

@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect('/login')

if __name__=='__main__':
    app.run(debug=True)