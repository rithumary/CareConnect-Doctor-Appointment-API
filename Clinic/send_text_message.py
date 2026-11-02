import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+91XXXXXXXXXX",
    from_="+1XXXXXXXXXX",
    body="Your appointment has been booked successfully."
)

print(message.sid)