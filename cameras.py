
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/ben')
def ben_cam():
    return render_template('ben.html')

@app.route('/sam')
def sam_cam():
    return render_template('sam.html')

@app.route('/default')
def default_page():
    return render_template('default.html')

@app.route('/')
def remote(state):
    if state == 1:
        return render_template('ben.html')
    elif state == 2:
        return render_template('sam.html')
    elif state == 3:
        return render_template('default.html')
    pass


@app.route('/control')
def control():
    pass

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)