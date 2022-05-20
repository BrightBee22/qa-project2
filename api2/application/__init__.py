from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/monster', methods =['GET'])
def get_monster():
    monsters = ['Bishaten',
                'Magnamalo', 'Rathalos',
                'Valstrax', 'Chameleos']
    randomnum = random.randint(0,4)
    return Response(monsters[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')