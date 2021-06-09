from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    a = ""
    country = ['Russia', 'Italy', 'USA']
    print(request.form)
    if request.method == "POST":
        if request.form.get("country_list") == 'USA':
            a = 'RED'
    return render_template("index.html", country=country, a=a)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')