#!/usr/bin/env python3

import re
import random
from subprocess import run
from winreg import HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, REG_SZ, ConnectRegistry, EnumValue, OpenKey, SetValueEx


def changeMacAddress():
    # MAC Addresses to attempt using. You will select one when the script is used.
    # You can change the names in this list or add names to this list.
    # Make sure you use 12 valid hexadecimal values. 
    # If the MAC address change fails try setting the second character to 2 or 6 or A or E,
    # for example: 0A1122334455 or 0A5544332211
    # If unsure, leave the MAC addresses listed here as is.
    # mac_to_change_to = ["0A1122334455", "0E1122334455", "021122334455", "061122334455"]

    # We create an empty list where we'll store all the MAC addresses.
    mac_address = None

    # We start off by creating a regular expression (regex) for MAC addresses.
    mac_add_regex = re.compile(r"([A-Za-z0-9]{2}[:-]){5}([A-Za-z0-9]{2})")

    # We start off by creating a regular expression (regex) for MAC addresses.
    mac_name_regex = re.compile(r"(Wi-Fi)")


    # We create a regex for the transport names. It will work in this case. 
    #  But when you use the .+ or .*, you should consider making it not as greedy.
    transport_name_regex = re.compile("({.+})")

    # We create regex to pick out the adapter index
    adapterIndex = re.compile("([0-9]+)")

    # Python allows us to run system commands by using a function provided by the module: 
    # (run(<list of command line arguments goes here>, 
    # <specify the second argument if you want to capture the output>))
    # The script is a parent process and creates a child process which runs the system command, 
    # and will only continue once the child process has completed.
    # To save the content that gets sent to the standard output stream (the terminal), 
    # we have to specify that we want to capture the output, so we specify the second 
    # argument as capture_output = True. This information gets stored in the stdout attribute. 
    # The information is stored in bytes and we need to decode it to Unicode before we use it
    # as a String in Python.
    # We use Python to run the getmac command, and then capture the output. 
    # We split the output at the newline so that we can work with the individual lines 
    # (which will contain the Mac and transport name).
    getmac_output = run("getmac /v", capture_output=True).stdout.decode().split('\n')

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
            mac_address = (nameFind.group(0), macFind.group(0),transportFind.group(0))
            break

    print(mac_address)

    # We know the first part of the key, we'll append the folders where we'll search the values
    controller_key_part = r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"

    # We connect to the HKEY_LOCAL_MACHINE registry. If we specify None, 
    # it means we connect to local machine's registry.
    with ConnectRegistry(None, HKEY_LOCAL_MACHINE) as hkey:
        # Create a list for the 21 folders. I used a list comprehension. The expression part of the list comprehension
        # makes use of a ternary operator. The transport value for you Mac Address should fall within this range. 
        # You could write multiple lines.
        controller_key_folders = [("\\000" + str(item) if item < 10 else "\\00" + str(item)) for item in range(0, 21)]

        # We now iterate through the list of folders we created.
        for key_folder in controller_key_folders:
            # We try to open the key. If we can't we just except and pass. But it shouldn't be a problem.
            # We have to specify the registry we connected to, the controller key 
            # (This is made up of the controller_key_part we know and the folder(key) name we created
            # with the list comprehension).
            try:
                with OpenKey(hkey, controller_key_part + key_folder, 0, KEY_ALL_ACCESS) as regkey:
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
                            name, value, type = EnumValue(regkey, count)
                            # To go to the next value if we didn't find what we're looking for we increment count.
                            count = count + 1

                            # We check to see if our "NetCfgInstanceId" is equal to our Transport number for our 
                            # selected Mac Address.
                        
                            if name == "NetCfgInstanceId" and value == mac_address[2]:
                                # new_mac_address = mac_to_change_to[int(update_option)]
                                new_mac_address = "02%02x%02x%02x%02x%02x" % (random.randint(0, 255),
                                                                                random.randint(0, 255),
                                                                                random.randint(0, 255),
                                                                                random.randint(0, 255),
                                                                                random.randint(0, 255))
                                SetValueEx(regkey, "NetworkAddress", 0, REG_SZ, new_mac_address)
                                print(new_mac_address)
                                print("Successly matched Transport Number")
                                # get list of adapters and find index of adapter you want to disable.
                        
                    except WindowsError:
                        pass
            except:
                pass


    # # Code to disable and enable Wireless devicess
    # run_disable_enable = input("Do you want to disable and reenable your wireless device(s). Press Y or y to continue:")
    # # Changes the input to lowercase and compares to y. If not y the while function which contains the last part will never run.
    # if run_disable_enable.lower() == 'y':
    #     run_last_part = True
    # else:
    #     run_last_part = False

    # run_last_part will be set to True or False based on above code.
    while True:

        # Code to disable and enable the network adapters
        # We get a list of all network adapters. You have to ignore errors, as it doesn't like the format the command returns the data in.
        network_adapters = run(["wmic", "nic", "get", "name,index"], capture_output=True).stdout.decode('utf-8', errors="ignore").split('\r\r\n')
        for adapter in network_adapters:
            # We get the index for each adapter
            adapter_index_find = adapterIndex.search(adapter.lstrip())

            # If there is an index and the adapter has wireless in description we are going to disable and enable the adapter
            if adapter_index_find and "Wireless" in adapter:
                disable = run(["wmic", "path", "win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "disable"],capture_output=True)
                # If the return code is 0, it means that we successfully disabled the adapter
                if(disable.returncode == 0):
                    print(f"Disabled {adapter.lstrip()}")
                # We now enable the network adapter again.
                enable = run(["wmic", "path", f"win32_networkadapter", "where", f"index={adapter_index_find.group(0)}", "call", "enable"],capture_output=True)
                # If the return code is 0, it means that we successfully enabled the adapter
                if (enable.returncode == 0):
                    print(f"Enabled {adapter.lstrip()}")

        # We run the getmac command again
        getmac_output = run("getmac", capture_output=True).stdout.decode()
        # We recreate the Mac Address as to shows up in getmac XX-XX-XX-XX-XX-XX format from the 12 character string we have. We split the string into strings of length 2 using list comprehensions and then. We use "-".join(list) to recreate the address
        # mac_add = "-".join([(mac_to_change_to[int(update_option)][i:i+2]) for i in range(0, len(mac_to_change_to[int(update_option)]), 2)])
        # # We want to check if Mac Address we changed to is in getmac output, if so we have been successful.
        # if mac_add in getmac_output:
        #     print("Mac Address Success")
        # Break out of the While loop. Could also change run_last_part to False.
        break