from django.shortcuts import render , redirect
from django.http import HttpResponse
import MySQLdb
def createMsg(request):
    if request.method == "POST":
        conn = MySQLdb.connect(user='root' , password='root1234*/' , db='guestbook' , host='localhost')
        cur = conn.cursor()
        name = request.POST.get('username')
        message = request.POST.get('message')
        cur.execute('CREATE TABLE IF NOT EXISTS `gustmsg` (`ID` INT NOT NULL AUTO_INCREMENT PRIMARY KEY , `name` VARCHAR(250) NOT NULL , `msg` VARCHAR(500) NOT NULL)') 
        sqlinsert = ("INSERT INTO `gustmsg`(name,msg)VALUES('{}','{}')".format(name,message))
        cur.execute(sqlinsert)
        conn.commit()
        conn.close()
        return redirect('allmessage')
    else:
        return render(request,'guestmsg/createone.html' , {})
def allMessage(request):
    conn = MySQLdb.connect(user='root' , password='root1234*/' , db='guestbook' , host='localhost')
    cur = conn.cursor()
    cur.execute('select name,msg from gustmsg')
    guestbooksname = []
    guestbooksage = []
    for list in cur.fetchall():
        guestbooksname.append(list[0])
        guestbooksage.append(list[1])            
    context = {
        'guestbooksname':guestbooksname,
        'guestbooksage':guestbooksage,
    }
    return render(request,'guestmsg/home.html',context)