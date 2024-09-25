from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = "random"
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT email address?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    welcome_message = ""
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    email = session.get('email')
    email_partitioned = email.split('.') if email else []

    if 'utoronto' not in email_partitioned:
        welcome_message += "Please use your UofT email."
    elif email:
        welcome_message += f"Your UofT email is {email}"


    return render_template('index.html', form=form, name=session.get('name'), welcome_message=welcome_message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')