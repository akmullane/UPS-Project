from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        weight = request.form['weight']
        types = request.form['types']
        size = request.form['size']
        origin = request.form['origin']
        destination = request.form['destination']
        pickup_time = request.form['pickup_time']
        status = request.form['status']
        location = request.form['location']
        referenceNum = request.form['referenceNum']
#     # Do something with the form data
#     return f"Package {referenceNum} has been submitted!"
        # Do something with the input data
        return f"Package {referenceNum} has been submitted!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run()




# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET','POST'])
# def submit_package():
#     name = request.form['name']
#     weight = request.form['weight']
#     types = request.form['types']
#     size = request.form['size']
#     origin = request.form['origin']
#     destination = request.form['destination']
#     pickup_time = request.form['pickup_time']
#     status = request.form['status']
#     location = request.form['location']
#     referenceNum = request.form['referenceNum']
#     # Do something with the form data
#     return f"Package {referenceNum} has been submitted!"

# if __name__ == '__main__':
#     app.run(debug=True)
