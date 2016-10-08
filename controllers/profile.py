from flask import *
from extensions import db


profile = Blueprint('profile', __name__, template_folder='templates')

@profile.route('/profile', methods=['GET','POST'])
def profile_route():

	cur = db.cursor()
	cur.execute('SELECT metric_name FROM Metrics')

	metrics = cur.fetchall()
	cur.close()

	if request.method == 'GET':
		return render_template("profile.html", metrics = metrics)

	if request.method == 'POST':
		cur = db.cursor()

		metric = request.form.get('metric_name')

		cur.execute('INSERT INTO Metrics (metric_id, metric_name) VALUES (NULL, %s)',(metric,))
		cur.execute('SELECT metric_name FROM Metrics')
		metrics = cur.fetchall()
		return render_template("profile.html", metrics = metrics)

