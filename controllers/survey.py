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
  
 #   cur.execute('SELECT ticket_num, firstname, lastname FROM Ticket')

  return render_template("survey.html", metrics=metrics)
