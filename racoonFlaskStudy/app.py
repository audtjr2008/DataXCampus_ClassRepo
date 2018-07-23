# -- coding: utf-8 --
from flask import Flask
from flask import render_template


app = Flask(__name__)


#app.roue 는 주소값을 나타낸다.
#이건 저 함수를 실행하라는 것이다.
#경로에 따라서 어떤것을 보여주는가가 Routing 이다.
#내 주소에 아무것도 입력하지 않았을때 '/'




@app.route('/')
@app.route('/<path>')
def pathfinder(path=None):
    # 플라스크 함수에서, string을 입력하면 자동으로 HTML로 변환하여 리턴해줌
    # 하지만 기본적으로 HTML 태그를 집어넣어야 한다.

    if path in ['2','3','4','6','12','13','14','15']:
        return render_template('/notes/note%s.html'%path)
    else :
        return  render_template('index.html')
    # TODO 나 열심히 할게요





#웹에서 /a를 추가하면 Hello World2 method가 실행된다.
@app.route('/a')
def hello_world2():
    return '<h1>Hello World2!</h1>'


# Run -> Edit configuration -> Debug mode check 하면
@app.route('/a/b')
def hello_world3():
    return '<h1>Hello World3!</h1>'

# 주소값에도 변수의 개념이 있다.
@app.route('/c/<name>')
def hello_worldc(name):
    return '<h1>Hello World3!%s</h1>'%name



# 시스템 설계시 어떤 입력을 받아서 어떤 결과를 줄것인가가 중요하다.
# 웹에서 입력은 링크나 주값 혹은 폼으로 입력해서 사용자 입력을 받는다.
# 오늘 정해야한다.
# 우리는 주소값 활용해서 결과값을 보여주는 방법을 알았다.


if __name__ == '__main__':
    app.run()

