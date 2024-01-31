from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response


# import datetime

# data = datetime.date.today()
# dataheure = datetime.datetime.now()
# formatted_time = dataheure.strftime('%H')
# formatted = dataheure.strftime('%M')
# print(formatted_time)
# print(formatted)
# print(dataheure)


from flask import Flask, request, render_template, redirect, url_for,send_file

# import pywhatkit

# Configurations pour le serveur SMTP


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'



db = SQLAlchemy(app)



debug = True

class compte(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    comp = db.Column(db.Integer)
    
    def __init__(self,comp):
        self.comp = comp
    
    def __repr__(self):
        
        return {
            "comp": self.comp,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class Maboutik(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(100), unique = False , nullable = False)
    deux= db.Column(db.String(100), unique = False , nullable = False)
    premier = db.Column(db.String(100), unique = False , nullable = False)
    trois= db.Column(db.String(100), unique = False , nullable = False)
    quatre = db.Column(db.String(100), unique = False , nullable = False)
    reponse = db.Column(db.String(100), unique = False , nullable = False)
   
    def __init__(self,question,deux,premier,trois,quatre,reponse):
        self.question = question
        self.deux = deux
        self.premier = premier
        self.trois = trois
        self.quatre = quatre
        self.reponse = reponse


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(question: {self.question}, deux: {self.deux}, age: {self.age})"
    def __repr__(self):
        
        return {
            "question": self.question,
            "deux": self.deux,
            "premier": self.premier,
            "trois": self.trois,
            "quatre": self.quatre,
            "reponse": self.reponse
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

# user = Maboutik.query.filter_by(id=id).first()
# eude = Maboutik.query.all()





@app.route('/mention')
def mention():
    
    return render_template("mention.html")



@app.route('/bien')
def bien():
    
    return render_template("bien.html")


@app.route('/')
def acceuil():
    user = compte.query.get(1)
    user.comp = 1
    db.session.commit()

    user = compte.query.get(2)
    user.comp = 0
    db.session.commit()
    return render_template("acceuil.html")


@app.route('/add')
def add():
    
    return render_template("quizz.html")

@app.route('/index')
def index():
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    if az <= len(eude) :
        print(az)
        
        user = Maboutik.query.filter_by(id=az).first()
        
        question = user.question
        deux= user.deux
        premier= user.premier
        trois = user.trois
        quatre =user.quatre
        reponse= user.reponse

        gang = [question,[premier,deux,trois,quatre]]
        return render_template("index.html",gang=gang)
    return redirect("/fin")

@app.route('/pons',methods=["POST"])
def pons():
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    
   
    user = Maboutik.query.filter_by(id=az).first()
    
    
    reponse= user.reponse
    question = request.form["qui"]
    if question :
        eudpe = compte.query.all()
        user = compte.query.get(1)
        if user.comp <= len(eude) :
            user.comp = user.comp + 1
            print(user.comp)
        
            db.session.commit()
        else : 
            return redirect("/")

    if question == reponse:
        user = compte.query.get(2)
        
        user.comp = user.comp + 1
        db.session.commit()
        return redirect("/bien")
    return redirect("/mention")

@app.route('/fin')
def fin():
    usz = compte.query.get(1)
    moi = usz.comp//2
    pet = usz.comp-1
    user = compte.query.get(2)
    gang = user.comp
    return render_template("fin.html",gang=gang,pet=pet,moi=moi)

@app.route('/add',methods=["POST"])
def quizz():
    question = request.form["question"]
    premier = request.form["premier"]
    deux = request.form["deux"]
    trois = request.form["trois"]
    quatre = request.form["quatre"]
    reponse = request.form["reponse"]

    ajout = Maboutik(question=question,premier=premier,deux=deux,trois=trois,quatre=quatre,reponse=reponse)
    db.session.add(ajout)
    db.session.commit()
    return render_template("acceuil.html")




if __name__ == '__main__' :
    app.run(debug=True,port=5007)
