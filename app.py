from flask import Flask, render_template
import extensions
import controllers
import config

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

app.register_blueprint(controllers.ticket)
app.register_blueprint(controllers.main)

app.secret_key = "super secret key"
if __name__ == '__main__':
  # listen on external IPs
  app.run(host=config.env['host'], port=config.env['port'], debug=True)