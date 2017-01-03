settings=open(".git/config","a+")

foundUserRemote=False
foundPUSHUrl=False
remoteLine=-1
iLine=0
for line in settings.readlines():
    if line.find("[remote") != -1:
        remoteName=line.split("\"")[1]
        print remoteName
        if remoteName!="origin":
            foundUserRemote=True
            remoteLine=iLine
    if foundUserRemote:
        if line.find("pushurl")!=-1:
            print line
            foundPUSHUrl=True
        if line.find("[")!=-1:
            print "found new section; breaking"
            break
    iLine=iLine+1

if not foundUserRemote:
    print "No user remote found; need to 'git remote add ...'"
elif foundPUSHUrl:
    print "Found pushurl; do nothing"
else:
    print "need to add line with username",remoteLine
    


print "done"
settings.close()
