from flask import *
from extensions import db

survey = Blueprint('survey', __name__, template_folder='templates')

@survey.route('/survey', methods=['GET', 'POST'])
def survey_route():

  ticket_num = request.args.get('ticketnum',"")

  if request.method == 'GET':
    cur = db.cursor()
    cur.execute('SELECT * FROM Metrics')
    metrics = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT firstname, lastname, major, grad_year FROM Ticket WHERE ticket_num = %s', (ticket_num,))
    student = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT recruiter_id, firstname, lastname FROM Recruiter')
    recruiters = cur.fetchall()
    cur.close()

  return render_template("survey.html", metrics=metrics, student=student[0], recruiters=recruiters)
