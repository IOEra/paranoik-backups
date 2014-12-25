import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from paranoik.notifiers.notification import NotificationBase


class EmailNotification(NotificationBase):

    @staticmethod
    def _prepare_plaintext_message():
        return "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

    @staticmethod
    def _prepare_html_message():
        return """\
        <html>
          <head></head>
          <body>
            <p>Hi!<br>
               How are you?<br>
               Here is the <a href="https://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """

    def send(self):
        email_from = self._config.read("email", "email_from")
        email_recipients = self._config.read("email", "email_recipients")
        smtp_server = self._config.read("email", "smtp_server")
        smtp_port = self._config.read("email", "smtp_port")
        smtp_username = self._config.read("email", "smtp_username")
        smtp_password = self._config.read("email", "smtp_password")

        message = MIMEMultipart('alternative')
        message['Subject'] = "Link"
        message['From'] = email_from
        message['To'] = email_recipients

        # Create the body of the message (a plain-text and an HTML version).
        text = self._prepare_plaintext_message()
        html = self._prepare_html_message()

        mime_plain = MIMEText(text, 'plain')
        mime_html = MIMEText(html, 'html')

        message.attach(mime_plain)
        message.attach(mime_html)

        server = smtplib.SMTP('{0}:{1}'.format(smtp_server, smtp_port))
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, email_recipients, message.as_string())
        server.quit()