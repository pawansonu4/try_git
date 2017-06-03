import smtplib
message = """ From: From Person <pawansonu4@gmail.com>
To: To Person <pawansonu4@gmail.com>
MIME-Version:1.0
Content-type: text/html
Subject: SMTP HTML e-mail

This is an email message to be sent in html format

<b>this is html message</b>
<h1>this is headline</h1>
"""

try:
    sender="pawansonu4@gmail.com"
    receivers="pawansonu4@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, "pawansonu41111")
    server.sendmail(sender, receivers, message)
    print ("Succ sent email")
except Exception:
    print(Exception)