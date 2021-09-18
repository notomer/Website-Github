import pandas as pd
import smtplib

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values

print(emails)
