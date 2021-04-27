import smtplib
import ssl

def mailer(m, name=0):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = m['sender']  
	receiver_email = m['receiver']  
	password = m['password']
	s = 'sub'
	message = f"""\
	{name if name else ''}
	
Subject: {m['subject']}


{m['body']}"""

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		try:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, message)
			return 'Sent'
		except Exception as e:
			#print("Unexpected error:", e)
			return "Authentication error: " + str(e)


	

