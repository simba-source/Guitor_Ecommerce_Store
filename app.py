'''
Some flask starter code, will need to do more research...
'''

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# app = Flask(__name__, static_folder='static')
app.config['MYSQL_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin205'
app.config['MYSQL_PASSWORD'] = 'software'
app.config['MYSQL_DB'] = 'mktdata'
mysql = MySQL(app)

@app.route('/form')
# ‘/’ URL is bound with hello_world() function.
def form():
    return render_template('form.html')
# def login():
#     cur = mysql.conection.cursor()
#     # cur.execute("DROP TABLE guitar")
#     # cur.execute("CREATE TABLE guitar(ID INT, Name VARCHAR(150), Price DECIMAL(7, 2))")
#     cur.execute("INSERT INTO guitar VALUES (123, 'Fender Strat', 499.99)")
#     # cur.execute("SELECT * FROM guitar")
#     mysql.connection.commit()
#     cur.close()
#     return cur.fetchall()

#
# @app.route("/home", methods=['GET', 'POST'])
# def home():
#     """Home page """
#     return render_template('home.html',
#                            title="Home Page",
#                            heading="Home Page",
#                            show=display)
#
# @app.route("/shop", methods=['GET', 'POST'])
# def home():
#     """Home page """
#     return render_template('shop.html',
#                            title="Shop",
#                            heading="Shop",
#                            show=display)
#
#
# @app.route("/transactions", methods=['GET', 'POST'])
# def transactions():
#     # search_term = ''
#     # if request.method == 'POST':
#     #     search_term = request.form.get('search_term')
#     #     q = sql_injection.create_search_query(1234, search_term)
#     # else:
#     #     q = 'SELECT * FROM trnsaction WHERE trnsaction.account_id = 1234'
#     # cnx = Db.get_connection()
#     # c = Db.execute_query(cnx, q)
#     # rows = c.fetchall()
#     # return render_template('transactions.html',
#                            # search_term=search_term,
#                            # rows=rows,
#                            # query=q,
#                            # title="My Transactions",
#                            # heading="My Transactions")
#
#
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     """Login the user. """
#     #
#     # with open(app.config['CREDENTIALS_FILE']) as fh:
#     #     reader = csv.DictReader(fh)
#     #     credentials = {row['username']:
#     #                        {'acct_id': row['id'],
#     #                         'pw_hash': row['password_hash']}
#     #                    for row in reader}
#     # if request.method == 'POST':
#     #     username = request.form.get('username')
#     #     password = request.form.get('password')
#     #     pw_hash = hash_pw(password)
#     #     try:
#     #         if credentials[username]['pw_hash'] == pw_hash:
#     #             return redirect(url_for('login_success',
#     #                                     id_=credentials[username]['acct_id']))
#     #     except KeyError:
#     #         pass
#     #     flash("Invalid username or password!", 'alert-danger')
#     # return render_template('login.html',
#     #                        title="Secure Login",
#     #                        heading="Secure Login")
#
#
# @app.route("/login_success/<int:id_>", methods=['GET', ])
# def login_success(id_):
#     flash("Welcome! You have logged in!", 'alert-success')
#     return render_template('customer_home.html',
#                            title="Customer Home",
#                            heading="Customer Home")
#
#
# # @app.route('/')
# # @app.route('/login', methods =['GET', 'POST'])
# # def login():
# #     msg = ''
# #     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
# #         username = request.form['username']
# #         password = request.form['password']
# #         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# #         cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
# #         account = cursor.fetchone()
# #         if account:
# #             session['loggedin'] = True
# #             session['id'] = account['id']
# #             session['username'] = account['username']
# #             msg = 'Logged in successfully !'
# #             return render_template('index.html', msg = msg)
# #         else:
# #             msg = 'Incorrect username / password !'
# #     return render_template('login.html', msg = msg)
# #
# #
# # @app.route('/logout')
# # def logout():
# #     session.pop('loggedin', None)
# #     session.pop('id', None)
# #     session.pop('username', None)
# #     return redirect(url_for('login'))
#

app.run(host = 'local', port=5000)