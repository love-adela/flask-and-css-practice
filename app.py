from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbBlog

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/api/article', methods=['GET'])
def get_articles():
    result = list(db.articles.find({}, {'_id':0}))
    return jsonify({'result':'success', 'articles': result})

@app.route('/api/article', methods=['POST'])
def post_articles():
    article = request.get_json()

    # 제목, 부제, 내용 중 하나가 비어있을 경우, 400 Bad Reqeust 반환
    if not (article['title'] and article['subtitle'] and article['content']):
        return jsonify({'result':'failed'}), 400

    db.articles.insert_one(article)
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
