##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import datetime as dt
import pandas as pd
import random
import smtplib

EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day


data = pd.read_csv("birthdays.csv")
recipients = [[row["name"],row["email"],row["year"],row["month"],row["day"]] for _, row in data.iterrows()]

for recipient in recipients:
    if month in recipient and day in recipient:
        random_int = f"letter_{random.randint(1,3)}"
        with open(f"letter_templates/{random_int}.txt","r") as random_letter:
            default_letter_text = random_letter.read()
            new_letter_text = default_letter_text.replace("[NAME]", recipient[0])
            print(new_letter_text)
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=recipient[1],
                                    msg=f"Subject:Happy Birthday!\n\n{new_letter_text}")
