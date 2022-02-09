
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

#Static Routes
@app.route('/ben')
def ben_cam():
    return render_template('ben.html')

@app.route('/sam')
def sam_cam():
    return render_template('sam.html')

@app.route('/')
def default_page():
    return render_template('default.html')

@app.route('/', methods=['GET', 'POST'] )
def remote():
    with open('state.txt', 'r') as file:
        for line in file:
            state = line.strip()
            print(state)
            if state[0] == '1':
                print(state)
                return render_template('ben.html')
            elif state[0] == '2':
                print(state)
                return render_template('sam.html')
            else:
                print(state)
                return render_template('default.html')



@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            state = '1'
            return state
        elif  request.form.get('action2') == 'VALUE2':
            state = '2'
            return state
        elif  request.form.get('action3') == 'VALUE3':
            state = '3'
            return state
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('control.html')
    
    return render_template("control.html")
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)