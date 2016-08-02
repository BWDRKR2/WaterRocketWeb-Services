from time import sleep
import pifacerelayplus


DELAY = 10.0  # seconds

def arm():
	print('Armed')
	armed = 'Y'
	return armed

def unarm():
	print('Unarmed')
	armed = 'N'
	return armed

def beginfuel(pfr):
	print('Being Fueling')
	fueling = 'Y'
	pfr.relays[0].turn_on()
	sleep(20)

def endfuel(pfr):
	print('End Fueling')
	fueling = 'N'
	pfr.relays[0].toggle() 
	fueled_complete = 'Y'
	return fueled_complete

def launch(pfr, armed, fueled):
	if armed == 'Y' and fueled == 'Y':
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
		sleep(5)
		pfr.relays[1].toggle()

if __name__ == "__main__":
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
#    pfr.relays[0].toggle()
    #pfr.relays[0].turn_off()
#    sleep(DELAY)
#    pfr.relays[0].toggle()
#    sleep(DELAY)
#    print ('TWo')
	
#    pfr.relays[0].toggle() 
#    sleep(5)
#    pfr.relays[0].toggle()		
    #pfr.relays[0].toggle()
    #pfr.relay_port.all_off()
#    print('Three')
#    pfr.relay_port.value = 0xAA
#    pfr.relay_port.all_off()
#    print('Four')
#    pfr.relays[0].turn_on()
#    pfr.relays[1].turn_on()
#    pfr.relays[2].turn_on()
#    pfr.relays[3].turn_on()
#    print('Five')
#    sleep(3)	
#    pfr.relay_port.all_off()	
#    print('Done')
    armed=arm()
    unarm()
    beginfuel(pfr)
    fueled=endfuel(pfr)
    launch(pfr,armed, fueled)
    
				
#    beginfuel()
#    endfuel()
#    launch()
exit()





