import sqlite3
from random import randint
db_name = 'quiz.sqlite'
conn = None
curor = None
quizes = [
        ('Своя игра', ),
        ('Кто хочет стать миллионером?', ),
        ('Самый умный', )]

questions = [
        ('Сколько месяцев в году имеют 28 дней?'  ,'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зеленый утес, если упадет в Красное море?'  ,'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?' ,'Ложкой', 'Правой',  'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?' , 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?' ,'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?' ,'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')]
def zopen():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    zopen()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()
def cek():
    cursor.execute("""SELECT question_id FROM quiz_content 
                    WHERE quiz_id = 5 ORDER BY id""")

    
def create():
    global questions, quizes
    zopen()
    # создание таблиц
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT,
        wrong1 TEXT,
        wrong2 TEXT,
        wrong3 TEXT)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS quiz 
    (id INTEGER PRIMARY KEY, name VARCHAR)
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS quiz_content (
    id INTEGER PRIMARY KEY,
    quiz_id INTEGER,
    question_id INTEGER,
    FOREIGN KEY (quiz_id) REFERENCES quiz (id))""")

    cursor.execute('''PRAGMA foreign_keys=on''') 

    # вставка элементов


    for i in questions: cursor.execute("""INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)""",i)
    for i in quizes: cursor.execute("""INSERT INTO quiz (name) VALUES (?)""",i)
    conn.commit()
    # создание связей

    

    """query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    answer = input("Добавить связь (y / n)?")
    while answer != 'n':
       quiz_id = int(input("id викторины: "))
       question_id = int(input("id вопроса: "))
       cursor.execute(query, [quiz_id, question_id])
       conn.commit()
       answer = input("Добавить связь (y / n)?")"""


def show(table):
    query = 'SELECT * FROM ' + table
    zopen()
    cursor.execute(query)
    print(cursor.fetchall())

def show_tables():
    show('questions')
    show('quiz')
    show('quiz_content')
def show2():
    cursor.execute("""SELECT quiz_content.id, questions.question, questions.answer 
                    FROM quiz_content, questions
                    WHERE quiz_content.question_id == questions.id 
                    AND quiz_content.quiz_id == 3
                    ORDER BY quiz_content.id""")
    print(cursor.fetchall())
def count(x):
    g = 0
    for i in x:
        g += 1
    return g
def choose():
    cursor.execute("""SELECT name FROM quiz ORDER BY id""")
    x = cursor.fetchall()
    n = ""
    for i in x:
        n += f" {x.index(i)} {i}".replace("(","").replace(")","").replace("'","")
    b = input("Выбирите Викторину:"+n)
    get_question(int(b)+1)
def get_question(quiz_id):
    quests = []
    cursor.execute("""SELECT questions.question, questions.answer, questions.wrong1, questions.wrong2, questions.wrong3
                    FROM quiz_content, questions
                    WHERE quiz_content.question_id == questions.id 
                    AND quiz_content.quiz_id == (?)
                    ORDER BY questions.id""",[quiz_id])
    quests = cursor.fetchall()
    balls = 0
    return quests
    r"""for i2 in quests:
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
            h += f"\n({i}) {indexs[i][1]}"
        print(str(i2[0])+h)
        x = input()
    """
        
    
    pass
def main(z):
    #clear_db()
    #create()
    zopen()
    z = get_question(z)
    close()
    return z

if __name__ == "__main__":
    main()
