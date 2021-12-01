def swapFileData():
    fileName1=input("enter the file name")
    fileName2=input("enter the file name")
    with open (fileName1,"r" ) as a:
        dataa=a.read()
    with open (fileName2,"r") as b:
        datab=b.read()
    with open (fileName1,"w") as a:
        a.write(datab)
    with open (fileName2,"w") as b:
        b.write(dataa)
    print ("swiped")
swapFileData()