from flask import Flask, render_template, request, jsonify, session, redirect
from pymongo import MongoClient
from datetime import datetime
from functools import wraps


#models.py에서 추가로 import 필요한 것들.
# from passlib.hash import pbkdf2_sha256
import hashlib 
import uuid
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash


#routes.py에서 추가로 Import.

app = Flask(__name__)
app.secret_key = b'\xd79\x91@\x87\nM\x85=\xb0QL\n\xd5b('

client =  pymongo.MongoClient('localhost', 27017)
db = client.qnanswers


# 데코레이터 - 로그인 할 경우만 들어갈 수 있음
def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/contents')
@login_required
def contents():
    return render_template('contents.html')

@app.route('/userinfo')
def userinfo():
    return render_template('userinfo.html')

@app.route('/main/user')
@login_required
def afterlogin():
    return render_template('mainpage_after.html')

@app.route('/session')
def checksession():
    return render_template('session_view.html')

# API 역할을 하는 부분
# mainpage - section 2
@app.route('/get', methods=['GET'])
def home_get():
    home_question = list(db.qs.find({}, {'_id': False, 'question': 1}))
    home_answer = list(db.qs.find({}, {'_id': False, 'answer': 1}))

    return jsonify({'home_q': home_question, 'home_a': home_answer})


# contents
@app.route('/contents/get', methods=['GET'])
def contents_get():
    questions = list(db.qs.find({}, {'_id': False}))

    return jsonify({'all_questions': questions})


@app.route('/contents/post', methods=['POST'])
def contents_post():
    user_receive = request.form['user_give']
    question_receive = request.form['question_give']
    answer_receive = request.form['answer_give']

    # 시각 데이터로 원하는 문자열 만들기(한글일 경우)
    time_now = datetime.now()
    now_text = time_now.strftime("%Y{} %m{} %d{} %H{} %M{}")
    now_text = now_text.format('년', '월', '일', '시', '분')

            

    # db에 저장
    doc = {
        # 'user': session['user']['email'],
        'question': question_receive,
        'answer': answer_receive,
        'time': now_text
    }
    
    db.contents.insert_one(doc)

    return jsonify({'msg': '답변이 저장되었습니다.'})


# mypage
@app.route('/mypage/get', methods=['GET'])
def read_answers():
    answers = list(db.contents.find({}, {'_id': False}))
    # answers = list(db.mypage_sample.find({'id': 'id1'}, {'_id': False}))
    return jsonify({'all_answers': answers})


# # 정현님 로그인
# @app.route('/login/post', methods=['GET', 'POST'])
# def login():
#     email_receive = request.form['email_give']
#     pw_receive = request.form['pw_give']

#     users = list(db.register.find({}, {'_id': False, 'email': 1, 'pw': 1}))

#     emailli = []
#     pwli = []
#     for user in users:
#         emailli.append(user['email'])
#         pwli.append(user['pw'])

#     if "@" and "." not in email_receive:
#         return jsonify({"msg": "이메일을 확인해주세요"})
#     elif not (email_receive and pw_receive):
#         return jsonify({'msg': '패스워드를 입력해주세요'})
#     else:
#         # for user in users:
#         if email_receive in emailli and pw_receive in pwli:
#             return jsonify({'msg': '환영합니다'})
#         else:
#             return jsonify({'msg': '입력값을 확인하세요'})



# # register
# @app.route('/register', methods=['POST'])
# def register_info():
#     username_receive = request.form['username_give']
#     email_receive = request.form['email_give']
#     pw_receive = request.form['pw_give']
#     repeatpw_receive = request.form['repeatpw_give']

#     if "@" not in email_receive:
#         return jsonify({'msg': '이메일을 입력해주세요.'})

#     elif '.' not in email_receive:
#         return jsonify({'msg': '이메일을 완성해주세요'})

#     elif not (email_receive and pw_receive and repeatpw_receive):
#         return jsonify({'msg': '모두 입력해주세요'})

#     doc = {
#         'username': username_receive,
#         'email': email_receive,
#         'pw': pw_receive,
#         'repeatpw': repeatpw_receive
#     }

#     db.register.insert_one(doc)
#     return jsonify({'msg': '회원가입 완료!'})

# 이하  models.py 부분

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        #user객체 생성하기
        user = {
            "_id": uuid.uuid4().hex, #고유 식별자 만들어주는 거
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        
        # password 암호화(encryption) -- 여러 시도들
        # user['password'] = pbkdf2_sha256.hash(user['password'])
        # user['password'] = hashlib.sha256(user['password'].encode())
        user['password'] = generate_password_hash(user['password'])
        

        # 이미 존재하는 email인지 확인하기
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "이메일 주소가 이미 사용중입니다."}), 400

        if db.users.insert_one(user):
            return self.start_session(user)
            return jsonify({"msg":"회원가입 완료!"})

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/') 

    def login(self):
        user = db.users.find_one({
            "email": request.form.get('email')
        })
        #패스워드도 확인하는 절차 : 앞에 암호화된 부분, 뒤에를 암호화 안 된 입력값으로 넣어야 되더라는!(순서 중요)
        if user and check_password_hash(user['password'], request.form.get('password')):
            return self.start_session(user)
            print(session["logged_in"])
        return jsonify({"error": "invalid login credentials"}), 401

# routes.py
@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
