from twilio.rest import Client

account_sid = ""  # copy from Console
auth_token = ""                  # copy from Console
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio test!",
    from_="+17372508034",   # your Twilio number
    to="+27781775606"       # your verified personal number
)

print("Message SID:", message.sid)
