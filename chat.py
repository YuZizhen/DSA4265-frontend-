from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_user_input(request_data):
    """Extracts and validates user input from the request"""
    user_message = request_data.get('message', '').strip()
    if not user_message:
        raise ValueError("No message provided")
    return user_message

def get_bot_response(user_message):
    """Processes user input and generates bot response"""
    # Currently just acknowledges receipt
    # Later you can add your LLM logic here
    return f"Message received: {user_message}"

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        # Get and validate input
        user_message = get_user_input(request.json)
        
        # Generate response
        bot_response = get_bot_response(user_message)
        
        return jsonify({
            'status': 'success',
            'response': bot_response
        })
    
    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)