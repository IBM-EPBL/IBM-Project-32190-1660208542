import sendgrid
from sendgrid.helpers.mail import *

def mailtest_request(to_email):
    sg = sendgrid.SendGridAPIClient(api_key= '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' )
    from_email = Email("kaushik.selvaraju@gmail.com")
    subject = "Budget Alert !"
    content = Content("text/plain", "Your Expense is out of Budget !")
    try:
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(" Mail send Successfully ! ")
    except:
        print(" Error While sending Mail ! ")