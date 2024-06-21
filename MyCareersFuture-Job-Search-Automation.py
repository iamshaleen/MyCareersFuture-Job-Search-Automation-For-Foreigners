import requests
import json
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Step 1: Define the API requests
api_requests = [
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "growth",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "partnership",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "strategy",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "product manager",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "program manager",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "payments",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "loan",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "cards",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    },
    {
        'url': 'https://api.mycareersfuture.gov.sg/v2/search?limit=20&page=0',
        'headers': {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36',
            'Mcf-Client': 'jobseeker',
            'Origin': 'https://www.mycareersfuture.gov.sg'
        },
        'payload': {
            "sessionId": "",
            "search": "fintech",
            "categories": ["Banking and Finance"],
            "positionLevels": ["Middle Management", "Manager", "Senior Executive", "Professional"],
            "postingCompany": [],
            "sortBy": ["new_posting_date"]
        }
    }
    
]

# Step 2: Define function to send API requests and fetch results
def send_api_requests(api_requests):
    results = []
    for request in api_requests:
        response = requests.post(request['url'], headers=request['headers'], json=request['payload'])
        if response.status_code == 200:
            #print((response.json())[])
            test = response.json()
            for t in test['results']:
                #print(t['postedCompany']['name'])
                #print(t['title'])
                #print(t['metadata']['newPostingDate'])
                results.append(t['postedCompany']['name']+"||"+t['title']+"||"+t['metadata']['newPostingDate']+"||"+t['metadata']['jobDetailsUrl'])
            #print(results)
        else:
            print(f"Failed to fetch data from {request['url']}")
    return list(set(results))

# Step 3: Send API requests and fetch results
api_results = send_api_requests(api_requests)

# Step 4: Define function to compare results and find new entries
def find_new_entries(previous_results, current_results):
    new_entries = []
    for current_result in current_results:
        #print(current_result)
        #print(current_result not in previous_results)
        if current_result not in previous_results:
            new_entries.append(current_result)
    return new_entries

# Step 5: Load previous results from file or database (if available)
try:
    #print("inside load previous results")
    with open('previous_results.json', 'r') as file:
        previous_results = json.load(file)
        #print(previous_results)
except FileNotFoundError:
    previous_results = []

# Step 6: Find new entries
new_entries = find_new_entries(previous_results, api_results)

# Step 7: Save current results for future comparison
with open('previous_results.json', 'w') as file:
    json.dump(api_results, file)

# Step 8: Define function to send email
def send_email(new_entries):
    if new_entries:
        # Email configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'sender@gmail.com'
        receiver_email = 'recepient@gmail.com'
        password = 'your app specific password here' # Create one here and add it in the script https://myaccount.google.com/apppasswords

        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'New Job Listings in SG - Automated job '+datetime.date.today().strftime('%d-%b-%Y')

        # Create email body
        #print(new_entries)
        body = 'New job listings:\n\n'
        for job in new_entries:
            arr = job.split("||")
            body += f"Company Name: {arr[0]}\n"
            body += f"Job title: {arr[1]}\n"
            body += f"Posting Date: {arr[2]}\n"
            body += f"Job URL: {arr[3]}\n"
            body += f"\n\n"
        print(body)
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    else:
        print("No new job listings found.")

# Step 9: Send email with new entries (if any)
send_email(new_entries)
