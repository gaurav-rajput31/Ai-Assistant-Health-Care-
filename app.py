from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
        user_input = data['message']
            response = check_symptoms(user_input)  # Or use an AI model
                return jsonify({"response": response})

                if __name__ == '__main__':
                    app.run(debug=True)
                    