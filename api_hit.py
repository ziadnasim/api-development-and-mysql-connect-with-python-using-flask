from flask import request
import pymysql
import flask
import json
from flask import jsonify
import pymysql.cursors

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/locations', methods=['GET'])
def home1():
    #conn = pymysql.connect(host="64.188.2.228", user="odvutcom_apiTest", passwd="remoteTest123!@#", db="odvutcom_apiTest")
    #conn = pymysql.connect(host="64.188.2.228", user="odvutcom_apiTest", passwd="remoteTest123!@#", db="odvutcom_apiTest")
    #conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd",db="u9PE2LncVJ")
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="api",charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donation")
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

@app.route('/add_location', methods=['POST'])
def add_loc():
    #conn = pymysql.connect(host="64.188.2.228", user="odvutcom_apiTest", passwd="remoteTest123!@#", db="odvutcom_apiTest")
    ##conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd",db="u9PE2LncVJ")
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="api", charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    myCursor = conn.cursor()
    d_name = request.form['name']
    d_loc = request.form['location']
    d_area = request.form['donation_address']
    d_count = request.form['donation_count']
    d_amt = request.form['donation_amount']
    d_thana = request.form['thana']
    d_lat = request.form['lat']
    d_longx = request.form['longx']
    myCursor.execute(
        "INSERT INTO donation (name, location, donation_address, donation_count, donation_amt, thana, lat, longx) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (d_name, d_loc, d_area, int(d_count), float(d_amt), d_thana, float(d_lat), float(d_longx)))
    conn.commit()
    conn.close()
    return d_name

app.run()