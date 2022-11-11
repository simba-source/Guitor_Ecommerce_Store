from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder='styles')

app.config['MYSQL_DATABASE_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin205'
app.config['MYSQL_DATABASE_PASSWORD'] = 'software'
app.config['MYSQL_DATABASE_DB'] = 'mktdata'
mysql = MySQL(app)
mysql.init_app(app)

def data():
    cur = mysql.get_db().cursor()
    # cur.execute("DROP TABLE GUITAR")
    # cur.execute("DROP TABLE COMPANY")
    # cur.execute("DROP TABLE USER")
    cur.execute("CREATE TABLE COMPANY(ID INT, Name VARCHAR(150), PRIMARY KEY (ID))")
    cur.execute("CREATE TABLE GUITAR(ID INT, Name VARCHAR(150), Picture VARCHAR(150), Description VARCHAR(150), Price DECIMAL(7, 2), companyID INT, PRIMARY KEY (ID),FOREIGN KEY (companyID) REFERENCES COMPANY(ID))")
    cur.execute("CREATE TABLE USER(ID INT, FName VARCHAR(150), LName VARCHAR(150), Username VARCHAR(150), Password VARCHAR(150), Balance DECIMAL(7,2), PRIMARY KEY (ID))")
    # cur.execute("CREATE TABLE PURCHASE(ID INT, User_ID INT, User_balance DECIMAL(7,2), Item_ID INT, PRIMARY KEY (ID))")

    fd = open('SQL/start_data.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for i in sqlCommands:
        i = i.strip('\n')
        try:
            cur.execute(i)
            print(i)
            # print(i)
        except:
            print("")
    mysql.get_db().commit()
    cur.close()

@app.route('/login', methods=['GET', 'POST'])
@app.route('/templates/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
@app.route('/templates/register.html', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
@app.route('/templates/index.html', methods=['GET', 'POST'])
def origin():
    # data()
    #check if user is logged in. if so, direct to index, if not, redirect to login
    return render_template('index.html')

#we should move this code to a new function getProduct()
@app.route('/shop', methods=['GET', 'POST'])
@app.route('/templates/shop.html', methods=['GET', 'POST'])
def shop():
    cur = mysql.get_db().cursor()

    cur.execute("SELECT Name, Price, Picture FROM GUITAR")
    products = cur.fetchall()

    #nested dictionary. Outer for each product, inner for products' keys and values
    products_dictionary = {}
    item_index = 1
    i = 0
    for elem in products:
       products_dictionary.update({
           item_index: {'title': products[i][0], 'price': products[i][1], 'image': products[i][2]}
        })
       item_index += 1
       i += 1

    #print(products_dictionary)
    return render_template('shop.html', products = products_dictionary)

@app.route('/loadproduct', methods=['GET', 'POST'])
def load_product_page():
    print('loadproduct ran')
    return redirect('product.html')

@app.route('/templates/product.html', methods=['GET', 'POST'])
def product():
    return render_template('product.html')

@app.route('/templates/contact.html', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/templates/cart.html', methods=['GET', 'POST'])
def cart():
    # cur = mysql.connect.cursor()
    # cur.execute("SELECT * FROM PURCHASE")
    # data = cur.fetchall()
    return render_template('cart.html') #, variable = data


@app.route('/templates/about.html', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/templates/purchased.html', methods=['GET', 'POST'])
def purchase():
    #query to check if any items are in user's cart before rendering purchased page
    return render_template('purchased.html')

@app.route('/product.html', methods=['GET', 'POST'])
def product2():
    return render_template('purchased.html')

@app.route('/query', methods=['GET', 'POST'])
def query():
    cur = mysql.get_db().cursor()
    cur.execute("SELECT Name FROM GUITAR")
    Name = cur.fetchall()
    cur.execute("SELECT Price FROM GUITAR")
    Price = cur.fetchone()
    cur.execute("SELECT Description FROM GUITAR")
    Desc = cur.fetchall()
    for i in Price:
        print(i)
    return render_template('querytest.html', random_quote=Desc)


if __name__ == '__main__':
    # runs the simple app
    app.run()
