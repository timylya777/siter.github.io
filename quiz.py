from db_scripts import *
from flask import *
from flask import request
session = {"answ":{},"numb":0,"ball":0}
css1 = r""" <head>
        <meta charset="UTF-8">
        <style>
                body {
        color: #000000
        };


        .select{
        background-color: #756b75;
        color: #f0e1f0;
        padding: 1.25% 1.25%;
        text-align: left;
        margin: 10% 0% 0% 44%

        }




        .btn{
        padding: 1.25% 1.25%;
        margin: 1% 0% 0% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        padding: 10px 30px;
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;
        }
        .text{
        
        padding: 1.25% 1.25%;
        margin: 7% 44% 0% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        padding: 10px 30px;
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;

        }
        .text2{
        
        padding: 1.25% 1.25%;
        margin: 1% 42% 1% 44%;
        font-family: Roboto, sans-serif;
        font-weight: 100;
        font-size: 14px;
        color: #fff;
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        border: none;
        box-shadow: rgb(0, 0, 0) 0px 9px 50px 0px;
        border-radius: 50px;
        transition : 1936ms;
        transform: translateY(0);
        display: flex;
        flex-direction: row;
        align-items: center;

        }

        .btn:hover{
        
        transition : 1936ms;
        padding: 10px 50px;
        transform : translateY(-0px);
        background: linear-gradient(164deg, #0066CC 0%, #c500cc 69%);
        color: #ffffff;
        border: solid 0px #0066cc;
        };
        list-style: none
            </style>
            <title>Викторина</title>
            </head>"""
def index():
    global session, css1
    session["numb"] = 0
    return css1 + r'''
                <h1 class="text">Выберите викторину</h1>
                  <h2>
                      <form  method="POST" action="choose">

            <br><z class="text2" ><input class="btn2" type ="radio" name="list" value="1"><a class="btn2">первая</a></z>
            <br><z class="text2" ><input class="btn2" type ="radio" name="list" value="2"><a class="btn2">вторая</a></z>
            <br><z class="text2" ><input class="btn2" type ="radio" name="list" value="3"><a class="btn2">третья</a></z>

            <input class="btn" type="submit"  value="Отправить"></button>

                  </h2>'''
def choose():
    if request.method == 'POST':
        session['quiz'] = request.form.get('list')
        #print(session['quiz'])
        return redirect(url_for('view'))
def view():
    global session
    quests = main(int(session['quiz']))
    xop = 0
    session["numb"] += 1 
    if request.method == 'POST':
        for i2 in quests:
            xop += 1
            answers = []
            indexs = {}
            
            z = 0
            for i in i2:
                z += 1
                if z >= 2:
                    answers.append(i)
            z = 0
            while True:
                if count(indexs.keys()) == 4: break
                x = randint(1,4)
                if not x in indexs:
                    indexs[x] = [z,answers[z]]
                    z += 1
            h = ""
            for i in range(1,5):
                if  indexs[i][1] == answers[0]:
                    session["answ"][session["numb"]] = i 

                h += f"""<br><z class="text2" ><input class="btn2" type ="radio" name="1" value="{i}"><a class="btn2">({i}) {indexs[i][1]}</a></z>"""


            #print(str(i2[0])+h)
            x = """<form method="POST" action="view">"""
            
            if xop == session["numb"]:
                if session["answ"][session["numb"]-1] == int(request.form.get('1')):session["ball"] += 2
                else: session["ball"] += -1
                return  css1+'<h1 class="text">'+str(i2[0])+"</h1>"+x+h+'<br><input class="btn" type="submit" value="Отправить">'
    if request.method == 'GET':
        for i2 in quests:
            answers = []
            indexs = {}
            xop += 1
            z = 0
            for i in i2:
                z += 1
                if z >= 2:
                    answers.append(i)
            z = 0
            while True:
                if count(indexs.keys()) == 4: break
                x = randint(1,4)
                if not x in indexs:
                    indexs[x] = [z,answers[z]]
                    z += 1
            h = ""
            for i in range(1,5):
                if  indexs[i][1] == answers[0]:
                    session["answ"][session["numb"]] = i 

                h += f"""<br><z class="text2" ><input class="btn2" type ="radio" name="1" value="{i}"><a class="btn2">({i}) {indexs[i][1]}</a></z>"""
            #print(str(i2[0])+h)
            x = """<form method="POST" action="view">"""
            
            if  xop == session["numb"]:
                return  css1+'<h1 class="text">'+str(i2[0])+"</h1>"+x+h+'<br><input class="btn" type="submit" value="Отправить">'

    return css1 + '<a class="text" href="/finish">Закончить викторину</a>'
def finish():
    return css1 + f"""<h1 class="text">Викторина закончена</h1>
    <br><h2><a class ="text2">C счётом:{session["ball"]}</a></h2>
    <br><h2><a class ="text2" href='/'>Выбрать другую викторину</a></h2>
    """
    session["numb"] = 0
def css():
    return 
app = Flask(__name__) # создаём объект веб-приложения
if __name__ == "__main__":
    app.add_url_rule('/', 'index', index, methods=['POST', "GET"])
    app.add_url_rule('/choose', 'choose', choose, methods=['POST','GET'])
    app.add_url_rule('/view', 'view', view, methods=['POST', "GET"])
    app.add_url_rule('/finish', 'finish', finish)

    #app.run(debug=True)
    app.run()
