from abc import ABC, abstractmethod

class IMailSender(ABC):
    @abstractmethod
    def send_mail(self, to_address, from_address, subject, body):
        pass

class SmtpServer(IMailSender):
    def send_mail(self, to_address, from_address, subject, body):
        print(f"Send mail: subject: {subject} from: {from_address} to: {to_address} body: {body}")

class EmailSender:
    def __init__(self, mail_sender: IMailSender):
        self.mail_sender = mail_sender

    def send_email(self, to_address, from_address, subject, body):
        # Delegate email sending to the mail sender implementation
        self.mail_sender.send_mail(to_address, from_address, subject, body)

# Client code.
# Create an instance of the SmtpServer class
smtp_server = SmtpServer()

# Create an instance of the EmailSender class and pass in the SmtpServer instance
email_sender = EmailSender(smtp_server)

# Send an email using the EmailSender instance
email_sender.send_email(
    to_address='recipient@example.com',
    from_address='sender@example.com',
    subject='mail subject.',
    body='This is a test email body.'
)

"""
Send mail: subject: mail subject. from: sender@example.com to: recipient@example.com body: This is a test email body.
"""