from flask import Flask ,request, abort
from sqlalchemy import or_
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
class Answepm(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    compt = db.Column(db.Integer)
    vai = db.Column(db.String(20), unique = False , nullable = False)
    mail = db.Column(db.String(20), unique = False , nullable = False)
    question = db.Column(db.Integer)
    reponse = db.Column(db.Integer)
    
    def __init__(self,compt,vai,mail,question,reponse):
        self.compt = compt
        self.vai = vai
        self.mail = mail
        self.question = question
        self.reponse = reponse
    
    def __repr__(self):
        
        return {
            "compt": self.compt,
            "vai": self.vai,
            "mail": self.mail,
            "question": self.question,
            "reponse": self.reponse,
            
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

    user = classement.query.get(session['utilisateur_id'])
    user.note = 0
    db.session.commit()

    # ude = Answepm.query.all()
    # for i in ude:
    #     if i.mail==useru.nom :
    #         udep = Answepm.query.all()
    #         db.session.delete(i.id)
    #         db.session.commit()
    # ude = Answepm.query.filter_by(mail=useru.nom).all()

    # for i in ude:
    #     db.session.delete(i)

    # db.session.commit()

        

    # db.session.commit()
    return render_template("acceuil.html")


@app.route('/add')
def add():
    ude = Maboutik.query.filter(or_(Maboutik.reponse == 1, Maboutik.reponse == 2, Maboutik.reponse == 3, Maboutik.reponse == 4)).all()

    for i in ude:
        db.session.delete(i)

    db.session.commit()
    return render_template("quizz.html")



@app.route('/index')
def index():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if is_translator_request():
        abort(403)
    
      

    data = datetime.date.today()
    dataheure = datetime.datetime.now()
    formatted_time = dataheure.strftime('%H')
    formatted = dataheure.strftime('%M')
    sec = dataheure.strftime('%S')
    # print(formatted_time)sc
    # print(formatted)
    # print(sec)
    # print(dataheure)
    
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    if az == 1 :
        ude = Answepm.query.filter_by(mail=useru.nom).all()

        for i in ude:
            db.session.delete(i)

        db.session.commit()

          
    if az <= len(eude) :
        # print(az)
        
        user = Maboutik.query.filter_by(id=az).first()
        
        question = user.question
        deux= user.deux
        premier= user.premier
        trois = user.trois
        quatre =user.quatre
        reponse= user.reponse
        userup = compte.query.get(2)
        cd = userup.comp
        # print(cd)
        plo = compte.query.get(1)
        plop = plo.comp
        gang = [question,[premier,deux,trois,quatre]]
        return render_template("index.html",gang=gang,sec=sec,cd=cd,plop=plop)
    # print(useru.nom)
    plo = compte.query.get(1)
    plop = plo.comp
    print(useru.nom)
    user = classement.query.filter_by(comp=useru.nom).first()
    fds = user.id
    print(fds)
    userump = classement.query.get(fds)
    userump.note = plop
    db.session.commit()
    return redirect("/fin")

@app.route('/pons',methods=["POST"])
def pons():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    if is_translator_request():
        abort(403)
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    
   
    user = Maboutik.query.filter_by(id=az).first()
    
    
    reponse= user.reponse
    question = request.form["qui"]
    if question == 1 :
        question = 2
    elif question == 2 :
        question = 1
    else :
        pass
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
        # ust = classement.query.get(1)
        # print(ust.id)
        # azp = ust.note+1
        # ust.note = azp
        # db.session.commit()

        user = compte.query.get(2)
        user.comp = user.comp + 1
        db.session.commit()

        ajout = Answepm(compt=az,vai="vrai",mail=useru.nom,question=question,reponse=reponse)
        db.session.add(ajout)
        db.session.commit()
        return redirect("/bien")
    
    # ust = classement.query.get(1)
    # ust.note = 0
    # db.session.commit()
    ajout = Answepm(compt=az,vai="faux",mail=useru.nom,question=question,reponse=reponse)
    db.session.add(ajout)
    db.session.commit()
    return redirect("/mention")



@app.route('/mention')
def mention():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    
    
    return render_template("mention.html")



@app.route('/mentione')
def mentione():
    if 'utilisateur_id' in session:
        useru = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    
    

    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    user = Maboutik.query.filter_by(id=az).first()
    
    
    reponse= user.reponse
    taz = []
    eudpe = compte.query.all()
    user = compte.query.get(1)
    if user.comp <= len(eude) :
        user.comp = user.comp + 1
        # print(user.comp)
        
        db.session.commit()
    else : 
        return redirect("/")

    if int(reponse) < 4 :
        question = int(reponse)+1
    elif reponse == 4 :
        question = int(reponse)-1
    else :
        pass


    ajout = Answepm(compt=az,vai="faux",mail=useru.nom,question=str(question),reponse=reponse)
    db.session.add(ajout)
    db.session.commit()


    return render_template("mention.html")


# DECONNEXION {}
@app.route('/deconnexion')
def deconnexion():
    session.pop('utilisateur_id', None)
    return redirect('/pre')
# FIN DECONNEXION {}
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










@app.route('/classez')
def classez():
   
    classep = classement.query.all()
    eudpe = Profiles.query.all()
    datae = compte.query.get(2)
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
            aqsz = i
            print("voivi ",aqsz)
            break

    
    txs= [aqsz[0],aqsz[1]]
    aouo=[20, 'Emmanuel DEDY']
    
    print(txs,maxe,aqsz[1])
    lenm= len(tab)-2
    qcs=[]
    for a in tab[::-1]:
        qcs.append(a)

    qsw = qcs.index(txs)+1
    # for o in qcs :
    #     if o == txs :
    #         qsw = tab.index(o)
    #         break
    
    
    
    return render_template("classement.html",tab=qcs,comp=comp,maxe=txs,lenm=lenm,qsw=qsw)
@app.route('/admin')
def admin():
    if 'utilisateur_id' in session:
        sessionp = Profiles.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre')
    classep = classement.query.all()
    eudpe = Profiles.query.all()
    datae = compte.query.get(2)
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
            aqsz = i
            print(aqsz)
            break

    dss = sessionp.nom
    txs= [datae.comp,dss]
    print(txs)
    lenm= len(tab)-2
    qcs=[]
    for a in tab[::-1]:
        qcs.append(a)

    qsw = qcs.index(txs)+1
    # for o in qcs :
    #     if o == txs :
    #         qsw = tab.index(o)
    #         break
    
    
    
    return render_template("admin.html",tab=qcs,comp=comp,maxe=txs,lenm=lenm,qsw=qsw,sessionpp=sessionp.nom)



@app.route('/add_data')
def add_data():
    
    return render_template("insc.html")

@app.route('/insc',methods = ["POST"])
def insc() :
    
    user = Profiles.query.filter_by(nom = request.form.get("nom")).first()
    if user :
        return redirect("/add_data")
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
        classem = classement(comp=nom,note=0)
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
    eudeuy = Answepm.query.all()
    
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
    




def is_translator_request():
    # Liste des identifiants d'agents utilisateur de traducteurs automatiques courants
    translator_user_agents = ["GoogleTranslate", "MicrosoftTranslator", "BingPreview", "SDL Translation"]

    user_agent = request.headers.get('User-Agent', '').lower()

    for translator in translator_user_agents:
        if translator.lower() in user_agent:
            return True

    return False

# @app.route('/')
# def home():
#     if is_translator_request():
#         abort(403)  # Interdit l'accès si une requête provient d'un traducteur automatique

    # Le reste du code pour la page d'accueil
    # return "Bienvenue sur mon site !"

@app.route('/ans',methods = ["POST"])
def ans():
   
    eude = Maboutik.query.all()
    i = compte.query.filter_by(id=1).first()
    az = i.comp
    
    # print(az)
    nom=request.form.get("quyi")
    nomypm=request.form.get("quypmi")
    print("me lo ",nomypm)
    
    if int(nomypm)==-1 :
        print("sdfg")
        user = Maboutik.query.filter_by(id=20).first()
        
    else:
        user = Maboutik.query.filter_by(id=nomypm).first()
    
    question = user.question
    deux= user.deux
    premier= user.premier
    trois = user.trois
    quatre =user.quatre
    reponse= user.reponse
    userup = compte.query.get(2)
    cd = userup.comp
    # print(cd)
    plo = compte.query.get(1)
    plop = plo.comp
    gang = [question,[premier,deux,trois,quatre],int(nomypm)]
    
    
    
    # Answepm
    eude = Answepm.query.all()
    ez = []
    for i in eude :
        if i.mail == nom :
            ez.append(i)

    
    inde = Maboutik.query.get(int(nomypm))
    indeet = Answepm.query.get(int(nomypm))
    # print(int(nomypm),indeet)
    # or indeet==20 or indeet==-1
    if int(nomypm)==20 or int(nomypm)==-1 :
        

        nomypm=-1
        inde = Maboutik.query.get(int(nomypm))
        indeet = Answepm.query.get(20)
        print("20Nous",indeet.question)
        fdsg = ez[-1].vai
        inde = Maboutik.query.get(20)
        ind = ez[-1]
        
        # cdf = indeet.question
        fdsg = ez[int(nomypm)].vai
        print("bonne",int(inde.reponse))
        # print("a",inde.reponse)
        # print(nomypm)
        # print(fdsg)
        return render_template("ans.html",gang=gang,eude=eude,fdsg=fdsg,inde=int(inde.reponse),indeet=indeet)
    print("bonne",int(inde.reponse))
    # if indeet == 1 :
    #     indeet = 2
    # elif indeet == 2:
    #     indeet == 1
    # else :
    #     pass
    fdsg = ez[int(nomypm)].vai
    comptc = ez[int(nomypm)].compt
    # if fdsg == "faux":
    #     a=0
    # else :
    #     a=1
    # print(fdsg)
    # print("ak",inde.reponse)
    # print("b",indeet.question)
        
    print("Nous",indeet.question)
    return render_template("ans.html",gang=gang,eude=eude,fdsg=fdsg,inde=int(inde.reponse),indeet=indeet.question)
    # print(useru.nom)
    
   

@app.route('/imp',methods=["POST"])
def imp():
    user = Profiles.query.filter_by(nom=request.form.get("quyi")).first()
    nom=request.form.get("quyi")
    # Answepm
    eude = Answepm.query.all()
    ez = []
    for i in eude :
        if i.mail == nom :
            ez.append(i)
    print(eude[1].vai)
    return render_template('imp.html',eude=ez,nom=nom)
if __name__ == '__main__' :
    app.run(debug=True,port=5007)
