from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingblog'
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/posts")
def posts():
    return render_template('posts.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')

@app.route("/fetch")
def fetch_contacts():
    contacts = Contacts.query.all()
    return render_template('fetch.html', contacts=contacts)

@app.route("/edit/<int:contact_id>", methods=['GET', 'POST'])
def edit_contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone_num = request.form['phone']
        contact.msg = request.form['message']
        contact.email = request.form['email']
        db.session.commit()
        return redirect(url_for('fetch_contacts'))
    return render_template('edit.html', contact=contact)

@app.route("/delete/<int:contact_id>", methods=['POST'])
def delete_contact(contact_id):
    contact = Contacts.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('fetch_contacts'))

if __name__ == '__main__':
    app.run(debug=True)
