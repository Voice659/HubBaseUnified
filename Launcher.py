HubBaseExists = False
VersionBacklogExists = False
HubBaseJEExists = False
HubBaseUTExists = False
try:
    from bin.HB.HubBase import *
    HubBaseExists = True
except ImportError:
    pass
try:
    from bin.VB.VersionBacklog import *
    VersionBacklogExists = True
except ImportError:
    pass
try:
    from bin.HBJE.JsPort import *
    HubBaseJEExists = True
except ImportError:
    pass
try:
    from bin.HBUT.Main import *
    HubBaseUTExists = True
except ImportError:
    pass

MaxProgrammNumber = 0
print("HubBaseLauncher v0.0.2.0.00 (.py - 0.0.2.0.05; .js - 0.0.1.0.01)")
LaunchOptionsL = []
if HubBaseExists:
    LaunchOptionsL += ["hb"]
    MaxProgrammNumber += 1
if HubBaseJEExists:
    LaunchOptionsL += ["hbjs"]
    MaxProgrammNumber += 1
if VersionBacklogExists:
    LaunchOptionsL += ["vb"]
    MaxProgrammNumber += 1
if HubBaseUTExists:
    LaunchOptionsL += ["hbut"]
    MaxProgrammNumber += 1
print("HubBase - 0 or 1" if HubBaseExists else "", "HubBaseJE - 2" if HubBaseJEExists else "", "Version Backlog - 3" if VersionBacklogExists else "", "HubBaseUT - 4" if HubBaseUTExists else "", sep=", ")
try:
    LaunchOptionInput = int(input("What to launch? -- "))
except ValueError:
    print("Enter a number next time", "Using default - option 1", sep="\n")
    LaunchOptionInput = 1
try:
    LaunchOptionInput = LaunchOptionsL[LaunchOptionInput - 1]
except IndexError:
    print(f"Enter a number in the range 0-{MaxProgrammNumber}")
if LaunchOptionInput == "hb":
    Setup_HubBase()
    Enter()
    Code()
    dev_console()
elif LaunchOptionInput == "hbjs":
    print("HubBase-onJS PyPort 0.0.1.0.01 (python port, May 18 2026, 18:50:26)")
    P1(10)
    P2()
    P3()
    print("Original programms:")
    OP1()
elif LaunchOptionInput == "vb":
    view_Log()
elif LaunchOptionInput == "hbut":
    Showcase()
