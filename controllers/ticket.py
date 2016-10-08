from flask import *
from extensions import db

ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/ticket', methods=['GET','POST'])
def ticket_route():
  if request.method=="GET":
    return render_template("ticket.html")
  if request.method=="POST":
    cur = db.cursor()
    cur.execute('INSERT INTO Ticket VALUES ()')
    return redirect(request.url)
