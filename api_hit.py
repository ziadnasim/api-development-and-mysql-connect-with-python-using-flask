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
    return "<h1>The Crazy Ones</h1><p>This site is a prototype API by The Crazy Ones.</p>"

@app.route('/locations', methods=['GET'])
def home1():
    conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd", db="u9PE2LncVJ")
    myCursor = conn.cursor()
    myCursor.execute('select * from donation')
    result = myCursor.fetchall()

    data = []
    for item in result:
        entry = {
            'name': item[1],
            'location': item[2],
            'donation_address': item[3],
            'donation_count': item[4],
            'donation_amt': item[5],
            'thana': item[6],
            'lat': item[7],
            'longx': item[8]
        }
        data.append(entry)
    return jsonify(data)

@app.route('/add_location', methods=['POST'])
def add_loc():
    conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd", db="u9PE2LncVJ")
    myCursor = conn.cursor()
    d_name = request.form['name']
    d_loc = request.form['location']
    d_area = request.form['donation_address']
    d_count = request.form['donation_count']
    d_amt = request.form['donation_amount']
    d_thana = request.form['thana']
    d_lat = request.form['lat']
    d_longx = request.form['longx']
    myCursor.execute("INSERT INTO donation (name, location, donation_address, donation_count, donation_amt, thana, lat, longx) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (d_name, d_loc, d_area, d_count, d_amt, d_thana, d_lat, d_longx))
    conn.commit()
    conn.close()
    return d_name

if __name__ == '__main__':
    app.run()