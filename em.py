import smtplib
import ssl

def mailer(m):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "huntntech@gmail.com"  # Enter your address
	receiver_email = "apoorvmishra05@gmail.com"  # Enter receiver address
	password = '63438187@AMa'
	message = """\
	Subject: {}

	{}""".format(m['subject'],m['body'])

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)

#mailer({'subject':'hello','body':'From python'})