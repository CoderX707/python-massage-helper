from email_helper import EmailHelper

# setup server config
config = {
    "server_name": "Server name", # Ex.: smtp.gmail.com
    "server_port": "Server port number", # Ex.: 465
    "server_user_email": "Server user email", # Ex.: youremail@gmail.com
    "server_user_password": "Server user password", # Ex.: Your Gmail password
    "sender_name": "Show sender name", # optional, Ex.: User Name
}
emailHelper = EmailHelper(config)

# send text email. object and function
emailObj = {
    "to": "To email address",
    "subject": "email subject",
    "body": "<h1>email body</h1>",
    "format": "html",  # optional, You can use (plain or html) format. default is plain
}
emailHelper.sendTextEmail(emailObj)

# send email with single attachment. object and function
emailObjWithAttachment = {
    "to": "To email address",
    "subject": "email subject",
    "body": "<h1>email body</h1>",
    "fileName": "File name", # Ex.: Attachment.zip
    "filePath": "File path", # Ex.: /test.zip
    "format": "html",  # optional, You can use (plain or html) format. default is plain
}

emailHelper.sendEmailWithSingleAttachmentFile(emailObjWithAttachment)
