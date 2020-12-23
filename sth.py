from flask import Flask, render_template, request, url_for
import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pokemonsword1#'
app.config['MYSQL_DB'] = 'giraffe'

mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        tasks = request.form['todo']
        cur = mysql.connection.cursor()
        cur.execute(f'INSERT into myusers(task, date_inserted) Values (%s, %s)', (tasks, datetime.date.today()))
        mysql.connection.commit()
        cur.execute("SELECT * FROM myusers")
        myresult = cur.fetchall()
        cur.close()
        return render_template('index.html', result=myresult)
    return render_template('index.html')


app.run(debug=True)
