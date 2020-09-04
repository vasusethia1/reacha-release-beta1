from flask import render_template,flash,url_for,redirect,request
from reacha.forms import RegistrationForm,LoginForm
from reacha.models import User,Post
from reacha import app,bcrypt,db
from flask_login import login_user,current_user,logout_user,login_required
@app.route("/")
def home():
	return render_template('about1.html')


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/Volunteer",methods=['GET','POST'])
def Volunteer():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()

	if form.validate_on_submit():
		username=request.form.get("username")
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		message="Account Created for "+username
		flash(message,'success')
		return redirect(url_for('login'))
	return render_template('volunteer.html',title='Volunteer',form=form)
@app.route("/login",methods=['POST','GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form=LoginForm()
	if form.validate_on_submit():
		
			user=User.query.filter_by(email=form.email.data).first()
			if user and bcrypt.check_password_hash(user.password,form.password.data):
				login_user(user,remember=form.remember.data)
				return redirect(url_for('home'))
			else:
				flash("Invalid Login Credentials","danger")
			return redirect(url_for('login'))
	return render_template('login.html',title="Login",form=form)

@app.route("/success")
def success():
	return render_template("success.html")
@app.route("/logout")
def logout():
	logout_user()
	return redirect ((url_for('home')))
@app.route("/account")
@login_required
def account():
	image_file=url_for('static',filename='profilepictures/'+current_user.image_file)
	return render_template('account.html',title='Account',image_file=image_file)
@app.route("/project/education/villagesports")
def villagesports():
	return render_template("villagesports.html")
@app.route("/project/education/rec")
def rec():
	return render_template("beliefs1.html")
@app.route("/project/education/ndpl")
def ndpl():
	return render_template("beliefs.html")
@app.route("/project/education/tatapowerenergyclub")
def tatapowerenergyclub():
	return render_template("tataproject.html")
@app.route("/project/education/sameerclub")
def sameerclub():
	return render_template("sameerclub.html")
@app.route("/project/education/maitreyaclub")
def maitreyaclub():
	return render_template("maitreyaclubs.html")
@app.route("/project/education/tatatelservices")
def tatatelservices():
	return render_template("tatatelservices.html")
@app.route("/project/livelihood/legenpact")
def legenpact():
	return render_template("legenpact.html")
@app.route("/project/livelihood/musicandculture")
def musicandculture():
	return render_template("cultureandmusic.html")
@app.route("/project/livelihood/drugde")
def drugde():
	return render_template("drugde.html")
@app.route("/project/livelihood/urirehabilation")
def urirehabilation():
	return render_template("urirehabilation.html")
@app.route("/project/livelihood/fashion")
def fashion():
	return render_template("fashion.html")
@app.route("/project/kojo")
def kojo():
	return render_template("kojo.html")
@app.route("/Accreditions")
def accreditions():
	return render_template("stakeholders.html")
@app.route("/Partners")
def partners():
	return render_template("partners.html")
@app.route("/Publications/panditsriramsharma")
def pub1():
	return render_template("Publications.html")
@app.route("/Publications/beingdifferent")
def pub2():
	return render_template("Publications2.html")
@app.route("/Publications/batforallseason")
def pub3():
	return render_template("Publication3.html")
@app.route("/adovacy/toolkit")
def toolkit():
	return render_template("toolkit.html")
@app.route("/test")
def test():
	return render_template("about1.html")
@app.route("/media1")
def test1():
	return render_template("media1.html")
@app.route("/media2")
def media2():
	return render_template("media2.html")
@app.route("/media3")
def media3():
	return render_template("media3.html")
@app.route("/contact/volunteer")
def volunteer():
	return render_template("volunteer.html")
@app.route("/contact/workwithus")
def workwithus():
	return render_template("workwithus.html")
@app.route("/knowledgebank")
def knowledge():
	return render_template("knowledgebank.html")
@app.route("/knowledgebank/garbagemanagement")
def garabagemangement():
	return render_template("garbagemanagement.html")
@app.route("/knowledgebank/actionideas")
def actionideas():
	return render_template("actionideas.html")
@app.route("/contact/engage")
def engage():
	return render_template("engage.html")
@app.route("/contact/partner")
def partner():
	return render_template("partner.html")
@app.route("/contact/connect")
def connect():
	return render_template("contactus.html")
@app.route("/project/designimpactmovement")
def designimpactmovement():
	return render_template("designimpactmovement.html")
@app.route("/covid19")
def covid19():
	return render_template("covid19.html")