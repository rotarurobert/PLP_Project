
g = open("res.html" , "w")
f = open("foo.txt")

def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def Headers ( str ) :
    counter = 1
    for i in range(len(str)-1) :
            if  str[i] == str[i+1] and str[i] == '*' :
                counter += 1
            else:
                break
    g.write("<h%d> %s </h%d>\n" %(counter,str[counter:].strip("\n"),counter))
    return

def paragraph ( str ) :
    g.write("<p> %s </p>" %(str))


def bold ( str ) :
    g.write("<strong> %s </strong>\n" % (str[2:].strip("\n")))
    return



def italic ( str ) :

    g.write("<em> %s </em>\n" % (str[1:].strip("\n")))
    return

deleteContent(g)
for line in f:
    a = line
    print (a.split())
    print (a[len(a)-2:len(a)-1])
    print (a[0])
    print (a)
    if( a[0] == '*' ):
        Headers( a )
    elif a[0:2] == '__' :
        bold(a)
    elif a[0] == '_' :
        italic( a )
    else:
        paragraph( a )


f.close()
g.close()
