##Avaiables eviroment
commands = {
        1 : 'ping www.google.com' #Check connected networks
        2 : 'netsh wlan add profile filename = "{path}"' #Add profile of networks
        3 : 'netsh wlan delete profile name = "{ssid}"' #Delete profile of any networks
        4 : 'netsh wlan connect name = "{ssid}"' #Connect to network have name is "{ssid}"
        5 : 'netsh wlan disconnect' #Disconnect internet
        6 : 'netsh wlan show profile' #Show all profile of network saved in PC
        }
resultFail = {
        1 : 'Ping request could not find host www.google.com. Please check the name and try again.'
        2 : 'Error'
        3 : 'Error'
        4 : 'Error'
        5 : 'Error'
        6 : 'Error'
        }
##Lib
import XMLWirelessWindows as Wireless
:q
