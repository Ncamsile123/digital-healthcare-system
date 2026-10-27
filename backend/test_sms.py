from twilio.rest import Client

account_sid = ""  # copy from Console
auth_token = ""                  # copy from Console
client = Client(account_sid, auth_token)

# message = client.messages.create(
# body="Appointment reminder",
# from_="+17372508034",
# to="+27781775606"
# )
# print("Message SID:", message.sid)
