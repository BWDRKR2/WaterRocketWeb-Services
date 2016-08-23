import falcon
import launch_api

class Reset(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Dan Immanuel Kant\n\n')

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
    def on_get(self, req, resp):
     	resp.status = falcon.HTTP_200
	resp.body = ('Begin Fuel = Y')
	a=launch_api.beginfuel()

class EndFuel(object):
    def on_get(self, req, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('End Fuel = Y')	

class Abort(object):
    def on_get(self, reg, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('Abort = Y')

class Launch(object):
    def on_get(self, reg, resp):
	resp.status = falcon.HTTP_200
	resp.body = ('Launch = Y')
	resp.body = ('Lift Off')

app = falcon.API()

reset = Reset()
arm = Arm()
unarm = Unarm()
beginfuel = BeginFuel()
endfuel = EndFuel()
abort = Abort()
launch = Launch()

app.add_route('/reset', reset)
app.add_route('/arm', arm)
app.add_route('/unarm', unarm)
app.add_route('/begin_fuel', beginfuel)
app.add_route('/end_fuel', endfuel)
app.add_route('/abort', abort)
app.add_route('/launch', launch)
