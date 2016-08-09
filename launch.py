from time import sleep
import pifacerelayplus
import configparser




def reset():
	armed = 'N'
	fueling = 'N'
	fueled = 'N'
	launch = 'N'
	createconfig(armed, fueling, fueled, launch)

def arm():
	print('Armed')
	armed = 'Y'
	fueling = 'N'
	fueled = 'N'
	launch = 'N'
	createconfig(armed, fueling, fueled, launch)
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
	createconfig(armed, fueling, fueled, launch) 
	pfr.relays[0].turn_on()
	sleep(10)

def endfuel(pfr):
	print('End Fueling')
	armed = 'Y'
	fueling = 'N'
	fueled = 'Y'
	launch = 'N'
	pfr.relays[0].toggle() 
	createconfig(armed, fueling, fueled, launch)
	return fueled

def abort():
	a=0

def launch(pfr):
	armed, fueling, fueled, launch = readconfig()
	print("XXXXX")
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
		fueling = 'N'
		launch = 'Y'
		createconfig(armed, fueling, fueled, launch)

def createconfig(Armed, Fueling, Fueled, Launch):
	cfgfile = open("launch.cfg",'w')
	Config = configparser.ConfigParser()
	Config.add_section('Launch_Settings')
	Config['Launch_Settings']['Armed'] = Armed
	Config['Launch_Settings']['Fueling'] = Fueling
	Config['Launch_Settings']['Fueled'] = Fueled
	Config['Launch_Settings']['Launch'] = Launch
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
	print('Armed = ',armed)
	print('Fueling = ',fueling)
	print('Fueled = ', fueled)
	print('Launch = ', launch) 
	return armed, fueling, fueled, launch

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





