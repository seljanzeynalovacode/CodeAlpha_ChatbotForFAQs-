from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_logic import get_response

app = Flask(__name__)
# We use CORS to allow requests coming from the frontend (from another port)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    # Get the JSON data sent from the frontend
    data = request.get_json()
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'answer': 'No question was entered.'}), 400
        
    # Call the function from our logic file and get the response
    bot_reply = get_response(user_message)
    
    # Send the response to the frontend in JSON format
    return jsonify({'answer': bot_reply})

if __name__ == '__main__':
    # Start the server on port 5000
    print("Backend server is running! http://localhost:5000") 
    app.run(debug=True, port=5000)