from flask import *
from extensions import db

queue = Blueprint('queue', __name__, template_folder='templates')

@queue.route('/queue', methods=['GET','POST'])
def queue_route():
  if request.method=='GET':
    cur = db.cursor()
    cur.execute('SELECT ticket_num, firstname, lastname FROM Ticket WHERE recruiter_id IS NULL AND hidden = 0')
    queue = cur.fetchall()
    cur.close()
    return render_template("queue.html", queue=queue)
  if request.method=='POST':
    cur = db.cursor()
    query = 'UPDATE Ticket SET hidden=1 WHERE ticket_num=%s'
    cur.execute(query,(request.form.get('num'),))
    return redirect(url_for('survey.survey_route',ticketnum = request.form.get('num')))
