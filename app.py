from flask import Flask, render_template
import extensions
import controllers
import config

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

app.register_blueprint(controllers.ticket)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.queue)
app.register_blueprint(controllers.survey)
app.register_blueprint(controllers.profile)
app.register_blueprint(controllers.notification)

app.secret_key = config.env['secret_key']
if __name__ == '__main__':
  # listen on external IPs
  app.run(host=config.env['host'], port=config.env['port'], debug=True)
