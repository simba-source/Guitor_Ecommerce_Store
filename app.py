from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__,static_folder='styles')

app.config['MYSQL_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin205'
app.config['MYSQL_PASSWORD'] = 'software'
app.config['MYSQL_DB'] = 'mktdata'
mysql = MySQL(app)
mysql.init_app(app)

@app.route('/',methods = ['GET','POST'])
def origin():
    return render_template('index.html')

@app.route('/templates/index.html', methods = ['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/templates/shop.html', methods = ['GET','POST'])
def shop():
    return render_template('shop.html')

@app.route('/templates/contact.html', methods = ['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/templates/cart.html', methods = ['GET','POST'])
def cart():
    return render_template('cart.html')

@app.route('/templates/about.html', methods = ['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/templates/product.html', methods = ['GET','POST'])
def product():
    return render_template('product.html')

@app.route('/templates/purchased.html', methods = ['GET','POST'])
def purchase():
    return render_template('purchased.html')

@app.route('/query', methods = ['GET', 'POST'])
def query():
    cur = mysql.connect.cursor()
    cur.execute("DROP TABLE guitar")
    cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2))")
    cur.execute("INSERT INTO guitar VALUES (123, 'Fender Strat', 499.99)")
    cur.execute("SELECT Name FROM guitar")
    data = cur.fetchall()
    return render_template('querytest.html', random_quote = data)

if __name__ == '__main__':

    #runs the simple app
    app.run()
