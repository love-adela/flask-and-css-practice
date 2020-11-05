from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article', methods=['GET'])
def get_articles():
    # TODO: 1. 모든 docuemtn 찾기 & _id 값은 출력에서 제외하기
    # TODO: 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!'})

@app.route('/article', methods=['POST'])
def post_articles():
    # TODO: 1.클라이언트로부터 데이터 받기
    data = request.get_json()
    
    # article = {'title': title, 'subtitle': subtitle, 'content': content}
    # TODO: 2.mongoDB에 데이터 넣기
    # db.articles.insert_one(article)
    return jsonify({'result':'success', 'result_data': data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)