# Full Automation Pipeline

## Description
In this project, python is tracking the prices of all the products in the All-in-One website that has dropped below a threshold of $500. Any resulting price below the threshold will be emailed to a customer or a designated email.  The link to the site is: https://webscraper.io/test-sites/e-commerce/allinone

## Requirements:
- Python 3
- requests library
- beautifulsoup4 library
- dotenv library

# Installation:
Install the required dependencies using pip:  
- pip install requests beautifulsoup4
- pip install python-dotenv

## Setup
Create a '.env' file in the project folder with the following:
EMAIL_ADDRESS=yourgmail@gmail.com
EMAIL_PASSWORD=your_app_password

## How to run:  
After installation, navigate to the project folder and run the command below.

## Commands
python3 pipeline.py

## Current Limitations
- Email recipient is hardcoded to sender
- Tracks all products, not a specific one
- Threshold is hardcoded at $500

## Future Improvements
- Schedule script to run automatically every day
- Accept threshold as a command line argument
- Send one summary email instead of one per product
- Track specific products by name
- Add a separate "alerts" CSV that logs only prices below threshold

## Output
- Saves all the scraped prices to prices.csv with timestamps
- Sends an email alert for any price below $500

## Acknowledgements
Built with guidance and assistance from Claude Ai.