from flask import Flask, jsonify, render_template, request, session, redirect
from mysql import connector
from films import getFilms, get_fav_films, get_user_info
from gameCenter import getGames
from utilities import *

# * Default flask project (don't change)
app = Flask(__name__)
app.secret_key = "secret_key"

# * Database connection details
connection = connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="Project"  # was "testingFlask", change if shit fucks up
)

# * sql query wrapper
def dbquery(q, action="select"):
        result = []
        with connection.cursor() as cursor:
                cursor.execute(q)
                if action != "select":
                        connection.commit() # either update or insert
                else:
                        rows = cursor.fetchall()
                        if rows:
                                for r in rows:
                                        result.append(r)
                                return result[0]


# *################################*#


# * Pages the user is gonna visit

@app.route("/", methods=['GET'])
def homeTest():
    return render_template("front.html")
    #
    #result = getGames(connection, cursor)
    #return jsonify(result)


@app.route("/index", methods=['GET'])
# @cross_origin(origin='*', headers=['Content-Type']) # * Only uncomment if you know what you are doing. If you need this..then you're fucked. GL
def home():
    return render_template("index.html")


@app.route("/dashboard", methods=['GET'])
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route("/games", methods=['GET'])
def viewGames():
    return render_template("games.html")


# *################################*#

# * API Pages -- User should usually not go on these sites#
@app.route("/api/login", methods=['POST'])
def dologin():
    email = request.form.get('email')
    result = dbquery(f"SELECT IdUser FROM User where email = \'{email}\'")
    
    if not result:
        message = "User does not exist!"
        return error(message)
    
    session['userid'] = getUserid(email)

    return redirect("/dashboard")
    
    
@app.route("/api/games", methods=['GET'])  # Accepting the methods ['GET'], ['POST', 'GET']
def games():
    if !authenticate(): # TODO: use the following 3 lines of code to prevent access to unauthed users
        message = "401 Unauthenticated" 
        return error(message) 
    result = getGames(connection, cursor)
    return jsonify(result)
    # return render_template("front.html") # * Renders the HTML page


@app.route("/api/films", methods=['GET'])
def films():
    result = getFilms(connection, cursor)
    return jsonify(result)  # * Returns the result is JSON, easier to work with


@app.route("/api/<user>/infos", methods=['GET'])
def user_infos(user):
    result = get_user_info(connection, cursor, user)
    return jsonify(result)


@app.route("/api/<user>/favourite_films", methods=['GET'])
def fav_film(user):
    result = get_fav_films(connection, cursor, user)
    return jsonify(result)


# *################################*#


# * Si le port 5000 ne marche pas, lancer sur port 8000
# if __name__ == "__main__":
#    app.run(port=8000, debug=True)


# * Running the app
app.run(debug=True)
