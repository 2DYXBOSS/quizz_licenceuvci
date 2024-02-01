from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response


import datetime

data = datetime.date.today()
dataheure = datetime.datetime.now()
formatted_time = dataheure.strftime('%H')
formatted = dataheure.strftime('%M')
print(formatted_time)
print(formatted)
print(dataheure)


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



class Connecter(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(20), unique = False , nullable = False)
    password = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,nom,password):
        self.nom = nom
        
        self.password = password

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, email: {self.email}, password: {self.password})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "password": self.password
        }
    
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
class classement(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    comp = db.Column(db.String(20), unique = False , nullable = False)
    note = db.Column(db.Integer)
    
    def __init__(self,comp,note):
        self.comp = comp
        self.note = note
    
    def __repr__(self):
        
        return {
            "comp": self.comp,
            "note": self.note,
            
        }
    
with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")
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
class Profiles(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(20), unique = False , nullable = False)
  
    password = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,nom,password):
        self.nom = nom
    
        self.password = password

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, email: {self.email}, password: {self.password})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "password": self.password
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
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    return render_template("mention.html")



@app.route('/bien')
def bien():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    return render_template("bien.html")


@app.route('/')
def acceuil():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
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
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    
    data = datetime.date.today()
    dataheure = datetime.datetime.now()
    formatted_time = dataheure.strftime('%H')
    formatted = dataheure.strftime('%M')
    sec = dataheure.strftime('%S')
    # print(formatted_time)
    # print(formatted)
    # print(sec)
    # print(dataheure)

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
        return render_template("index.html",gang=gang,sec=sec)
    return redirect("/fin")

@app.route('/pons',methods=["POST"])
def pons():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    
   
    user = Maboutik.query.filter_by(id=az).first()
    
    
    reponse= user.reponse
    question = request.form["qui"]
    if question :
        # eudpe = classement.query.all()
        # cla = classement.query.get(1)
        taz = []
        eudpe = compte.query.all()
        user = compte.query.get(1)
        if user.comp <= len(eude) :
            user.comp = user.comp + 1
            # print(user.comp)
            
            db.session.commit()
        else : 
            return redirect("/")

    if question == reponse:
        ust = classement.query.get(1)
        print(ust.id)
        azp = ust.note+1
        ust.note = azp
        db.session.commit()

        user = compte.query.get(2)
        user.comp = user.comp + 1
        db.session.commit()
        return redirect("/bien")
    
    ust = classement.query.get(1)
    ust.note = 0
    db.session.commit()
    return redirect("/mention")

@app.route('/fin')
def fin():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    usz = compte.query.get(1)
    moi = usz.comp//2
    pet = usz.comp-1
    user = compte.query.get(2)
    gang = user.comp
    uszt = classement.query.get(session['utilisateur_id'])
    uszt.note = gang
    uszt.comp = uszt.comp
    db.session.commit()
    return render_template("fin.html",gang=gang,pet=pet,moi=moi)

@app.route('/adde',methods=["POST"])
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
    return redirect("/add")










@app.route('/admin')
def admin():
    classep = classement.query.all()
    eudpe = Profiles.query.all()
    tab = []
    for i in classep :
        tab.append([i.note,i.comp ])
    q=[]
    tab = sorted(tab)
    w= reversed(tab)
    comp=[]
    for i in tab:
        q.append(i[0])

    maxe = max(q)
    for i in tab:
        if maxe == i[0] :
            txs = i
            break
        

    lenm= len(tab)-2
    return render_template("admin.html",tab=tab,comp=comp,maxe=txs,lenm=lenm)



@app.route('/add_data')
def add_data():
    
    return render_template("insc.html")

@app.route('/insc',methods = ["POST"])
def insc() :
    
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if request.method == "POST" :
        nom = request.form.get("nom")
        print(nom)
        pseudo = request.form.get("pseudo")
        password = request.form.get("password")
        print(password)

        conpassword = request.form.get("conpassword")
        if conpassword != password :
            flash("Entrez le meme mot de passe")
            return redirect("/add_data")
        p = Profiles(nom = nom, password = password)

        db.session.add(p)
        db.session.commit()
    if request.method == "POST" :
        classem = classement(comp=nom,note="premier")
        db.session.add(classem)
        db.session.commit()

    return redirect("/pre")

    









@app.route('/pre')
def pree():
    return render_template('conn.html')
@app.route('/sprome',methods = ["GET","POST"])
def sprome() :
    compte = 0
    eudeu = Profiles.query.all()
    Profilesp = Maboutik.query.all()
    eude = [eudeu,Profilesp]
    user = Profiles.query.filter_by(nom = request.form.get("nom") , password = request.form.get("password")).first()
    userr = Connecter.query.filter_by(nom = request.form.get("nom") ,password = request.form.get("password")).first()

    if user :
        
        datae = Profiles.query.get(user.id)
        
        print(f"vous etes connecter{user.nom}{user.id}")
        

        session['utilisateur_id'] = user.id
        return redirect('/')

    # elif userr :
    #     session['admining_id'] = userr.id
    #     return redirect('/admining')
    else :

        flash("Email ou Mot de passe invalide")
        return redirect("/pre")
    


@app.route('/p')
def p():
    return render_template('p.html')
    







if __name__ == '__main__' :
    app.run(debug=True,port=5007)
