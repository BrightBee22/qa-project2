from flask import Flask, render_template
import requests, uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4)

@app.route('/fortune', methods=['GET', 'POST'])
def recweapon():
    monster = requests.get('http://service2:5001/get/monster').text
    weapon = requests.get('http://service3:5002/get/weapon').text
    fortune = monster + "," + weapon
    recweapon = requests.post('http://service4:5003/post/recweapon', data=fortune)
    return render_template('home.html', monster=monster, weapon=weapon, recweapon=recweapon.text)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')