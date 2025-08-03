from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Hardcoded book recommendations
recommendations = {
    'romance': 'I recommend "Pride and Prejudice" by Jane Austen.',
    'mystery': 'Try "Gone Girl" by Gillian Flynn.',
    'fantasy': 'How about "Harry Potter" by J.K. Rowling?',
    'thriller': 'Consider "The Da Vinci Code" by Dan Brown.',
    'sci-fi': 'You might enjoy "Dune" by Frank Herbert.'
}

def get_recommendation(message):
    message = message.lower()
    for genre, book in recommendations.items():
        if genre in message or (genre == 'sci-fi' and 'science fiction' in message):
            return book
    return "I'm not sure what genre you like. Try mentioning romance, mystery, fantasy, thriller, or sci-fi."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message", "")
    bot_response = get_recommendation(user_msg)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
