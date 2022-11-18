import sendgrid
from sendgrid.helpers.mail import *

def mailtest_request(to_email):
    # sg = sendgrid.SendGridAPIClient(api_key= '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' )
    from_email = Email("kaushik.selvaraju@gmail.com")
    subject = "Budget Alert !"
    content = Content("text/plain", "Your Expense is out of Budget !")
    try:
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(" Mail send Successfully ! ")
    except:
        print(" Error While sending Mail ! ")