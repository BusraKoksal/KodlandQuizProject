from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sinav.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)

class Question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    QuestionText=db.Column(db.String(800),nullable=False)
    optionA=db.Column(db.String(100), nullable=False)
    optionB=db.Column(db.String(100), nullable=False)
    optionC=db.Column(db.String(100), nullable=False)
    optionD=db.Column(db.String(100), nullable=False)
    correct_answer=db.Column(db.String(1),nullable=False)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(80),nullable=True)
    score=db.Column(db.Integer,default=0)
    previous_score = db.Column(db.Integer, default=0)

@app.route("/",methods=['GET','POST'])

def index():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        questions=Question.query.all()

        answers=[]
        for i in range(len(questions)):
            answer=request.form.get (f'answers{i+1}')
            answers.append(answer)

        
        questions=Question.query.all()
        score=0
        
        
        
        for i, question in enumerate(questions):
            if answers[i]==question.correct_answer:
                score+=1
        
          
          
                

        user = User.query.filter_by(email=email).first()
        if user:
            previous_score = user.score  # Mevcut skoru sakla (önceki skor)
            user.score = max(user.score, score)  # Skoru güncelle
            user.previous_score = previous_score  # Güncellenmiş önceki skoru ata
        else:
            user = User(username=username, email=email, score=score, previous_score=score)
            db.session.add(user)


                

        
        
        db.session.commit()

        high_score = User.query.order_by(User.score.desc()).first()
        return redirect(url_for('sonuc', score=score, high_score=user.score if user else 0,  
                        previous_score=user.previous_score, global_high_score=high_score.score if high_score else 0))

        






    questions=Question.query.all()

    return render_template("index.html",questions=questions)

@app.route("/sonuc")
def sonuc ():
    score=request.args.get('score',type=int,default=0)
    high_score=request.args.get('high_score',type=int,default=0)
    previous_score = request.args.get('previous_score', type=int, default=0) 
    global_high_score=request.args.get('global_high_score',type=int,default=0)
    return render_template("sonuc.html", score=score,high_score=high_score,previous_score=previous_score,global_high_score=global_high_score)
def add_questions():
    questions = [
        {"QuestionText": "Python ile sohbet botu otomasyonu hangi kütüphane ile yapılabilir?", "optionA": "Flask", "optionB": "Discord.py", "optionC": "TensorFlow", "optionD": "NLTK", "correct_answer": "B"},
        {"QuestionText": "Python ile web geliştirme için hangi framework kullanılabilir?", "optionA": "Flask", "optionB": "ImageAI", "optionC": "TensorFlow", "optionD": "BeautifulSoup", "correct_answer": "A"},
        {"QuestionText": "Yapay zeka geliştirmek için hangi kütüphane yaygın olarak kullanılır?", "optionA": "TensorFlow", "optionB": "NLTK", "optionC": "BeautifulSoup", "optionD": "Discord.py", "correct_answer": "A"},
        {"QuestionText": "Bilgisayar görüşü için hangi kütüphane kullanılabilir?", "optionA": "TensorFlow", "optionB": "BeautifulSoup", "optionC": "ImageAI", "optionD": "NLTK", "correct_answer": "C"},
        {"QuestionText": "Doğal Dil İşleme (NLP) için hangi kütüphane yaygın olarak kullanılır?", "optionA": "BeautifulSoup", "optionB": "TensorFlow", "optionC": "NLTK", "optionD": "ImageAI", "correct_answer": "C"},
    ]
    
    for q in questions:
        # Aynı sorunun veritabanında olup olmadığını kontrol et
        existing_question = Question.query.filter_by(QuestionText=q["QuestionText"]).first()
        if not existing_question:
            # Eğer soru veritabanında yoksa, yeni soruyu ekle
            question = Question(QuestionText=q["QuestionText"], optionA=q["optionA"], optionB=q["optionB"], optionC=q["optionC"], optionD=q["optionD"], correct_answer=q["correct_answer"])
            db.session.add(question)
    
    db.session.commit()


    def __repr__(self):
        return '<User %r>' % self.username
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_questions()
    app.run(debug=True)
