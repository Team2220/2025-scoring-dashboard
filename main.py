from flask import Flask, render_template, Response

app = Flask(__name__)

s_RAuto = 0
s_RTele= 0
s_REnd = 0

s_BAuto = 0
s_BTele = 0
s_BEnd = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coral_auto')
def coral():
    return render_template('coral_auto.html')

@app.route('/coral_tele')
def coral_tele():
    return render_template('coral_tele.html')

@app.route('/algae_auto')
def algae_auto():
    return render_template('algae_auto.html')

@app.route('/algae_tele')
def algae_tele():
    return render_template('algae_tele.html')

@app.route('/style.css')
def style():
    css = open('templates/style.css', 'r').read()
    return Response(css, mimetype='text/css')

@app.route('/score/<alliance>/<period>/<score>')
def score(alliance, period, score):
    global s_RAuto, s_RTele, s_REnd, s_BAuto, s_BTele, s_BEnd
    if alliance == 'red':
        if period == 'auto':
            s_RAuto += score
        elif period == 'tele':
            s_RTele += score
        elif period == 'end':
            s_REnd += score
    elif alliance == 'blue':
        if period == 'auto':
            s_BAuto += score
        elif period == 'tele':
            s_BTele += score
        elif period == 'end':
            s_BEnd += score
    return 'Score updated'

app.run(debug=True, port=8080)