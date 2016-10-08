from flask import *
from extensions import db


profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/profile', methods=['GET','POST'])
def profile_route():


  if request.method == 'GET':

    cur = db.cursor()
    cur.execute('SELECT metric_name FROM Metrics')
    metrics = cur.fetchall()
    cur.close()

    cur = db.cursor()
    cur.execute('SELECT firstname, lastname FROM Recruiter')
    recruiters = cur.fetchall()
    cur.close()


    return render_template("profile.html", metrics = metrics, recruiters = recruiters)

  if request.method == 'POST':

    metrics = None
    recruiters = None

    if request.form.get('op') == 'metric':
      cur = db.cursor()
      metric = request.form.get('metric_name')
      # insert
      cur.execute('INSERT INTO Metrics (metric_id, metric_name) VALUES (NULL, %s)',(metric,))
      cur.execute('SELECT metric_name FROM Metrics')
      metrics = cur.fetchall()
      cur.close()
      
      cur = db.cursor()
      cur.execute('SELECT firstname,lastname FROM Recruiter')
      recruiters = cur.fetchall()
      cur.close()
      

    elif request.form.get('op') == 'recruiter':
      cur = db.cursor()
      firstname = request.form.get('recruiter_firstname')
      lastname = request.form.get('recruiter_lastname')
      # insert
      cur.execute('INSERT INTO Recruiter (firstname, lastname) VALUES (%s, %s)',(firstname,lastname))
      cur.execute('SELECT firstname,lastname FROM Recruiter')
      recruiters = cur.fetchall()
      cur.close()

      cur = db.cursor()
      cur.execute('SELECT metric_name FROM Metrics')
      metrics = cur.fetchall()
      cur.close()

    return render_template("profile.html", metrics = metrics, recruiters = recruiters)

