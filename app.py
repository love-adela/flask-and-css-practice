from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title = '아델라의 블로그'
        )

# TODO: POST 방식으로 아티클 생성 요청
# @app.route('/articles', methods=['POST'])
# def post_article():
#     url_receive = request.form['']

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)