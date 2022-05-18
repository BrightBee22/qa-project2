from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/monster/threat', methods=['GET'])
def get_threat():
    threat = requests.get('http://service2:5001/get/monster')
    threat_text = threat.text
    if threat_text == 'Arzuros' or 'Bishaten' or 'Lagombi' or 'Aksonom':
         danger = "Low"
    elif threat_text == 'Magnamalo' or 'Rathalos' or 'Almudron' or 'Nargacuga':
        danger = "Medium"
    else:
        danger = "High"

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')