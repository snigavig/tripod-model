import serial
import Tkinter

__author__ = 'snigavig'

PORT = '/dev/ttyACM0'
SPEED = 9600
top = Tkinter.Tk()


def send_command(servonum):
    connection = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)
    connection.write(str(servonum))
    connection.close()


def back_vertical_bottom_plus_callback():
    send_command(0)


def back_vertical_bottom_minus_callback():
    send_command(0)


def back_vertical_top_plus_callback():
    send_command(1)


def back_vertical_top_minus_callback():
    send_command(1)


def back_horizontal_plus_callback():
    send_command(14)


def back_horizontal_minus_callback():
    send_command(14)


def left_vertical_bottom_plus_callback():
    send_command(8)


def left_vertical_bottom_minus_callback():
    send_command(8)


def left_vertical_top_plus_callback():
    send_command(9)


def left_vertical_top_minus_callback():
    send_command(9)


def left_horizontal_plus_callback():
    send_command(10)


def left_horizontal_minus_callback():
    send_command(10)


def right_vertical_bottom_plus_callback():
    send_command(11)


def right_vertical_bottom_minus_callback():
    send_command(11)


def right_vertical_top_plus_callback():
    send_command(12)


def right_vertical_top_minus_callback():
    send_command(12)


def right_horizontal_plus_callback():
    send_command(13)


def right_horizontal_minus_callback():
    send_command(13)


BBackVerticalBottomPlus = Tkinter.Button(top, text="BackVerticalBottom+", command=back_vertical_bottom_plus_callback)
BBackVerticalBottomMinus = Tkinter.Button(top, text="BackVerticalBottom-", command=back_vertical_bottom_minus_callback)
BBackVerticalTopPlus = Tkinter.Button(top, text="BackVerticalTop+", command=back_vertical_top_plus_callback)
BBackVerticalTopMinus = Tkinter.Button(top, text="BackVerticalTop-", command=back_vertical_top_minus_callback)
BBackHorizontalPlus = Tkinter.Button(top, text="BackHorizontal+", command=back_horizontal_plus_callback)
BBackHorizontalMinus = Tkinter.Button(top, text="BackHorizontal-", command=back_horizontal_minus_callback)
BLeftVerticalBottomPlus = Tkinter.Button(top, text="LeftVerticalBottom+", command=left_vertical_bottom_plus_callback)
BLeftVerticalBottomMinus = Tkinter.Button(top, text="LeftVerticalBottom-", command=left_vertical_bottom_minus_callback)
BLeftVerticalTopPlus = Tkinter.Button(top, text="LeftVerticalTop+", command=left_vertical_top_plus_callback)
BLeftVerticalTopMinus = Tkinter.Button(top, text="LeftVerticalTop-", command=left_vertical_top_minus_callback)
BLeftHorizontalPlus = Tkinter.Button(top, text="LeftHorizontal+", command=left_horizontal_plus_callback)
BLeftHorizontalMinus = Tkinter.Button(top, text="LeftHorizontal-", command=left_horizontal_minus_callback)
BRightVerticalBottomPlus = Tkinter.Button(top, text="RightVerticalBottom+", command=right_vertical_bottom_plus_callback)
BRightVerticalBottomMinus = Tkinter.Button(top, text="RightVerticalBottom-", command=right_vertical_bottom_minus_callback)
BRightVerticalTopPlus = Tkinter.Button(top, text="RightVerticalTop+", command=right_vertical_top_plus_callback)
BRightVerticalTopMinus = Tkinter.Button(top, text="RightVerticalTop-", command=right_vertical_top_minus_callback)
BRightHorizontalPlus = Tkinter.Button(top, text="RightHorizontal+", command=right_horizontal_plus_callback)
BRightHorizontalMinus = Tkinter.Button(top, text="RightHorizontal-", command=right_horizontal_minus_callback)

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