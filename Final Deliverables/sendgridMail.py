import sendgrid
from sendgrid.helpers.mail import *

def mailtest_request(to_email):
    sg = sendgrid.SendGridAPIClient(api_key= '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' )
    from_email = Email("kaushikselvaraju7@gmail.com")
    subject = "Budget Alert !"
    content = Content("text/plain", "Your Expense is out of Budget !")
    try:
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        print("Mail send Successfully !")
    except:
        print("Error While sending Mail !")

# mailtest_request("19cs123@kpriet.ac.in")