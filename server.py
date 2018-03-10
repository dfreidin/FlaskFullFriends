from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriends')
@app.route('/')
def index():
    query = "SELECT CONCAT(first_name, ' ', last_name) AS name, age, DATE_FORMAT(friend_since, '%b %D') as since_month, year(friend_since) as since_year from friends;"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route("/add_friend", methods=["POST"])
def addFriend():
    query = "INSERT INTO friends (first_name, last_name, age, friend_since, created_at, updated_at) values('{}', '{}', {}, now(), now(), now());".format(request.form["first_name"], request.form["last_name"], request.form["age"])
    mysql.query_db(query)
    return redirect("/")
app.run(debug=True)