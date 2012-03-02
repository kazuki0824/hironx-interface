#!/opt/grx/bin/hrpsyspy
import os
import time
from java.lang import System
from java.awt import *
from javax.swing import *
from javax.swing.border import BevelBorder 

from guiinfo import *
import math

FILENAME_ROBOTHOST='.robothost'
txt = None 

def hostname():
    try:
        return __hostname
    except NameError:
        if os.path.isfile(FILENAME_ROBOTHOST):
            f = open(FILENAME_ROBOTHOST, "r")
            __hostname = f.readline().strip()
            f.close()
        else:
            __hostname = "localhost"
        print "hostname:", __hostname
        return __hostname

def reconnect():
  robotHost = hostname()
  System.setProperty('NS_OPT', '-ORBInitRef NameService=corbaloc:iiop:'+ robotHost +':2809/NameService')
  try:
    rtm.initCORBA()
    f = open(FILENAME_ROBOTHOST, 'w')
    f.write(robotHost+'\n')
    f.close()
    print ('reconnected')
    return True
  except IOError:
    print ('can not open to write: '+ FILENAME_ROBOTHOST)
  except:
    print ('can not connect to '+ robotHost)
  return False

def setupRobot():
  if reconnect():
    init()
    setupLogger()

def restart():
  waitInputConfirm('!! Caution !! \n Push [OK] to restart rtcd ')
  if reconnect():
    ms = rtm.findRTCmanager()
    ms.restart()

def createButton(name, func):
    if not func.__class__.__name__ == 'function':
       return None
    exec('def tmpfunc(e): import time; t1=time.time();'+func.__name__+'(); t2=time.time(); print "['+name+']", t2- t1 ,"[sec]"')
    btn = JButton(label=name, actionPerformed = tmpfunc)
    del tmpfunc
    return btn

def createFrame():
  global funcList,txt
  funcList = [["setup rt-system", setupRobot],["restart rtcd", restart], " "] + funcList
  frm = JFrame("sample GUI for "+bodyinfo.modelName, defaultCloseOperation = JFrame.EXIT_ON_CLOSE)
  frm.setAlwaysOnTop(True)
  pnl = frm.getContentPane()
  pnl.layout = BoxLayout(pnl, BoxLayout.X_AXIS)
  pnlId = 0
  pnlCount = 0
  MAX_OBJ_NUM = 30
  for i,func in enumerate(funcList):
    obj = None
    if func.__class__.__name__ == 'str':
      if func == '\n':
        pnlCount = MAX_OBJ_NUM
      else:
        obj = JLabel(func)
    elif func.__class__.__name__ == 'function':
      obj = createButton(func.__name__, func)
    elif func.__class__.__name__ == 'list':
      obj = createButton(func[0], func[1])
  
    if obj != None:
      if pnl.getComponentCount() < pnlId+1:
        p = JPanel()
        p.setBorder(BevelBorder(BevelBorder.RAISED))
        p.layout = BoxLayout(p, BoxLayout.Y_AXIS)
        p.setAlignmentY(Component.TOP_ALIGNMENT)
        if pnlId == 0:
          p.add(JLabel("HOSTNAME of ROBOT"))
          if os.path.isfile(FILENAME_ROBOTHOST):
            f = open(FILENAME_ROBOTHOST, "r")
            txt = JTextField(f.readline())
          else:
            txt = JTextField("localhost")
          p.add(txt)
        pnl.add(p)
      pnl.getComponent(pnlId).add(obj)
  
    pnlCount += 1
    if pnlCount > MAX_OBJ_NUM:
      print func
      pnlCount = 0 
      pnlId += 1
  return frm
  
if __name__ == '__main__' or __name__ == 'main':
  frm = createFrame()
  frm.pack()
  frm.show()
