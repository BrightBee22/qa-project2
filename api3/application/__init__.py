from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/weapon', methods =['GET'])
def get_weapon():
    weapons = ['Sword and Shield', 'Great Sword', 'Long Sword', 'Dual Blades',
                'Lance', 'Gunlance', 'Hammer', 'Hunting Horn', 'Switch Axe',
                'Charge Blade', 'Insect Glaive', 'Bow', 'Light Bowgun',
                'Heavy Bowgun']

    randomnum = random.randint(0,13)
    return Response(weapons[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')