import app

try:
	if(__name__ == "__main__"):
		app.routes.go("main")
except KeyboardInterrupt as keybordInterrupt:
	print("Exit application {}...".format(app.env.app_name))
	app.session.end_session()
	exit()