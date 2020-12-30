import bottle
from  model import *


@bottle.get("/")
def main_page():
    return bottle.template("views/modules.tpl", namer="Miha")

@bottle.get('/login') # or @route('/login')
def login():
    return '''
        
    '''

@bottle.post('/login') # or @route('/login', method='POST')
def do_login():
    username = bottle.request.forms.get('username')
    password = bottle.request.forms.get('password')
    if check_login(username, password):
        return main_page()#"<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

#Cookies
# setting a cookie - bottle.response.set_cookie("name of the cookie", value)
# check cookie - bottle.request.get_cookie("name of the cookie")






bottle.run(debug = True, reloader= True)
