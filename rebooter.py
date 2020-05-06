import os
#rebooter
choice = input("Write R to reboot, P to power off, N to exit.")
if choice == P or choice == p:
    os.system("su && poweroff")
elif choice == R or choice == r:
    os.system("su && reboot")
else:
    exit()
