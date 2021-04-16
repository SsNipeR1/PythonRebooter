import os
#rebooter
print("Write R to reboot, P to power off, N to exit.")
choice = input(">> ").lower()
if choice == "p":
    os.system("su && poweroff")
elif choice == "r":
    os.system("su && reboot")
else:
    exit() 
