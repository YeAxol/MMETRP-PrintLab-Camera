from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def remote():
    with open('state.txt', 'r') as file:
        for line in file:
            state = line.strip()
            if state[0] == '1':
                file.close()
                return render_template('ben.html')
            elif state[0] == '2':
                file.close()
                return render_template('sam.html')
            elif state[0] == '3':
                file.close()
                return render_template('combo.html')
            else:
                file.close()
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
