from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    result = 0
    resp = request.form
    a = resp.get('fnum')
    b = resp.get('snum')
    c = resp.get('calc')

    if c == '1':
        try:
            result = int(a)+int(b)
        except:
            result = 'Please Enter valid input'

    elif c == '2':
        try:
            result = int(a) - int(b)
        except:
            result = 'Please Enter Valid Inputs'

    elif c == '3':
        try:
            result = int(a) * int(b)
        except:
            result = 'Please Enter Valid Inputs'

    elif c == '4':
        try:
            result = int(a) / int(b)
        except:
            result = 'Please Enter Valid Inputs'

    return render_template("calci.html", abc=result)


if __name__ == '__main__':
    app.run(debug=True)
