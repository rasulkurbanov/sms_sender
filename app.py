from twilio.rest import Client

account_sid = "AC9bb055dc733d087dcec1f91c9393b961"
auth_token = "38c400707b3b1433b599c51a9ed38754"

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14153196148',
    body="Assalomu alaykum Islomjon.Salomatmisiz?",
    to='+998993241123'
)

print(message.sid)
