from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
import random

app = Flask(__name__, static_folder='styles')

app.config['MYSQL_DATABASE_HOST'] = 'final-db-205.cwokmtfympzg.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin205'
app.config['MYSQL_DATABASE_PASSWORD'] = 'software'
app.config['MYSQL_DATABASE_DB'] = 'mktdata'
mysql = MySQL(app)
mysql.init_app(app)

rand_list = []   #for id generation

# User class to store information about active user
class User:
    def __init__(self, is_logged_in, id):
        self.is_logged_in = is_logged_in
        self.id = id


# create global instance of class for client
active_user = User(False, None)

#initialize data in DB
def data():
    cur = mysql.get_db().cursor()
    cur.execute("DROP TABLE CART_ITEM")
    cur.execute("DROP TABLE CART")
    cur.execute("DROP TABLE GUITAR")
    cur.execute("DROP TABLE COMPANY")
    cur.execute("DROP TABLE USER")
    cur.execute("CREATE TABLE COMPANY(ID INT, Name VARCHAR(150), PRIMARY KEY (ID))")
    cur.execute(
        "CREATE TABLE GUITAR(ID INT, Name VARCHAR(150), Picture VARCHAR(150), Description VARCHAR(150), Price DECIMAL(7, 2), companyID INT, PRIMARY KEY (ID),FOREIGN KEY (companyID) REFERENCES COMPANY(ID))")
    cur.execute(
        "CREATE TABLE USER(ID INT, FName VARCHAR(150), LName VARCHAR(150), Username VARCHAR(150), Password VARCHAR(150), Balance DECIMAL(7,2), PRIMARY KEY (ID))")
    cur.execute(
        "CREATE TABLE CART(ID INT NOT NULL, User_ID INT, Date_made DATE, PRIMARY KEY (ID), FOREIGN KEY (User_ID) REFERENCES USER(ID))")
    cur.execute(
        "CREATE TABLE CART_ITEM(ID INT NOT NULL, Item_ID INT, Quantity INT, Date_made DATE, Cart_ID INT, PRIMARY KEY (ID), FOREIGN KEY (Item_ID) REFERENCES GUITAR(ID), FOREIGN KEY (Cart_ID) REFERENCES CART(ID))")

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

#login page
@app.route('/login', methods=['GET', 'POST'])
@app.route('/templates/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

#check login function
@app.route('/checklogin', methods=['GET', 'POST'])
def checklogin():
    # query for username and password from USERS
    # if credentials pass, render index
    # else if username doesn't exist

    if request.method == "POST":
        # getting input from name tag HTML form
        username = request.form.get("name")
        password = request.form.get("password")
        cur = mysql.get_db().cursor()
        try:
            cur.execute("SELECT Username, Password FROM USER WHERE Username = %s AND Password = %s",
                        (username, password))

            if not cur.fetchone():
                # invalid login - notify user
                error_message = "Invalid credentials. Try again or register to proceed."
                return render_template('login.html', message=error_message)
            else:
                # successful login - get id and update active_user
                cur.execute("SELECT ID FROM USER WHERE Username = %s", (username))
                id_for_active_user = cur.fetchall()
                # print("id for active user follows: ")
                # print(id_for_active_user[0][0])

                active_user.is_logged_in = True
                active_user.id = id_for_active_user

                return render_template('index.html')

        except:
            print('doesnt exist')

    return render_template('login.html')

#register page
@app.route('/register', methods=['GET', 'POST'])
@app.route('/templates/register.html', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

#register user
@app.route('/registeruser', methods=['GET', 'POST'])
def registeruser():
    if request.method == "POST":
        # getting input from name tag HTML form
        username = request.form.get("name")
        password = request.form.get("password")
        cur = mysql.get_db().cursor()
        cur.execute("SELECT * FROM CART")
        print(cur.fetchall())
        try:
            # get the last userid
            cur.execute("SELECT ID FROM USER")
            last_id = cur.fetchall()
            for i in last_id:
                final_id = int(i[-1]) + 1
            print(final_id)

            # see if new username is in the db already
            cur.execute("SELECT Username FROM USER WHERE Username = %s", username)
            if not cur.fetchone():
                # username is unique - create account
                print('not in db')
                cur.execute("INSERT INTO USER (Username,Password, ID) VALUES (%s, %s, %s)",
                            (username, password, final_id))
                cur.execute("INSERT INTO CART (ID,User_ID) VALUES (%s, %s)", (final_id, final_id))

                # commit change to database
                mysql.get_db().commit()

                # update active_user
                active_user.is_logged_in = True
                active_user.id = final_id

                account_created_message = "Account has been saved. "
                return render_template('index.html', message=account_created_message)
            else:
                # username is already in database
                print('in DB')
                failed_to_register = "Username already exists in databse. Enter new username or log in"
                return render_template('register.html', message=failed_to_register)
        except Exception:
            print('error')
            error_message = "Error"
            return render_template('register.html', message=error_message)

    # query to make sure username doesn't already exist
    # if username does not already exist, place new username and pass into database, redirect to index
    # if it does exist
    return render_template('index.html')

#origin page
@app.route('/', methods=['GET', 'POST'])
@app.route('/templates/index.html', methods=['GET', 'POST'])
def origin():
    # data()
    # check if user is logged in. if so, direct to index, if not, redirect to login
    return render_template('index.html')


# we should move this code to a new function getProduct()
@app.route('/shop', methods=['GET', 'POST'])
@app.route('/templates/shop.html', methods=['GET', 'POST'])
def shop():
    cur = mysql.get_db().cursor()

    cur.execute("SELECT ID, Name, Price, Picture FROM GUITAR")
    products = cur.fetchall()

    # nested dictionary. Outer for each product, inner for products' keys and values
    products_dictionary = {}
    item_index = 1
    i = 0
    for elem in products:
        products_dictionary.update({
            item_index: {'id': products[i][0], 'title': products[i][1], 'price': products[i][2],
                         'image': products[i][3]}
        })
        item_index += 1
        i += 1

    return render_template('shop.html', products=products_dictionary)

#search for product
@app.route('/search', methods=['GET', 'POST'])
def search_product():
    if request.method == "POST":
        # getting input from name tag HTML form
        search_query = request.form.get("searchQuery")

        # initialize mysql cursor
        cur = mysql.get_db().cursor()

        try:
            # query for all guitar names
            cur.execute("SELECT Name FROM GUITAR")
            product_names = cur.fetchall()

            #save all product names to a list
            guitar_names_list = []
            for name in product_names:
                guitar_names_list.append(name[0])

            # use python find method to find all guitar names with substring of search_query
            guitar_names_list_found = []
            for name in guitar_names_list:
                if name.find(search_query) != -1: #find() returns -1 if value is not found
                    guitar_names_list_found.append(name)

            # nested dictionary. Outer for each product, inner for products' keys and values
            products_dictionary = {}
            item_index = 1

            if not guitar_names_list_found:
                # no guitars match search
                empty_result = "No results found for your search. Please try again or browse all products. "
                return render_template('shop.html', products=products_dictionary, active_search=search_query, no_result=empty_result)
            else:
                # search found at least one guitar - display relevant product(s)
                for guitar_name in guitar_names_list_found:
                    cur.execute("SELECT ID, Name, Price, Picture FROM GUITAR WHERE Name = %s", (guitar_name))
                    current_guitar_info = cur.fetchall()

                    products_dictionary.update({
                        item_index: {'id': current_guitar_info[0][0], 'title': current_guitar_info[0][1],
                                     'price': current_guitar_info[0][2], 'image': current_guitar_info[0][3]}
                    })
                    item_index += 1

                return render_template('shop.html', products=products_dictionary, active_search=search_query)

        except:
            error_message = "Invalid Search. "
            return render_template('index.html', message=error_message)

    return render_template('index.html')

#load product page
@app.route('/loadproduct', methods=['GET', 'POST'])
def load_product_page():
    product_id = request.args.get('id')

    cur = mysql.get_db().cursor()
    cur.execute('SELECT ID, Name, Price, Picture, Description FROM GUITAR WHERE ID = "{}"'.format(product_id))
    product = cur.fetchall()

    product_dictionary = {'id': product[0][0], 'title': product[0][1], 'price': product[0][2],
                          'image': product[0][3], 'desc': product[0][4]}

    return render_template('product.html', product=product_dictionary)

#product page
@app.route('/product', methods=['GET', 'POST'])
@app.route('/templates/product.html', methods=['GET', 'POST'])
def product():
    return render_template('product.html')

#cart functionality
@app.route('/cart', methods=['GET', 'POST'])
@app.route('/templates/cart.html', methods=['GET', 'POST'])
def cart():
    # initialize mysql cursor
    cur = mysql.get_db().cursor()

    # check if user is logged in
    if not active_user.is_logged_in:
        # user is not logged in, redirect to previous page
        error_message = "Please log in to view your cart"
        # return redirect(request.referrer)
        return render_template('index.html', message=error_message)

    # query for all the items in cart
    cur.execute("SELECT Item_ID, CART_ITEM.ID FROM CART_ITEM JOIN CART ON CART.ID = CART_ID WHERE CART.User_ID = %s",
                (active_user.id))

    items = cur.fetchall()

    # nested dictionary. Outer for each product, inner for products' keys and values
    cart_items_dictionary = {}
    item_index = 1
    i = 0

    for item in items:
        # query for guitar using item_id
        cur.execute("SELECT * FROM GUITAR WHERE ID  = (%s)", (item[0]))
        guitar = cur.fetchall()

        cart_items_dictionary.update({
            item_index: {'id': guitar[0][0], 'title': guitar[0][1], 'image': guitar[0][2], 'price': guitar[0][4],
                         'cart_item_id': items[i][1]}
        })
        item_index += 1
        i += 1

    # get total cart price
    total_price = 0
    i = 1
    while i <= len(cart_items_dictionary):
        total_price = total_price + cart_items_dictionary[i]['price']
        i += 1

    return render_template('cart.html', items=cart_items_dictionary, subtotal=total_price)

#add item to cart
@app.route('/addtocart', methods=['GET', 'POST'])
def add_to_cart():
    product_id = request.args.get('product_id')

    # check if user is logged in
    if not active_user.is_logged_in:
        # user is not logged in, redirect to previous page
        error_message = "You need to be logged in to add to cart"
        # return redirect(request.referrer)
        return render_template('index.html', message=error_message)

    # user is logged in
    # initialize mysql cursor
    cur = mysql.get_db().cursor()

    # generate new id
    cur.execute("SELECT ID FROM USER")
    last_id = cur.fetchall()
    for i in last_id:
        final_id = int(i[-1])

    # check if user has cart
    cur.execute('SELECT * FROM CART WHERE User_ID = (%s)', (active_user.id))
    if not cur.fetchone():
        # user does not have cart. create cart for user
        cur.execute('SELECT * FROM CART WHERE ID = (%s)', final_id)
        if not cur.fetchone():
            print('user has no cart')
            cur.execute("INSERT INTO CART (ID,User_ID) VALUES (%s, %s)", (final_id, active_user.id))

    # cart exists - add item to cart
    else:

        final_id2 = random.randint(0, 100000000)
        if final_id2 in rand_list:
            final_id2 = random.randint(0, 100000000)
        else:
            rand_list.append(final_id2)

        # check to make sure it isn't in table
        cur.execute('SELECT * FROM CART_ITEM WHERE ID = (%s)', (final_id2))
        if not cur.fetchone():
            cur.execute("INSERT INTO CART_ITEM (ID, Item_ID, Quantity, Cart_ID) VALUES (%s, %s, %s, %s)",
                        (final_id2, product_id, 1, active_user.id))

        else:
            print('already in table')

    mysql.get_db().commit()
    added_to_cart_message = "Item has been added to cart. "
    return render_template('index.html', message=added_to_cart_message)

#remove item from cart function
@app.route('/removefromcart', methods=['GET', 'POST'])
def remove_from_cart():
    # get product id from url param
    cart_item_id = request.args.get('cart_item_id')

    # initialize mysql cursor
    cur = mysql.get_db().cursor()

    # remove cart_item from user's cart
    cur.execute('DELETE FROM CART_ITEM WHERE CART_ITEM.ID = (%s)', (cart_item_id))

    # commit change to database
    mysql.get_db().commit()

    removed_successfully_message = "Item has been removed from cart. "
    #print(removed_successfully_message)

    #because this is a POST, we want to use redirect
    return redirect('cart')
    #return render_template('cart.html', message=removed_successfully_message)

#about page
@app.route('/templates/about.html', methods=['GET', 'POST'])
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

#purchase page
@app.route('/templates/order_placed.html', methods=['GET', 'POST'])
def final_purchase():
    return render_template('order_placed.html')

#purchased page
#@app.route('/templates/purchased.html', methods=['GET', 'POST'])
@app.route('/purchased', methods=['GET', 'POST'])
def purchased():
    price = request.args.get('price')

    # initialize mysql cursor
    cur = mysql.get_db().cursor()

    # query to check if any items are in user's cart before rendering purchased page
    cur.execute("SELECT Item_ID, CART_ITEM.ID FROM CART_ITEM JOIN CART ON CART.ID = CART_ID WHERE CART.User_ID = %s",
                (active_user.id))

    has_cart_item = cur.fetchone()

    if has_cart_item:
        # at least one item in cart
        return render_template('purchased.html', price=price)

    else:
        # no items in cart
        error_message = "No Items in Cart"
        return render_template('cart.html', message=error_message)

#for testing
@app.route('/query', methods=['GET', 'POST'])
def query():
    cur = mysql.get_db().cursor()
    # cur.execute("SELECT Name FROM GUITAR")
    # Name = cur.fetchall()
    # cur.execute("SELECT Price FROM GUITAR")
    # Price = cur.fetchone()
    # cur.execute("SELECT Description FROM GUITAR")
    # Desc = cur.fetchall()
    # cur.execute("SELECT * FROM CART_ITEM JOIN CART ON CART.ID = CART_ID WHERE CART.User_ID = %s", (123456809))
    cur.execute("SELECT * FROM CART_ITEM")
    print(cur.fetchall())
    cur.execute("SELECT * FROM CART")
    print(cur.fetchall())

    # cur.execute("SELECT ID FROM USER")
    # last_id = cur.fetchall()
    # for i in last_id:
    #     final_id = int(i[-1]) + 1
    # print(final_id)

    # generate new id
    # cur.execute("SELECT ID FROM USER")
    # last_id = cur.fetchall()
    # for i in last_id:
    #     final_id = int(i[-1])
    # print(final_id)

    print(cur.fetchall())
    # cur.execute("SELECT * FROM CART_ITEM")
    # print(cur.fetchall())
    # for i in Price:
    #     print(i)
    return render_template('querytest.html')  # , random_quote=Desc)


# routing for 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="Not Found")


if __name__ == '__main__':
    # runs the simple app
    app.run()
