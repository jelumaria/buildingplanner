import smtplib

def send_mail(subject,message,to):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    gmail_id = 'bcachrist4@gmail.com'
    gmail_password = 'bca@123#'
    s.login(gmail_id, gmail_password)

    # message to be sent
    message = 'Subject: {}\n\n{}'.format(subject, message)

    # sending the mail
    s.sendmail(gmail_id,to,  message)

    print(to, message)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    send_mail("heoo","hai",'vishnurajani82@gmail.com')