from twilio.rest import Client

account_sid = ""
auth_token = ""

def send_sms(to_number, message_text):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message_text,
        from_="+17372508034",
        to=to_number
    )

    return message.sid