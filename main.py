from flask import Flask, request, render_template, redirect, url_for, session
import spotify
import gallatin

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "gallatinisamazing"
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/address/<user>')
def address(token):
    return render_template('address.html', result=token)

@app.route('/submit_city', methods=['POST'])
def submit_city():
    if request.method == 'POST':
        res = request.form['city']
        if res != "":
            session['city'] = res
        else:
            session['city'] = 'New York'
    return render_template('mood.html')

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    if request.method == 'POST':
        session['mood'] = request.form['mood']
    return render_template('output.html')

@app.route('/submit_output', methods=['POST'])
def submit_output():
    if request.method == 'POST':
        session['song_counts'] = request.form['song_counts']
    return render_template('mode.html')

@app.route('/submit_mode', methods=['POST'])
def submit_mode():
    if request.method == 'POST':
        session['mode'] = request.form['mode']
    mode = session['mode']
    count = session['song_counts']
    mood = session['mood']
    city = session['city']
    token = session['token']
    print(mode, count, mood, city)
    res = gallatin.generate_playlist(token, city, mood, count, mode)
    if res:
        return render_template('success.html')
    else:
        return render_template('fail.html')

@app.route('/submit',methods=['POST', 'GET'])
def submit():
    userID=""
    if request.method=='POST':
        userID=request.form['userID']
    res = gallatin.auth(userID)
    if res:
        session['token'] = res
        return render_template('city.html')
    else:
        return render_template('fail.html')

@app.route('/auto')
def auto():
    return render_template('auto.html')

@app.route('/manual')
def manual():
    return render_template('manual.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)