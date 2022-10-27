from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__,static_folder='styles')

app.config['MYSQL_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin205'
app.config['MYSQL_PASSWORD'] = 'software'
app.config['MYSQL_DB'] = 'mktdata'
mysql = MySQL(app)
mysql.init_app(app)

@app.route('/home')
# ‘/’ URL is bound with hello_world() function.
def home():
    return render_template('index.html')

@app.route('/')
def query():
    cur = mysql.connect.cursor()
    cur.execute("DROP TABLE guitar")
    cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2))")
    cur.execute("INSERT INTO guitar VALUES (123, 'Fender Strat', 499.99)")
    cur.execute("SELECT * FROM guitar")
    data = cur.fetchall()
    return render_template('querytest.html', random_quote = data)

if __name__ == '__main__':

    #runs the simple app
    app.run()
