from flask import *
from extensions import db

notification = Blueprint('notification', __name__, template_folder='templates')

@notification.route('/notification', methods=['GET','POST'])
def notification_route():
	if request.method=="POST":
		print "TEST ROUTE PING SUCCESS!!!"