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
    conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd", db="u9PE2LncVJ")
    myCursor = conn.cursor()
    myCursor.execute('select * from donation')
    result = myCursor.fetchall()
    data = []

    for item in result:
        entry = {
            'name': item[0],
            'lcoation': item[1],
            'donation_address': item[2],
            'donation_count': item[3],
            'donation_amount': item[4],
            'thana': item[5],
            'lat': item[6],
            'longx': item[7],
        }
        data.append(entry)
    return jsonify(data)

@app.route('/add_location', methods=['POST'])
def add_loc():
    conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd", db="u9PE2LncVJ", charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCurso)
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

if __name__ == '__main__':
    app.run()