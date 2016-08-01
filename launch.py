from time import sleep
import pifacerelayplus


DELAY = 10.0  # seconds

def arm():
	print('Armed')
	armed = 'Y'

def unarm():
	print('Unarmed')
	armed = 'N'

def beginfuel():
	print('Being Fueling')
	fueling = 'Y'

def endfuel():
	print('End Fueling')
	fueling = 'N'
	fueled_complete = 'Y'

def launch(armed, fueled):
	if armed == 'Y' and fueled == 'Y':
		print('10')
		sleep(10)
		print('9')
		sleep(10)
		print('8')
		sleep(10)
		print('7')
		sleep(10)
		print('6')
		sleep(10)
		print('5')
		sleep(10)
		print('4')
		sleep(10)
		print('3')
		sleep(10)
		print('2')
		sleep(10)
		print('1')
		sleep(1)
		print('Lift Off')

if __name__ == "__main__":
    pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
    pfr.relays[0].toggle()
    #pfr.relays[0].turn_off()
    sleep(DELAY)
    pfr.relays[0].toggle()
    sleep(DELAY)
    print ('TWo')
	
    pfr.relays[0].toggle() 
    sleep(5)
    pfr.relays[0].toggle()		
    #pfr.relays[0].toggle()
    #pfr.relay_port.all_off()
    print('Three')
    pfr.relay_port.value = 0xAA
    pfr.relay_port.all_off()
    print('Four')
    pfr.relays[0].turn_on()
    pfr.relays[1].turn_on()
    pfr.relays[2].turn_on()
    pfr.relays[3].turn_on()
    print('Five')
    sleep(3)	
    pfr.relay_port.all_off()	
    print('Done')
    arm()
    unarm()
    beginfuel()
    endfuel()
    launch('Y', 'Y')			
#    beginfuel()
#    endfuel()
#    launch()
exit()





