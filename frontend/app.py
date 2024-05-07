from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/submit',methods=['POST'])
def submit():
    id=request.form.get('id',None)
    if id==None:
        return "Error"
    
    output= 2

    return render_template('index.html',predicted_output=output)
    
@app.route("/sigin")
def signin():
    return render_template('sigin.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9000,debug=True)