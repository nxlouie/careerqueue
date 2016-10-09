from flask import *
from extensions import db
from twilio.rest import Client

account_sid = "ACb5ca7ce3d470992177f911ad8c1201b6" # Your Account SID from www.twilio.com/console
auth_token  = "fa15185b441c4d80de9aceca5aa0292c"  # Your Auth Token from www.twilio.com/console
twilio_number ="+16697219770"

client = Client(account_sid, auth_token)

notification = Blueprint('notification', __name__, template_folder='templates')

@notification.route('/notification', methods=['GET','POST'])
def notification_route():
  if request.method=="POST":
    cur = db.cursor()
    cur.execute('SELECT phone FROM Ticket WHERE ticket_num=(SELECT MIN(ticket_num) FROM Ticket) And hidden=0')
    text_num = cur.fetchall()
    body = "Twilio api BOI"
    to_num = "+1" + str(text_num[0]['phone'])
    message = client.messages.create(to=to_num, from_=twilio_number, body=body)
    return ""