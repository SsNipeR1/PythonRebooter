#rebooter
rnp = input("Write R to reboot, P to power off, N to exit.")
if rnp == P or rnp == p:
    import os
    os.system('tsu && poweroff')
elif rnp == R or rnp == r:
    import os
    os.system("tsu && reboot")
else:
    exit()