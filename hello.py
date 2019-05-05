from flask import Flask, render_template, redirect, request, url_for
from forms import Forms
app = Flask(__name__)
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "K3Y0NBL4D3B0Y"

@app.route("/", methods = ['GET','POST'])
def calculate():
    form = Forms()

    if request.method == 'POST':
        print("test1")
        username = request.form.get('Origin')  # access the data inside 
        password = request.form.get('Destination')
        calculate = request.form.get('Calculate')
        return redirect(url_for("/finished"))
    else:
        return render_template('calculate.html',form=form)
    


@app.route("/finished")
def finished():
    return render_template('finished.html')

if __name__ == '__main__':
    app.run(debug=True)

