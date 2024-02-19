from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "uistudents"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route('/')
def home_page():
    cursor.execute('SELECT * FROM enrolledstudents')
    database_info = cursor.fetchall()
    return render_template('home.html', dataz=database_info)


@app.route('/addstudent')
def add_student_page():
    return render_template('addStudent.html') 

@app.route('/success', methods=["POST"])
def success_page():
    namez = request.form['student_name']
    cursor.execute("INSERT INTO enrolledstudents (name) VALUES (%s)", namez)
    conn.commit()
    return render_template('success.html', added_student=namez)

@app.route('/about')
def about_page():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)
