from flask import *
from extensions import db

ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/ticket')
def ticket_create_route():
	return render_template("ticket.html")