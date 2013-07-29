from flask import Flask, render_template, request
from flask.ext.mail import Mail, Message
app = Flask(__name__)

mail=Mail(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'juanber84@gmail.com',
	MAIL_PASSWORD = '*******************'
	)

mail=Mail(app)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
    	myemail = 'juanber84@gmail.com'
    	msg = Message('NUEVO MENSAJE DE LA WEB',sender=myemail,recipients=[myemail])
	msg.body = request.form['name']+'  '+request.form['email']+'  '+request.form['message']
	mail.send(msg)
        return render_template('index.html', error = 'Enviado')
    else:
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run('juanberzal.com', 80)