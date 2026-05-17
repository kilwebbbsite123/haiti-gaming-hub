from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fortnite')
def fortnite():
    return render_template('fortnite.html')

@app.route('/callofduty')
def callofduty():
    return render_template('callofduty.html')

@app.route('/efootball')
def efootball():
    return render_template('efootball.html')

@app.route('/freefire')
def freefire():
    return render_template('freefire.html')

@app.route('/netflix')
def netflix():
    return render_template('netflix.html')

if __name__ == '__main__':
    app.run(debug=True)
