# from flask import Flask, jsonify, request, session, redirect
# from passlib.hash import pbkdf2_sha256
# import hashlib 
# import uuid
# from werkzeug.security import generate_password_hash, check_password_hash

# from app import db

# class User:

#     def start_session(self, user):
#         del user['password']
#         session['logged_in'] = True
#         session['user'] = user
#         return jsonify(user), 200

#     def signup(self):
#         print(request.form)

#         #user객체 생성하기
#         user = {
#             "_id": uuid.uuid4().hex, #고유 식별자 만들어주는 거
#             "name": request.form.get('username_give'),
#             "email": request.form.get('email_give'),
#             "password": request.form.get('pw_give')
#         }

#         # password 암호화(encryption) -- 여러 시도들
#         # user['password'] = pbkdf2_sha256.hash(user['password'])
#         # user['password'] = hashlib.sha256(user['password'].encode())
#         user['password'] = generate_password_hash(user['password'])
        

#         # 이미 존재하는 email인지 확인하기
#         if db.users.find_one({"email": user['email']}):
#             return jsonify({"error": "email address is already in use"}), 400

#         if db.users.insert_one(user):
#             return self.start_session(user)

#         return jsonify({"error": "Signup failed"}), 400

#     def signout(self):
#         session.clear()
#         return redirect('/') 

#     def login(self):
#         user = db.users.find_one({
#             "email": request.form.get('email')
#         })
#         #패스워드도 확인하는 절차 : 앞에 암호화된 부분, 뒤에를 암호화 안 된 입력값으로 넣어야 되더라는!(순서 중요)
#         if user and check_password_hash(user['password'], request.form.get('password')):
#             return self.start_session(user)
            
#         return jsonify({"error": "invalid login credentials"}), 401

