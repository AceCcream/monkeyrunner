import time
import sys
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

now = time.strftime("%Y-%m-%d-%H-%M-%S")
path='d:\picture'
logpath='d:\log\log'

name = sys.argv[0].split('\\')
filename = name[len(name)-1]

log = open(logpath+filename[0:-3]+"-log"+now+".txt",'w')
device = MonkeyRunner.waitForConnection(5)

device.removePackage("com.kittyplay.ex")
device.installPackage("KittyPlay_v3.1.8_release_20151104.apk")
log.write("apk installing")
MonkeyRunner.sleep(2)

# start mainactivity and enter the homepage
device.startActivity(component='com.kittyplay.ex/com.jiubang.kittyplay.MainActivity')
MonkeyRunner.sleep(5)

device.drag((552,754),(12,754),2,2)
MonkeyRunner.sleep(2)
device.touch(530,1108,"DOWN_AND_UP")

# pull the sidebar out
device.startActivity(component='com.kittyplay.ex/com.jiubang.kittyplay.ui.activity.drawer.DownloadManageActivity')


