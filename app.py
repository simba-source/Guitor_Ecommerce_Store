'''
Some flask starter code, will need to do more research...
'''

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin205'
app.config['MYSQL_PASSWORD'] = 'software'
app.config['MYSQL_DB'] = 'mktdata'
mysql = MySQL(app)
mysql.init_app(app)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def form():
    # # return render_template('form.html')
    cur = mysql.connect.cursor()
    cur.execute("DROP TABLE guitar")
    cur.execute("DROP TABLE company")
    cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2), companyID INT)")
    cur.execute("CREATE TABLE company(ID INT, Name VARCHAR(150))")

    fd = open('SQL/start_data.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for i in sqlCommands:
        i = i.strip('\n')
        try:
            cur.execute(i)
            print(i)
        except:
            print('error')
    cur.execute("SELECT Name FROM company WHERE ID = 47350")
    data = cur.fetchone()[0]
    return render_template('custom.html', random_quote = data)

@app.route('/home')
def home():
    return render_template('test.html')
# @app.route('/login')
# def login():
#     cur = mysql.conection.cursor()
#     # cur.execute("DROP TABLE guitar")
#     # cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2))")
#     # cur.execute("SELECT * FROM guitar")
#     mysql.connection.commit()
#     cur.close()
#     return cur.fetchall
# main driver function
if __name__ == '__main__':

    #runs the simple app
    app.run()

