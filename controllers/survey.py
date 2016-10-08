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

    return render_template("survey.html", metrics=metrics, student=student[0], recruiters=recruiters, ticket_num=ticket_num)

  if request.method == 'POST':

    cur = db.cursor()
    cur.execute('SELECT * FROM Metrics')
    metrics = cur.fetchall()
    cur.close()

    cur = db.cursor()
    for i in range(1, len(metrics) + 1):
      print request.form.get(str(i))
      # update StudentMetrics Table here
      query = 'INSERT INTO StudentMetrics VALUES (%s,%s,%s)'
      cur.execute(query,(str(request.form.get('ticket_num')),str(i),request.form.get(str(i))))
    cur.close()

    cur = db.cursor()
    comments = request.form.get('comments')
    print comments # update Ticket table here
    query = 'UPDATE Ticket SET comments=%s WHERE ticket_num=%s'
    cur.execute(query,(comments,str(request.form.get('ticket_num'))))
    cur.close()

    cur = db.cursor()
    recruiter_id = request.form.get('recruiter_name')
    print recruiter_id # AND update Ticket table here
    query = 'UPDATE Ticket SET recruiter_id=%s WHERE ticket_num=%s'
    cur.execute(query,(recruiter_id,str(request.form.get('ticket_num'))))
    cur.close()
    return redirect(url_for('queue.queue_route'))
