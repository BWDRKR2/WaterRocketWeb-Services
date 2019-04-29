import falcon
import launch_api


class Arm(object):
    def on_get(self, req, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('Armend = Y')
	a=launch_api.arm()

class Unarm(object):
    def on_get(self, req, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('Unarmed = N')
	#a=launch_api.unarm()

class BeginFuel(object):
    def on_get(self, req, resp, fuel_amount):
        a=launch_api.beginfuel(fuel_amount)
	resp.status = falcon.HTTP_200
	resp.body = ('Begin Fuel = Y')
	

class EndFuel(object):
    def on_get(self, req, resp):
        a=launch_api.endfuel()
	resp.status = falcon.HTTP_200
	resp.body = ('End Fuel = Y')	

class Abort(object):
    def on_get(self, reg, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('Abort = Y')

class Launch(object):
    def on_get(self, reg, resp):
        a=launch_api.launch()
	resp.status = falcon.HTTP_200
	resp.body = ('Launch = Y')
	resp.body = ('Lift Off')

app = falcon.API()


arm = Arm()
unarm = Unarm()
beginfuel = BeginFuel()
endfuel = EndFuel()
abort = Abort()
launch = Launch()


app.add_route('/arm', arm)
app.add_route('/unarm', unarm)
app.add_route('/begin_fuel/{fuel_amount}', beginfuel)
app.add_route('/end_fuel', endfuel)
app.add_route('/abort', abort)
app.add_route('/launch', launch)
