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
    # TODO: 제목이나 내용이 비어있으면 글쓰기 막고 400 Bad Request 반환해야함
    article = request.get_json()
    db.articles.insert_one(article)
    return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
