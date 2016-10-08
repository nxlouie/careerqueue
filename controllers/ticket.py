from flask import *
from extensions import db

ticket = Blueprint('ticket', __name__, template_folder='templates')

@ticket.route('/ticket', methods=['GET','POST'])
def ticket_route():
  if request.method=="GET":
    return render_template("ticket.html")
  if request.method=="POST":
    cur = db.cursor()
    print request.form.get('last')
    cur.execute('INSERT INTO Ticket VALUES (NULL,%s,%s,%s,%s,%s,%s,NULL)',(request.form.get('first'),request.form.get('last'),request.form.get('phone'),request.form.get('email'),request.form.get('major'),request.form.get('grad')))
    return redirect(request.url)
