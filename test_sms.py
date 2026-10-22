from backend import sms_gateway

# Replace with your real phone number (including country code)
sms_gateway.send_sms("+27781775606", "Test message from FastAPI healthcare system")

print("SMS sent successfully!")
