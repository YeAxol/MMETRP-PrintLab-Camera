from flask import Flask, render_template, request

app = Flask(__name__,template_folder='./templates',static_folder='./static')

STATE = [0]

@app.route('/control', methods=['POST','GET'])
def control():
    if request.method == 'POST':
        input_nopol = request.form['text_box']
        global STATE
        if input_nopol == '':
            input_nopol = 0
        STATE[0] = int(input_nopol)
        return render_template('control.html', nopol=input_nopol)
    return render_template('control.html')

@app.route('/', methods=['GET', 'POST'] )
def remote():
        global STATE
        print("state is =", STATE)
        State = STATE
        if STATE != State:
            remote()
        if  STATE[0] == 1:
            return render_template('ben.html')
        elif STATE[0] == 2:
            return render_template('sam.html')
        elif STATE[0] == 3:
            return render_template('combo.html')
        else:
            return render_template('default.html')

if __name__ == '__main__':
    app.run()
