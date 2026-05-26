# Title: Full Automation Pipeline
# Fetch the Webpage
# Find the price element
# Extract the price 
# Get the current timestamp
# Open the CSV in append mode
# Write the timestamp and price as new row

import requests
import csv
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime
from bs4 import BeautifulSoup

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

url = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

prices = soup.find_all("span", itemprop="price")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

filename = "prices.csv"

file_exists = os.path.isfile(filename)

with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    
    if not file_exists:
        writer.writerow(['Timestamp', 'Prices'])
    
    for price in prices:
        writer.writerow([now, price.text.strip()])
            
        price_value = float(price.text.strip().replace("$", ""))

        if price_value < 500:
            msg = MIMEText(f"Alert! Price dropped below threshold: {price_value}")
            msg["Subject"] = "Price Alert!"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = EMAIL_ADDRESS
            
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
                print("Alert email sent!")