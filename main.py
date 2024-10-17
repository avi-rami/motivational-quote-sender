import smtplib
import datetime as dt
import random

password = "yoie xmvd ebsh juyd"
my_email = "pythontester93@gmail.com"
other_email = "pythontester2002@yahoo.com"

# motivational quote email sender
today = dt.datetime.now()
weekday = today.weekday()
if weekday == 2:
    with (open("quotes.txt")) as q:
        quotes_list = q.readlines()
        new_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=other_email,
            msg=f"Subject:Monday Motivation!\n\n{new_quote}")
