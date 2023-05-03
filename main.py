from flask import Flask, request, render_template, redirect, url_for
import spotify
import gallatin

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/address/<token>')
def address(token):
    return render_template('address.html', result=token)

# @app.route('/address',methods=['POST'])
# def address():
#     if request.method=='POST':
#submit and address do it separately, combine them later to call generate_song
@app.route('/submit',methods=['POST', 'GET'])
def submit():
    userID=""
    if request.method=='POST':
        userID=request.form['userID']
    res = gallatin.main(userID)
    if res:
        return render_template('success.html')
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