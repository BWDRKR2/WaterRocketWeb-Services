from time import sleep
import pifacerelayplus
import configparser




def reset():
	armed = 'N'
	fueling = 'N'
	fueled = 'N'
	launch = 'N'
	abort = 'N'
	createconfig(armed, fueling, fueled, launch, abort)

def arm():
	print('Armed')
	armed = 'Y'
	fueling = 'N'
	fueled = 'N'
	launch = 'N'
	abort = 'N'
	createconfig(armed, fueling, fueled, launch, abort)
	return armed

def unarm():
	print('Unarmed')
	armed = 'N'
	fueling = 'N'
	fueled = 'N'
	launch = 'N'
	createconfig(armed, fueling, fueled, launch)
	return armed

def beginfuel(pfr):
	print('Begin Fueling')
	armed = 'Y'
	fueling = 'Y'
	fueled = 'N'
	launch = 'N'
	abort = 'N'
	createconfig(armed, fueling, fueled, launch, abort) 
	pfr.relays[0].turn_on()
	sleep(10)

def endfuel(pfr):
	print('End Fueling')
	armed = 'Y'
	fueling = 'N'
	fueled = 'Y'
	launch = 'N'
	abort = 'N'
	pfr.relays[0].toggle() 
	createconfig(armed, fueling, fueled, launch, abort)
	return fueled

def abort():
	print('Abort Launching')
	armed = 'Y'
	fueling = 'N'
	fueled = 'N'
	launch = 'Y'
	abort = 'Y'
	createconfig(armed, fueling, fueled, launch, abort)


def launch(pfr):
	armed, fueling, fueled, launch = readconfig()
	print("XXXXX")
	if armed == 'Y' and fueled == 'Y':
		count = 10
		print('Starting Launching Squence')
		while (count !=  0):
			print(count)
			sleep(1)
			count = count - 1

		pfr.relays[1].turn_on()
		print('Lift Off')
		sleep(2)
		pfr.relays[1].toggle()
		fueling = 'N'
		launch = 'Y'
		createconfig(armed, fueling, fueled, launch)

def createconfig(Armed, Fueling, Fueled, Launch, Abort):
	cfgfile = open("launch.cfg",'w')
	Config = configparser.ConfigParser()
	Config.add_section('Launch_Settings')
	Config['Launch_Settings']['Armed'] = Armed
	Config['Launch_Settings']['Fueling'] = Fueling
	Config['Launch_Settings']['Fueled'] = Fueled
	Config['Launch_Settings']['Launch'] = Launch
	Config['Launch_Settings']['Abort'] = Abort
	Config.write(cfgfile)
	cfgfile.close()

def readconfig():
	print('Read Config Test')	
	Config = configparser.ConfigParser()
	Config.read("launch.cfg")
	armed = Config.get('Launch_Settings','Armed')
	fueling = Config.get('Launch_Settings', 'Fueling')
	fueled = Config.get('Launch_Settings', 'Fueled')
	launch = Config.get('Launch_Settings', 'Launch')
	abort = Config.get('Launch_Settings', 'Abort')
	print('Armed = ',armed)
	print('Fueling = ',fueling)
	print('Fueled = ', fueled)
	print('Launch = ', launch) 
	print('Abort = ', abort)
	return armed, fueling, fueled, launch, abort

if __name__ == "__main__":
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)

    reset()
    readconfig()		
    armed=arm()
#    unarm()
    beginfuel(pfr)
    fueled=endfuel(pfr)
    launch(pfr)
    
exit()





