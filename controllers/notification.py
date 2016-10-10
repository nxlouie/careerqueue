from flask import *
from extensions import db
from twilio.rest import Client
import config

client = Client(config.env['account_sid'], config.env['auth_token'])

notification = Blueprint('notification', __name__, template_folder='templates')

@notification.route('/notification', methods=['GET','POST'])
def notification_route():
  if request.method=="POST":
    cur = db.cursor()
    cur.execute('SELECT phone FROM Ticket WHERE ticket_num=(SELECT MIN(ticket_num) FROM Ticket WHERE hidden = 0)')
    text_num = cur.fetchall()
    body = "Test text"
    to_num = "+1" + str(text_num[0]['phone'])
    message = client.messages.create(to=to_num, from_=config.env['twilio_number'], body=body)
    return ""
