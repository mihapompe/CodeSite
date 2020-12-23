import bottle
import model

@bottle.get("/")
def main_page():
    return "Got my new website up and running!"

bottle.run(debug = True, reloader= True)