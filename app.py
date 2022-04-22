from flask import Flask, render_template, request
import pandas as pd
#import urllib.request
#import ssl
#from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL
#import yaml
#from mysql.connector import connect
#import pymysql as MySQLdb

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
          host='db-mysql-sfo3-20178-do-user-11403836-0.b.db.ondigitalocean.com',
          user='doadmin',
          passwd='AVNS_3EuOgzTGRE8VBAk',
          database='defaultdb',
          #auth_plugin='mysql_native_password',
          port='25060')       

@app.route('/')
def hello():
    print("Welcome to movie rating app guys")
    return 'Hello you can change route: /movies for entering rating or /rating to view ratings or /table to see moviedata'

@app.route('/table')
def table():
    data = pd.read_csv('Movie_rating.csv')
    return render_template('moviedata.html', tables=[data.to_html()], titles=[''])
  

@app.route("/movies", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        userDetails = request.form
        member_id = userDetails['member_id']
        name = userDetails['name']
        rating = userDetails['rating']
        movie_name = userDetails['movie_name']
        #email = userDetails['email']
        cur = mydb.cursor(buffered=True)
        #cur = mysql.connection.cursor()
        #cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO members(member_id, name, rating, movie_name) VALUES(%s, %s, %s, %s)", (member_id,name,rating,movie_name))
        #mysql.connection.commit()
        mydb.commit()
        cur.close
        return 'success'
    return render_template('index.html')

@app.route("/rating")
def rating():  
        cur = mydb.cursor(buffered=True)
        cur.execute("select * from members")
        ratingdetails = cur.fetchall()
        return render_template('rating.html',ratingdetails=ratingdetails)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000 ,debug=True)
