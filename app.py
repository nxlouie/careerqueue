from flask import Flask
from flask import *

app = Flask(__name__, template_folder='templates')





app.secret_key = "super secret key"
if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)