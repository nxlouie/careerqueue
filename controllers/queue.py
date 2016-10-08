from flask import *
from extensions import db

queue = Blueprint('queue', __name__, template_folder='templates')

@queue.route('/queue', methods=['GET'])
def queue_route():
  cur = db.cursor()

  cur.execute('SELECT ticket_num, firstname, lastname FROM Ticket')
  queue = cur.fetchall()
  
  print queue

  return render_template("queue.html", queue=queue)
