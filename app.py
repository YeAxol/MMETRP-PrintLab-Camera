from flask import Flask, render_template, request
app = Flask(__name__)

STATE = 0

@app.route('/', methods=['GET', 'POST'] )
def remote():
            if  STATE == 1:
                return render_template('ben.html')
            elif STATE == 2:
                return render_template('sam.html')
            elif STATE == 3:
                return render_template('combo.html')
            else:
                return render_template('default.html')

@app.route('/control', methods=['POST','GET'])
def control():
    if request.method == 'POST':
        input_nopol = request.form['text_box']
        with open('state.txt', 'w+') as f:
                f.write(str(input_nopol))
        return render_template('control.html', nopol=input_nopol)
    return render_template('control.html')

if __name__ == '__main__':
    app.run()
