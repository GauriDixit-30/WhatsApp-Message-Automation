#step1- install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

#step2- Twilio credentials
account_sid = 'Your Twilio Account SID here'
auth_token = 'Your Twilio Auth Token here'

client = Client(account_sid, auth_token)

#step3- desgin send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp: Your Twilio WhatsApp Number',  # Twilio sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")  #error occurred

#step4- user input
name = input("Enter the recipient's name: ")
recipient_number = input("Enter the recipient's WhatsApp number with country code (e.g, +1234567890): ")
message_body = input(f"Enter the message you want to send to {name}: ")

#step5- parse date/time and calculate delay
date_str=input("Enter the date to send the message (YYYY-MM-DD): ")
time_str=input("Enter the time to send the message (HH:MM in 24-hour format): ")

#combine date and time into a single datetime object
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
#calculate delay in seconds
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past. Scheduled time must be in the future. Please try again.")
else:
    print(f"Message scheduled be sent to {name} at {schedule_datetime}.")

    time.sleep(delay_seconds)  #wait until the scheduled time
    send_whatsapp_message(recipient_number, message_body)  #send the message
    