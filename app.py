from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Level 1 route - Basic Vocabulary Games
@app.route('/level1')
def level1():
    return render_template('level1.html')

# Level 2 route - Guess the Word
@app.route('/level2')
def level2():
    return render_template('level2.html')

# Level 3 route - Spot the Error
@app.route('/level3')
def level3():
    return render_template('level3.html')

# Level 4 route - Scenarios with Videos
@app.route('/level4')
def level4():
    return render_template('level4.html')

# Level 5 route - Debating and Public Speaking
@app.route('/level5')
def level5():
    return render_template('level5.html')

# API route to simulate daily vocabulary challenge
@app.route('/api/daily-challenge')
def daily_challenge():
    words = [
        {"word": "Ebullient", "meaning": "Cheerful and full of energy"},
        {"word": "Resilient", "meaning": "Able to recover quickly from difficulties"},
        {"word": "Sagacious", "meaning": "Having good judgment; wise"},
        {"word": "Vivacious", "meaning": "Full of life and high-spirited"},
        {"word": "Perspicacious", "meaning": "Having a ready insight into and understanding of things"}
    ]
    return jsonify(words)

if __name__ == '__main__':
    app.run(debug=True)