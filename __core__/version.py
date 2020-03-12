global uver
x = open("Update.bruh","r")
version = x.readline()
n = version.split()
uver = round(float(n[1])+0.1,1)
x.close()




def write():
    m = open("Update.bruh","w")
    m.write(str(n[0])+" "+str(uver))
    m.close()

