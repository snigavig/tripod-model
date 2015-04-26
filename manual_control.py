import serial
import Tkinter

__author__ = 'snigavig'

PORT = '/dev/ttyACM0'
SPEED = 9600
top = Tkinter.Tk()


def sendCommand(servonum):
    connection = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)
    connection.write(str(servonum))
    connection.close()


def BBackVerticalBottomPlusCallBack():
    sendCommand(0)


def BBackVerticalBottomMinusCallBack():
    sendCommand(0)


def BBackVerticalTopPlusCallBack():
    sendCommand(1)


def BBackVerticalTopMinusCallBack():
    sendCommand(1)


def BBackHorizontalPlusCallBack():
    sendCommand(14)


def BBackHorizontalMinusCallBack():
    sendCommand(14)


def BLeftVerticalBottomPlusCallBack():
    sendCommand(8)


def BLeftVerticalBottomMinusCallBack():
    sendCommand(8)


def BLeftVerticalTopPlusCallBack():
    sendCommand(9)


def BLeftVerticalTopMinusCallBack():
    sendCommand(9)


def BLeftHorizontalPlusCallBack():
    sendCommand(10)


def BLeftHorizontalMinusCallBack():
    sendCommand(10)


def BRightVerticalBottomPlusCallBack():
    sendCommand(11)


def BRightVerticalBottomMinusCallBack():
    sendCommand(11)


def BRightVerticalTopPlusCallBack():
    sendCommand(12)


def BRightVerticalTopMinusCallBack():
    sendCommand(12)


def BRightHorizontalPlusCallBack():
    sendCommand(13)


def BRightHorizontalMinusCallBack():
    sendCommand(13)


BBackVerticalBottomPlus = Tkinter.Button(top, text="BackVerticalBottom+", command=BBackVerticalBottomPlusCallBack)
BBackVerticalBottomMinus = Tkinter.Button(top, text="BackVerticalBottom-", command=BBackVerticalBottomMinusCallBack)
BBackVerticalTopPlus = Tkinter.Button(top, text="BackVerticalTop+", command=BBackVerticalTopPlusCallBack)
BBackVerticalTopMinus = Tkinter.Button(top, text="BackVerticalTop-", command=BBackVerticalTopMinusCallBack)
BBackHorizontalPlus = Tkinter.Button(top, text="BackHorizontal+", command=BBackHorizontalPlusCallBack)
BBackHorizontalMinus = Tkinter.Button(top, text="BackHorizontal-", command=BBackHorizontalMinusCallBack)
BLeftVerticalBottomPlus = Tkinter.Button(top, text="LeftVerticalBottom+", command=BLeftVerticalBottomPlusCallBack)
BLeftVerticalBottomMinus = Tkinter.Button(top, text="LeftVerticalBottom-", command=BLeftVerticalBottomMinusCallBack)
BLeftVerticalTopPlus = Tkinter.Button(top, text="LeftVerticalTop+", command=BLeftVerticalTopPlusCallBack)
BLeftVerticalTopMinus = Tkinter.Button(top, text="LeftVerticalTop-", command=BLeftVerticalTopMinusCallBack)
BLeftHorizontalPlus = Tkinter.Button(top, text="LeftHorizontal+", command=BLeftHorizontalPlusCallBack)
BLeftHorizontalMinus = Tkinter.Button(top, text="LeftHorizontal-", command=BLeftHorizontalMinusCallBack)
BRightVerticalBottomPlus = Tkinter.Button(top, text="RightVerticalBottom+", command=BRightVerticalBottomPlusCallBack)
BRightVerticalBottomMinus = Tkinter.Button(top, text="RightVerticalBottom-", command=BRightVerticalBottomMinusCallBack)
BRightVerticalTopPlus = Tkinter.Button(top, text="RightVerticalTop+", command=BRightVerticalTopPlusCallBack)
BRightVerticalTopMinus = Tkinter.Button(top, text="RightVerticalTop-", command=BRightVerticalTopMinusCallBack)
BRightHorizontalPlus = Tkinter.Button(top, text="RightHorizontal+", command=BRightHorizontalPlusCallBack)
BRightHorizontalMinus = Tkinter.Button(top, text="RightHorizontal-", command=BRightHorizontalMinusCallBack)

BBackVerticalBottomPlus.pack()
BBackVerticalBottomMinus.pack()
BBackVerticalTopPlus.pack()
BBackVerticalTopMinus.pack()
BBackHorizontalPlus.pack()
BBackHorizontalMinus.pack()
BLeftVerticalBottomPlus.pack()
BLeftVerticalBottomMinus.pack()
BLeftVerticalTopPlus.pack()
BLeftVerticalTopMinus.pack()
BLeftHorizontalPlus.pack()
BLeftHorizontalMinus.pack()
BRightVerticalBottomPlus.pack()
BRightVerticalBottomMinus.pack()
BRightVerticalTopPlus.pack()
BRightVerticalTopMinus.pack()
BRightHorizontalPlus.pack()
BRightHorizontalMinus.pack()

top.mainloop()