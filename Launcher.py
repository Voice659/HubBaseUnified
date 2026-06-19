from bin.HB.HubBase import *
from bin.VB.VersionBacklog import *
from bin.HBJE.JsPort import *

print("HubBaseLauncher v0.0.1.0.0 (.py - 0.0.2.0.05; .js - 0.0.1.0.00)")
LaunchOptions = {1: "hb.py", 2: "jsport.js", 3: "vb.py"}
LaunchOptionsL = ["hb", "jsport", "vb"]
print(LaunchOptions)
LaunchOptionInput = int(input("What to launch?[1,2,3] -- "))
LaunchOptionInput = LaunchOptionsL[LaunchOptionInput - 1]
if LaunchOptionInput == "hb":
    global RA, VipAccess
    RA = 0
    Enter()
    Code()
    dev_console()
elif LaunchOptionInput == "jsport":
    print("HubBase-onJS PyPort 0.0.1.0.01 (default, May 18 2026, 18:50:26)")
    P1(10)
    P2()
    P3()
    print("Original programms:")
    OP1()
elif LaunchOptionInput == "vb":
    view_Log()
