from flask import Flask, render_template, request, jsonify
from ApiBot import get_anime_reply

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    bot_reply = get_anime_reply(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
