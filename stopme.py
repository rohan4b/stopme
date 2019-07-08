
from PIL import Image
import random
import pyxhook
import os
#change this to your log file's path

folder=os.path.dirname(__file__)
f=open(folder+"/list.txt","r")
a=[]
for i in f:
    a.append(i[:-1])
string=''
#this function is called everytime a key is pressed.
def OnKeyPress(event):


  global string

  if event.Key.islower():
  	string=string+event.Key
  if event.Key=='space':
    string=''
  print(string)


  for i in a:
    if i in string:
        print('yes')

        b=random.choice(os.listdir(folder+'/images'))
        img = Image.open(folder+'/images/'+b)
        img.show()
        string=''
        break
    else:
        print('no')

  if string=='letmedestroyeverythingihaveworkedforinmylife':
    hook1.cancel()


hook1=pyxhook.HookManager()
hook1.KeyDown=OnKeyPress
hook1.HookKeyboard()
hook1.start()
