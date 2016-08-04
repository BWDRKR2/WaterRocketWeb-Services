from time import sleep
import pifacerelayplus
import configparser

DELAY = 10.0  # seconds
Config = configparser.ConfigParser()


def arm():
	print('Armed')
	armed = 'Y'
	return armed

def unarm():
	print('Unarmed')
	armed = 'N'
	return armed

def beginfuel(pfr):
	print('Begin Fueling')
	fueling = 'Y'
	pfr.relays[0].turn_on()
	sleep(10)

def endfuel(pfr):
	print('End Fueling')
	fueling = 'N'
	pfr.relays[0].toggle() 
	fueled_complete = 'Y'
	return fueled_complete

def abort():
	a=0

def launch(pfr, armed, fueled):
	if armed == 'Y' and fueled == 'Y':
		print('Starting Launch Sequence')
		print('10')
		sleep(1)
		print('9')
		sleep(1)
		print('8')
		sleep(1)
		print('7')
		sleep(1)
		print('6')
		sleep(1)
		print('5')
		sleep(1)
		print('4')
		sleep(1)
		print('3')
		sleep(1)
		print('2')
		sleep(1)
		print('1')
		sleep(1)
		pfr.relays[1].turn_on()
		print('Lift Off')
		sleep(2)
		pfr.relays[1].toggle()

def createconfig(Config, Armed, Fueled, Launch):
	cfgfile = open("launch.cfg",'w')
	Config.add_section('Launch_Settings')
	Config['Launch_Settings']['Armed'] = Armed
	Config['Launch_Settings']['Fueled'] = Fueled
	Config['Launch_Settings']['Launch'] = Launch
	Config.write(cfgfile)
	cfgfile.close()

	


if __name__ == "__main__":
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

    armed=arm()
#    unarm()
    beginfuel(pfr)
    fueled=endfuel(pfr)
    launch(pfr,armed, fueled)
    Armed = 'Y'
    Fueled = 'Y'
    Launch = 'N'		
    createconfig(Config, Armed, Fueled, Launch)
    
exit()





