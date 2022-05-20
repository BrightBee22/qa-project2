from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/weapon', methods =['GET'])
def get_weapon():
    weapons = ['Great Sword', 'Hammer',
                'Charge Blade', 'Insect Glaive',
                'Bow',]
    randomnum = random.randint(0,4)
    return Response(weapons[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')