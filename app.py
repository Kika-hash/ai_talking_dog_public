from flask import Flask, request, render_template, redirect, url_for
from back_end_main import back_end

app = Flask(__name__, static_folder="static")

@app.route("/")
def main_page():
    return render_template("main.html")


@app.route('/answer', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        question = request.form["questionInput"]
        response = back_end(question)
        return render_template("main.html", result_message=response)

    # Render the form template for GET requests
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(debug=True)
