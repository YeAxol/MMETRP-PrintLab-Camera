
from flask import Flask, render_template, request, make_response
from os import listdir
app = Flask(__name__)

#Static Routes
@app.route('/ben')
def ben_cam():
    return render_template('ben.html')

@app.route('/sam')
def sam_cam():
    return render_template('sam.html')

@app.route('/', methods=['GET', 'POST'] )
def remote():
    with open('state.txt', 'r') as file:
        for line in file:
            state = line.strip()
            print(state)
            if state[0] == '1':
                print(state)
                file.close()
                return render_template('ben.html')
            elif state[0] == '2':
                print(state)
                file.close()
                return render_template('sam.html')
            else:
                print(state)
                file.close()
                return render_template('default.html')



@app.route('/control', methods=['POST','GET'])
def control():
    input_nopol = request.form['text_box']
    if request.method == 'POST':
        with open('state1.txt', 'w+') as f:
                f.write(str(input_nopol))
        return render_template('control.html', nopol=input_nopol)
    else:
        return render_template('control.html')

    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)