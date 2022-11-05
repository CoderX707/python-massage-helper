import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


class EmailHelper:
    def __init__(self, serverConfigObject):
        self.server_name = serverConfigObject["server_name"]
        self.server_port = serverConfigObject["server_port"]
        self.server_user_email = serverConfigObject["server_user_email"]
        self.server_user_password = serverConfigObject["server_user_password"]
        self.sender_name = (
            serverConfigObject["sender_name"]
            if "sender_name" in serverConfigObject
            else serverConfigObject["server_user_email"]
        )

    def __createServerAndSendEmail(self, recipient, message):
        server = smtplib.SMTP_SSL(self.server_name, self.server_port)
        server.login(self.server_user_email, self.server_user_password)
        server.sendmail(self.server_user_email, [recipient], message.as_string())
        server.quit()

    def sendTextEmail(self, emailObject):
        format = emailObject["format"] if "format" in emailObject else "plain"
        msg = MIMEText(emailObject["body"], format, "utf-8")
        msg["Subject"] = Header(emailObject["subject"], "utf-8")
        msg["From"] = formataddr(
            (str(Header(self.sender_name, "utf-8")), self.server_user_email)
        )
        msg["To"] = emailObject["to"]
        self.__createServerAndSendEmail(emailObject["to"], msg)

    def sendEmailWithSingleAttachmentFile(self, emailObject):
        format = emailObject["format"] if "format" in emailObject else "plain"
        msg = MIMEMultipart()
        msg["Subject"] = Header(emailObject["subject"], "utf-8")
        msg["From"] = formataddr(
            (str(Header(self.sender_name, "utf-8")), self.server_user_email)
        )
        msg["To"] = emailObject["to"]
        msg.attach(MIMEText(emailObject["body"], format, "utf-8"))
        attachment = open(emailObject["filePath"], "rb")
        p = MIMEBase("application", "octet-stream")
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header(
            "Content-Disposition", "attachment; filename= %s" % emailObject["fileName"]
        )
        msg.attach(p)
        self.__createServerAndSendEmail(emailObject["to"], msg)
