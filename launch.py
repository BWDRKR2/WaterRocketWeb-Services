from time import sleep
import pifacerelayplus


DELAY = 10.0  # seconds


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
    sleep(30)	
    pfr.relay_port.all_off()	
	
print('Done')
exit()
