'''
Some flask starter code, will need to do more research...
'''

from flask import Flask, render_template, request, url_for, flash, redirect
from db import Db

#app creation
app = Flask(__name__)

app = Flask(__name__, static_folder='instance/static')

app.config.from_object('config')
#route tells us how to use the url
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'




@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page """
    # return render_template('home.html',
    #                        title="Home Page",
    #                        heading="Home Page",
    #                        show=display)


@app.route("/welcome", methods = ['GET', 'POST'])
def welcome():
    # """welcome page"""
    #  return render_template('welcome.html',
    #                            title="Customer Welcome",
    #                            heading="Customer Welcome")

@app.route("/transactions", methods=['GET', 'POST'])
def transactions():
    # search_term = ''
    # if request.method == 'POST':
    #     search_term = request.form.get('search_term')
    #     q = sql_injection.create_search_query(1234, search_term)
    # else:
    #     q = 'SELECT * FROM trnsaction WHERE trnsaction.account_id = 1234'
    # cnx = Db.get_connection()
    # c = Db.execute_query(cnx, q)
    # rows = c.fetchall()
    # return render_template('transactions.html',
                           # search_term=search_term,
                           # rows=rows,
                           # query=q,
                           # title="My Transactions",
                           # heading="My Transactions")


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Login the user. TODO """
    #
    # with open(app.config['CREDENTIALS_FILE']) as fh:
    #     reader = csv.DictReader(fh)
    #     credentials = {row['username']:
    #                        {'acct_id': row['id'],
    #                         'pw_hash': row['password_hash']}
    #                    for row in reader}
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     pw_hash = hash_pw(password)
    #     try:
    #         if credentials[username]['pw_hash'] == pw_hash:
    #             return redirect(url_for('login_success',
    #                                     id_=credentials[username]['acct_id']))
    #     except KeyError:
    #         pass
    #     flash("Invalid username or password!", 'alert-danger')
    return render_template('login.html',
                           title="Secure Login",
                           heading="Secure Login")


@app.route("/login_success/<int:id_>", methods=['GET', ])
def login_success(id_):
    flash("Welcome! You have logged in!", 'alert-success')
    return render_template('customer_home.html',
                           title="Customer Home",
                           heading="Customer Home")



# main driver function
if __name__ == '__main__':

    #runs the simple app
    app.run()