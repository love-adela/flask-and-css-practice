from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title = '아델라의 블로그',
        post_list = ['논리회로에서 음수 표현하기', '알고리즘 개념 잡기', '비둘기집의 원리'],
        post_subtitle = 'MSB의 값에 따라 양수와 음수를 표현할 수 있다.',
        post_date = ['2020-11-03',],
        tag_list = ['#computer_science', '#algorithm']
        )

# TODO: POST 방식으로 아티클 생성 요청
# @app.route('/articles', methods=['POST'])
# def post_article():
#     url_receive = request.form['']

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)