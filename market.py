'''
Some flask starter code, will need to do more research...
'''


from flask import Flask

#app creation
app = Flask(__name__)


#route tells us how to use the url
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


# main driver function
if __name__ == '__main__':

    #runs the simple app
    app.run()