from flask import Flask, jsonify, render_template, redirect, session, request
from utilities import *
from gameCenter import *

# * Default flask project (don't change)
app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SESSION_TYPE'] = 'filesystem'

#TODO Repplace the front.html with index.html or just remove this route
@app.route("/", methods=['GET'])
def homeTest():
    return render_template("front.html")
    #
	# result = getGames(connection, cursor)
	# return jsonify(result)


@app.route("/index", methods=['GET'])
# @cross_origin(origin='*', headers=['Content-Type']) # * Only uncomment if you know what you are doing. If you need this..then you're fucked. GL
def home():
    return render_template("index.html")


@app.route("/dashboard", methods=['GET'])
def dashboard():
    if not authenticate(session):
        message = "401 Unauthenticated"
        return error(message)
    return render_template("dashboard.html", username=getUsername(session['userid']))

@app.route("/profile", methods = ['POST','GET'])
def profile():
    return render_template("profile.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template("login.html")

#
@app.route("/games", methods=['GET'])
def viewGames():
    return render_template("games.html")


@app.route("/all-games", methods=['GET'])
def viewAllGames():
    return render_template("games.html")




# *################################*#

# * API Pages -- User should usually not go on these sites#
@app.route("/api/login", methods=['POST'])
def dologin():
    email = request.form.get('email')
    userid = getUserid(email)

    if not userid:
        message = "User does not exist!"
        return error(message,"/login")

    setWebSession(session, userid)

    return redirect("/dashboard")

@app.route("/api/logout", methods=['GET'])
def dologout():
	unsetWebSession(session)
	return redirect("/login")

@app.route("/api/all-games", methods=['GET'])  # Accepting the methods ['GET'], ['POST', 'GET']
def games():
    result = getAllGames(connection, cursor)
    return jsonify(result)


# return render_template("front.html") # * Renders the HTML page


@app.route("/api/<user>/infos", methods=['GET'])
def user_infos(user):
    if not authenticate(session):
        message = "401 Unauthenticated"
        return error(message)
    return ""


# *################################*#


# * Si le port 5000 ne marche pas, lancer sur port 8000
# if __name__ == "__main__":
#    app.run(port=8000, debug=True)


# * Running the app
app.run(debug=True)

