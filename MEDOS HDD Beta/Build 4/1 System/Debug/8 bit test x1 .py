count = int
in1 = str
print ("Opening debug tool: 8 bit count")
print ("This command tests your system to see if it can count to an 8 bit integer of 256")
print ("{system} file selected: 8BITTESTX1.PY")
print ("Ready to launch!")
print ("Estimated time:")
print ("8 MB RAM = 148 seconds:")
print ("16 MB RAM = 132 seconds")
print ("32 MB RAM = 120 seconds")
print ("64 MB RAM = 80 seconds")
print ("128 MB RAM = 72 seconds")
print ("256 MB RAM = 64 seconds")
print ("512 MB RAM = 50 seconds")
print ("1028 MB RAM = 32 seconds")
print ("1500 MB RAM = 10 seconds")
print ("2056 MBB RAM = 5 seconds")
print ("Are you ready?")
print ("Type 'OPEN' to try out command")
in1 = str(input("FC://"))
if in1 == ("OPEN"):
	count = 0
	count = int
	count =+ 1
	print (count)
while not (count > 256):
    count += 1
    print (count)
else:
        print ("You have successfully counted to a 8 bit integer")
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    