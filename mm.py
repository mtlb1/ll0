import requests
from flask import *

app = Flask(__name__)

@app.route("/")
def Home():
    return "Dev : @X_DevR | @PR2_NET"

@app.route("/ChToken/")
def Ch():
    Tok = request.args.get("Token")
    Rget = requests.get("https://api.telegram.org/bot"+Tok+"/Getupdates")
    if '"ok":true' in Rget.text:
        return {'Status':True,'DEV':'DaMaR | @X_DevR'}
    else:
        return {'Status':False,'DEV':'DaMaR | @X_DevR'}
if __name__ == "__main__":
    app.run()
