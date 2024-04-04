from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Hemlighet!'

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        msg = request.form.get('Message')

        print(name, email, phone, msg)

    return render_template("contact.html")

@app.route("/gallery")
def gallery_page():
    return render_template("gallery.html")

@app.route("/services")
def services_page():
    return render_template("services.html")


if __name__ == "__main__":
    # with app.app_context():
    #     upgrade()
    #     seed_data()
    app.run(debug=True)