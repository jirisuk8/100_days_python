import smtplib
import datetime as dt
import random


def send_email(mail_body):
    my_email = "epigeon.cz@gmail.com"
    password = "epigeon.CZ88"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pavelkarel@yahoo.com",
                            msg=f"Subject: Motivational quote for today\n\n Hello,\n"
                                f"your motivational quote for today:\n\n {mail_body}")


def get_quote():
    with open("quotes.txt", "r") as quotes:
        quote = random.choice(quotes.readlines())
    return quote



# if dt.datetime.now().weekday() == 4:
#     print(dt.datetime.now().weekday())

send_email(get_quote())
