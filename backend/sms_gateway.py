from twilio.rest import Client

account_sid = ""
auth_token = "f"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="sms_appointment_reminders",   # template name, not custom text
    from_="+17372508034",               # your Twilio number
    to="+27781775606"                   # your verified personal number
)

print("Message SID:", message.sid)
