from flask import request, Flask
import pymysql
from flask import jsonify

app = Flask(__name__)
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
            'address': item[1],
            'latitude': item[2]}
        data.append(entry)
    return jsonify(data)


@app.route('/add_location', methods=['POST'])
def add_loc():
    conn = pymysql.connect(host="remotemysql.com", user="u9PE2LncVJ", passwd="EDajKwnNsd", db="u9PE2LncVJ")
    myCursor = conn.cursor()
    d_name = request.form['name']
    d_area = request.form['area']
    d_amt = request.form['amt']
    myCursor.execute("INSERT INTO donation (donor_name,donation_area,amt_contr) VALUES (%s,%s,%s)",
                     (d_name, d_area, d_amt))
    conn.commit()
    conn.close()
    return d_name


if __name__ == '__main__':
    app.run()
