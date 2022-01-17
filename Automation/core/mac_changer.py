
from abc import ABC, abstractmethod
import re
import random
import subprocess
import subprocess
import winreg

class MacChanger(ABC):
    
    def __init__(self, adapter_name) -> None:
        """Create mac address changer instance"""
        self.adapter_name = adapter_name

    def reset_adapter(self) -> None:
        """Display and enable the adapter after changing its mac address"""
        
        # We create regex to pick out the adapter index
        adapterIndex = re.compile("([0-9]+)")
    
        while(True):
            

            # Code to disable and enable the network adapters
            # We get a list of all network adapters. You have to ignore errors, as it doesn't like the format the command returns the data in.
            network_adapters = subprocess.run(["wmic", "nic", "get", "name,index"], capture_output=True).stdout.decode('utf-8', errors="ignore").split('\r\r\n')
            for adapter in network_adapters:
                # We get the index for each adapter
                adapter_index_find = adapterIndex.search(adapter.lstrip())

                # If there is an index and the adapter has wireless in description we are going to disable and enable the adapter
                if adapter_index_find and self.adapter_name in adapter:
                    disable = subprocess.run(["wmic", "path", "win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "disable"],capture_output=True)
                    # If the return code is 0, it means that we successfully disabled the adapter
                    # if(disable.returncode == 0):
                    #     print(f"Disabled {adapter.lstrip()}")
                    # We now enable the network adapter again.
                    enable = subprocess.run(["wmic", "path", f"win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "enable"],capture_output=True)
                    # If the return code is 0, it means that we successfully enabled the adapter
                    # if (enable.returncode == 0):
                    #     print(f"Enabled {adapter.lstrip()}")

            # Break out of the While loop. Could also change run_last_part to False.
            break
            
    def change_address(self, desire_mac_address = None):
        """Change the mac address"""

        # We get the current mac address
        adapter_name, old_mac_address, transport_num = self.get_current_mac_address()
        
        if(desire_mac_address != None and desire_mac_address == ''.join(old_mac_address.lower().split('-'))):
            return (old_mac_address, desire_mac_address)

        # We know the first part of the key, we'll append the folders where we'll search the values
        controller_key_part = r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"

        # We connect to the HKEY_LOCAL_MACHINE registry. If we specify None, 
        # it means we connect to local machine's registry.
        with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
            # Create a list for the 21 folders. I used a list comprehension. The expression part of the list comprehension
            # makes use of a ternary operator. The transport value for you Mac Address should fall within this range. 
            # You could write multiple lines.
            controller_key_folders = [("\\000" + str(item) if item < 10 else "\\00" + str(item)) for item in range(0, 30)]

            # We now iterate through the list of folders we created.
            for key_folder in controller_key_folders:
                # We try to open the key. If we can't we just except and pass. But it shouldn't be a problem.
                # We have to specify the registry we connected to, the controller key 
                # (This is made up of the controller_key_part we know and the folder(key) name we created
                # with the list comprehension).
                try:
                    with winreg.OpenKey(hkey, controller_key_part + key_folder, 0, winreg.KEY_ALL_ACCESS) as regkey:
                        # We will now look at the Values under each key and see if we can find the "NetCfgInstanceId" 
                        # with the same Transport Id as the one we selected.
                        try:
                            # Values start at 0 in the registry and we have to count through them. 
                            # This will continue until we get a WindowsError (Where we will then just pass) 
                            # then we'll start with the next folder until we find the correct key which contains 
                            # the value we're looking for.
                            count = 0
                            while True:
                                # We unpack each individual winreg value into name, value and type.
                                name, value, type = winreg.EnumValue(regkey, count)
                                # To go to the next value if we didn't find what we're looking for we increment count.
                                count = count + 1

                                # We check to see if our "NetCfgInstanceId" is equal to our Transport number for our 
                                # selected Mac Address.
                                if name == "NetCfgInstanceId" and value == transport_num:
                                    # new_mac_address = mac_to_change_to[int(update_option)]
                                    
                                    if(desire_mac_address == None):

                                        new_mac_address = "02%02x%02x%02x%02x%02x" % (random.randint(0, 255),
                                                                                        random.randint(0, 255),
                                                                                        random.randint(0, 255),
                                                                                        random.randint(0, 255),
                                                                                        random.randint(0, 255))
                                    elif(desire_mac_address != None):
                                        new_mac_address = desire_mac_address

                                    winreg.SetValueEx(regkey, "NetworkAddress", 0, winreg.REG_SZ, new_mac_address)
                                    # print("Successly matched Transport Number")

                                else:
                                    # print("Unsuccessly matched Transport Number")
                                    pass

                        except WindowsError:
                            pass
                except:
                    pass

        # run_last_part will be set to True or False based on above code.
        if(old_mac_address is not []):
            self.reset_adapter()
            return (old_mac_address, new_mac_address)

        return (None, None)


    def change_mac_address(self, prev_mac_address = None):
        """Generate or Change the mac address for each account"""

        # Change MAC address (from execl or generate new one)
        desire_mac_address = str(prev_mac_address) if(isinstance(prev_mac_address, str)) else None
        old_mac_address, new_mac_address = self.change_address(desire_mac_address)

        print(f"Previouse MAC address: {old_mac_address}")
        print(f"New MAC address: {new_mac_address}")

        return new_mac_address

    @abstractmethod
    def get_current_mac_address(self) -> str:
        """Get current mac address for related adapter"""

class WifiMacChanger(MacChanger):

    def __init__(self, adapter_name) -> None:
        super().__init__(adapter_name)
    

    def get_current_mac_address(self) -> str:
        # We start off by creating a regular expression (regex) for MAC addresses.
        mac_add_regex = re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")

        # We create a regex for the transport names. It will work in this case. 
        #  But when you use the .+ or .*, you should consider making it not as greedy.
        transport_name_regex = re.compile("({.+})")

        # we create regex to searech for Wi-Fi trasport
        mac_name_regex = re.compile(r"(Wi-Fi)")

        getmac_output = subprocess.run("getmac /v", capture_output=True).stdout.decode(encoding='ISO-8859-1').split('\n')
    
        # We loop through the output
        for macAdd in getmac_output:
            # We use the regex to find the Mac Addresses.
            macFind = mac_add_regex.search(macAdd)

            # We use the regex to find the transport name.
            transportFind = transport_name_regex.search(macAdd)
            
            # We use the regex to find the transport name.
            nameFind = mac_name_regex.search(macAdd)


            # If you don't find a Mac Address or Transport name the option won't be listed.
            # if macFind == None or transportFind == None or nameFind == None:
            #     continue

            if macFind != None and transportFind != None and nameFind != None:
                
                # We append a tuple with the Mac Address and the Transport name to a list.
                old_mac_address = (nameFind.group(0), macFind.group(0),transportFind.group(0))

                return old_mac_address
    
class EthernetMacChanger(MacChanger):

    def __init__(self, adapter_name) -> None:
        super().__init__(adapter_name)
        
    def get_current_mac_address(self) -> str:
        # We start off by creating a regular expression (regex) for MAC addresses.
        mac_add_regex = re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")

        # We create a regex for the transport names. It will work in this case. 
        #  But when you use the .+ or .*, you should consider making it not as greedy.
        transport_name_regex = re.compile("({.+})")

        # we create regex to searech for Ethernet trasport
        mac_name_regex = re.compile(r"(Ethernet)")

        getmac_output = subprocess.run("getmac /v", capture_output=True).stdout.decode(encoding='ISO-8859-1').split('\n')
    
        # We loop through the output
        for macAdd in getmac_output:
            # We use the regex to find the Mac Addresses.
            macFind = mac_add_regex.search(macAdd)

            # We use the regex to find the transport name.
            transportFind = transport_name_regex.search(macAdd)
            
            # We use the regex to find the transport name.
            nameFind = mac_name_regex.search(macAdd)


            # If you don't find a Mac Address or Transport name the option won't be listed.
            # if macFind == None or transportFind == None or nameFind == None:
            #     continue

            if macFind != None and transportFind != None and nameFind != None:
                
                # We append a tuple with the Mac Address and the Transport name to a list.
                old_mac_address = (nameFind.group(0), macFind.group(0),transportFind.group(0))

                return old_mac_address
    


# If the MAC address change fails try setting the second character to 2 or 6 or A or E,
# for example: 0A1122334455 or 0A5544332211
# If unsure, leave the MAC addresses listed here as is.
# mac_to_change_to = ["0A1122334455", "0E1122334455", "021122334455", "061122334455"]
# changeMacAddress(desire_mac_address="107B440E40BC")