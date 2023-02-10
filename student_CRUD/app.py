from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///student.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Student(db.Model):
    enrollNo=db.Column(db.String,primary_key=True)
    name=db.Column(db.String,nullable=False)
    year=db.Column(db.String)
    semester=db.Column(db.String)
    previousPercent=db.Column(db.String)
    address=db.Column(db.String)
    def __repr__(self) -> str:
        return f"{self.enrollNo}-{self.name}"
app.app_context().push()
@app.route("/",methods=['POST','GET'])
def home():
    if request.method=="POST":
       return homePost()
    return render_template("index.html")
def homePost():
    enrollNo=request.form["Enroll"]
    name=request.form["Name"]
    year=request.form["Year"]
    semester=request.form["Semester"]
    previousPercent=request.form["Percent"]
    address=request.form["Address"]
    student=Student(enrollNo=enrollNo,name=name,year=year,semester=semester,previousPercent=previousPercent,address=address)
    db.session.add(student)
    db.session.commit()
    return render_template("index.html")
@app.route("/manageStudent")
def manage():
    students=Student.query.all()
    print(students)
    return render_template("manageStudent.html",students=students)
@app.route('/delete/<string:enrollNo>')
def delete(enrollNo):
    student=Student.query.filter_by(enrollNo=enrollNo).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/manageStudent")
@app.route('/update/<string:enrollNo>',methods=['POST','GET'])
def update(enrollNo):
    if request.method=='GET':
        return getUpdate(enrollNo)
    else:
        return postUpdate(enrollNo)
def getUpdate(enrollNo):
     student=Student.query.filter_by(enrollNo=enrollNo).first()
     return render_template('update.html',student=student)
def postUpdate(enrollNo):
    name=request.form["Name"]
    year=request.form["Year"]
    semester=request.form["Semester"]
    previousPercent=request.form["Percent"]
    address=request.form["Address"]
    student=Student.query.filter_by(enrollNo=enrollNo).first()
    student.name=name
    student.year=year
    student.semester=semester
    student.previousPercent=previousPercent
    student.address=address
    db.session.add(student)
    db.session.commit()
    return redirect("/manageStudent")

if __name__=="__main__":
    app.run(debug=True,host="localhost",port="3000")