from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import run_bot

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/somePath', methods=['POST'])
def returnString():
    requestString = request.get_json()
    someString = requestString.get("catch")
    print('Chatbot is working: ', someString)


    predictor = run_bot.run_Chat_bot()

    return requestString


if __name__ == '__main__':
    app.run(debug=True)
