import re
import subprocess
from random import choice,randint

inp = input("Enter 1 per te vendosur mac adresen manualisht ose 2 per mac adres automatikisht: ").strip()
interface = input("Enter network interface tuaj: ").strip()

def main():
    if inp == "1":
        interface = input("Enter network interface tuaj: ").strip()
        new_mac = input("Enter mac adresen e re: ").strip()
        change_mac(interface,new_mac)
    elif inp == "2":
        random = random_mac()
        print(random)
        change_mac(interface,random)

def random_mac():
    cisco = ["00","40","96"]
    dell = ["00","14","22"]
    mac_address = choice([cisco,dell])

    for i in range(3):
        one = choice(str(randint(0,9)))
        two = choice(str(randint(0,9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig "+str(interface)+ " down"], shell = True)
    subprocess.call(["ifconfig "+str(interface)+ " hw ether"+ str(new_mac)], shell = True)
    subprocess.call(["ifconfig "+str(interface)+ " up"], shell = True)

def CurrentMac():
    output = subprocess.check_output(["ifconfig " + "eth0"], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
    print("Mac adresa e vjeter eshte: {}".format(current_mac))

if __name__ == "__main__":
    main()
