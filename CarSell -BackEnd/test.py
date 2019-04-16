from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb2137afcc8750e0d589536e17a8932f7"
# Your Auth Token from twilio.com/console
auth_token  = "80f4c1dcf38bdd83af13154521009772"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675310", 
    from_="+15017122661",
    body="Hello from Python!")

print(message.sid)
