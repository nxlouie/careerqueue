from flask import *
from extensions import db

survey = Blueprint('survey', __name__, template_folder='templates')

@survey.route('/survey', methods=['GET'])
def survey_route():
  return render_template("survey.html")
