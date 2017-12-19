
g=open("res.html", "w")

ok_bold = 1
ok_ita = 1
ok_code = 1
ok_bullet = 0

def Headers ( line ) :
    counter = 0
    global ok_bold, ok_ita, ok_code
    word=line.split()[0]
    for letter in range(len(word)):
        if word[letter] == "#":
            counter += 1
    g.write("<h%d>" %(counter))
    for word in line.split()[1:]:
        if word == '__':
            bold(ok_bold)
            ok_bold += 1
        elif word == '*':
            italic(ok_ita)
            ok_ita += 1
        elif word == '`' :
            code( ok_code )
            ok_code += 1
        else:
            g.write(word.strip() + " ")
    g.write("</h%d>\n" % (counter))
    return


def Paragraph ( line ) :
    global ok_bold, ok_ita, ok_code
    g.write("<p>")
    for word in line.split()[0:]:
        if word == '__':
            bold(ok_bold)
            ok_bold += 1
        elif word == '*':
            italic(ok_ita)
            ok_ita += 1
        elif word == '`':
            code(ok_code)
            ok_code += 1
        else:
            g.write(word.strip() + " ")
    g.write("</p>\n")
    return



def bold ( ok ) :
    if ok % 2 == 1:
        g.write("<strong>")
    else:
        g.write("</strong>")
    return


def italic ( ok ) :
    if ok % 2 == 1:
        g.write("<em>")
    else:
        g.write("</em>")
    return


def new_line() :
    g.write("<br \>")
    return


def code ( ok ) :
    if ok %2 == 1:
        g.write("<code>")
    else :
        g.write("</code>")


def bullet_list ( line ) :
    global ok_bullet
    if ok_bullet == 0:
        g.write("<ul>\n")
        ok_bullet = 1
    global ok_bold, ok_ita, ok_code
    g.write("<li>")
    for word in line.split()[1:]:
        if word == '__':
            bold(ok_bold)
            ok_bold += 1
        elif word == '*':
            italic(ok_ita)
            ok_ita += 1
        elif word == '`':
            code(ok_code)
            ok_code += 1
        else:
            g.write(word.strip() + " ")
    g.write("</li>\n")
    return



def deleteContent(file):
    file.seek(0)
    file.truncate()

deleteContent(g)
last_line = "-"
with open('foo.txt') as f:
    for line in f:
        if last_line.lstrip().startswith('-') and line.lstrip().startswith('-') == False :
            g.write('</ul>\n')
        if line.lstrip().startswith('#'):
            Headers( line )
        elif line.lstrip().startswith('-'):
            bullet_list( line )
        else:
            Paragraph( line )
        last_line = line

