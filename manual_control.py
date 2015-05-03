import Tkinter
from Tkconstants import *
from Tkinter import Frame, Button, Entry, Label, StringVar
import serial
import threading


__author__ = 'snigavig'


class ManualControl(Frame):
    SERIAL_TIMEOUT = 100
    PORT = '/dev/ttyACM0'
    SPEED = 9600
    DELIMITER = ","
    current_state = [300, 320, 230, 430, 230, 430, 320, 430, 320] # dummy data
    goal_state = []
    entry_state_map = []
    connection = serial.Serial(PORT, SPEED, timeout=0, stopbits=serial.STOPBITS_TWO)

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.right_arm_horizontal_bottom_entry = Entry(self, bd=5)
        self.right_arm_horizontal_top_entry = Entry(self, bd=5)
        self.right_arm_vertical_entry = Entry(self, bd=5)
        self.left_arm_horizontal_bottom_entry = Entry(self, bd=5)
        self.left_arm_horizontal_top_entry = Entry(self, bd=5)
        self.left_arm_vertical_entry = Entry(self, bd=5)
        self.leg_horizontal_bottom_entry = Entry(self, bd=5)
        self.leg_horizontal_top_entry = Entry(self, bd=5)
        self.leg_vertical_entry = Entry(self, bd=5)
        self.send_button = Button(self, text="Send command", command=self.send_command)

        self.leg_vertical_label_variable = StringVar()
        self.leg_horizontal_top_label_variable = StringVar()
        self.leg_horizontal_bottom_label_variable = StringVar()
        self.left_arm_vertical_label_variable = StringVar()
        self.left_arm_horizontal_bottom_label_variable = StringVar()
        self.right_arm_vertical_label_variable = StringVar()
        self.right_arm_horizontal_top_label_variable = StringVar()
        self.right_arm_horizontal_bottom_label_variable = StringVar()
        self.left_arm_horizontal_top_label_variable = StringVar()

        self.leg_vertical_label = Label(self, textvariable=self.leg_vertical_label_variable, text=self.current_state[8])
        self.leg_horizontal_top_label = Label(self, textvariable=self.leg_horizontal_top_label_variable,
                                              text=self.current_state[7])
        self.leg_horizontal_bottom_label = Label(self, textvariable=self.leg_horizontal_bottom_label_variable,
                                                 text=self.current_state[6])
        self.left_arm_vertical_label = Label(self, textvariable=self.left_arm_vertical_label_variable,
                                             text=self.current_state[5])
        self.left_arm_horizontal_bottom_label = Label(self, textvariable=self.left_arm_horizontal_bottom_label_variable,
                                                      text=self.current_state[3])
        self.right_arm_vertical_label = Label(self, textvariable=self.right_arm_vertical_label_variable,
                                              text=self.current_state[2])
        self.right_arm_horizontal_top_label = Label(self, textvariable=self.right_arm_horizontal_top_label_variable,
                                                    text=self.current_state[1])
        self.right_arm_horizontal_bottom_label = Label(self,
                                                       textvariable=self.right_arm_horizontal_bottom_label_variable,
                                                       text=self.current_state[0])
        self.left_arm_horizontal_top_label = Label(self, textvariable=self.left_arm_horizontal_top_label_variable,
                                                   text=self.current_state[4])
        self.parent = parent
        self.init_ui()
        self.read_serial()

    def on_up_key_pressed_callback(self, widget):
        self.goal_state[self.entry_state_map.index(widget)] += 10
        widget.delete(0, END)
        widget.insert(0, self.goal_state[self.entry_state_map.index(widget)])

    def on_down_key_pressed_callback(self, widget):
        self.goal_state[self.entry_state_map.index(widget)] -= 10
        widget.delete(0, END)
        widget.insert(0, self.goal_state[self.entry_state_map.index(widget)])

    def read_ui_input(self):
        self.goal_state = [
            self.right_arm_horizontal_bottom_entry.get(),
            self.right_arm_horizontal_top_entry.get(),
            self.right_arm_vertical_entry.get(),
            self.left_arm_horizontal_bottom_entry.get(),
            self.left_arm_horizontal_top_entry.get(),
            self.left_arm_vertical_entry.get(),
            self.leg_horizontal_bottom_entry.get(),
            self.leg_horizontal_top_entry.get(),
            self.leg_vertical_entry.get()
        ]

    def send_command(self):
        self.read_ui_input()
        self.connection.write(str(self.DELIMITER.join(self.goal_state)))

    def read_serial_mock(self):
        print self.current_state

    def read_serial(self):
        if self.connection.inWaiting() > self.SERIAL_TIMEOUT:
            self.current_state = self.connection.readline()
            print self.current_state
            self.current_state = self.current_state.rstrip().split(',')
            self.update_ui_labels()
            print self.current_state


        self.parent.after(500, self.read_serial)


    def update_ui_labels(self):
        self.right_arm_horizontal_bottom_label_variable.set(self.current_state[0])
        self.right_arm_horizontal_top_label_variable.set(self.current_state[1])
        self.right_arm_vertical_label_variable.set(self.current_state[2])
        self.left_arm_horizontal_bottom_label_variable.set(self.current_state[3])
        self.left_arm_horizontal_top_label_variable.set(self.current_state[4])
        self.left_arm_vertical_label_variable.set(self.current_state[5])
        self.leg_horizontal_bottom_label_variable.set(self.current_state[6])
        self.leg_horizontal_top_label_variable.set(self.current_state[7])
        self.leg_vertical_label_variable.set(self.current_state[8])

    def init_ui(self):

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)

        self.right_arm_horizontal_bottom_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.right_arm_horizontal_bottom_entry))
        self.right_arm_horizontal_bottom_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.right_arm_horizontal_bottom_entry))
        self.right_arm_horizontal_top_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.right_arm_horizontal_top_entry))
        self.right_arm_horizontal_top_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.right_arm_horizontal_top_entry))
        self.right_arm_vertical_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.right_arm_vertical_entry))
        self.right_arm_vertical_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.right_arm_vertical_entry))
        self.left_arm_horizontal_bottom_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.left_arm_horizontal_bottom_entry))
        self.left_arm_horizontal_bottom_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.left_arm_horizontal_bottom_entry))
        self.left_arm_horizontal_top_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.left_arm_horizontal_top_entry))
        self.left_arm_horizontal_top_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.left_arm_horizontal_top_entry))
        self.left_arm_vertical_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.left_arm_vertical_entry))
        self.left_arm_vertical_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.left_arm_vertical_entry))
        self.leg_horizontal_bottom_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.leg_horizontal_bottom_entry))
        self.leg_horizontal_bottom_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.leg_horizontal_bottom_entry))
        self.leg_horizontal_top_entry.bind('<Up>', lambda event: self.on_up_key_pressed_callback(
            self.leg_horizontal_top_entry))
        self.leg_horizontal_top_entry.bind('<Down>', lambda event: self.on_down_key_pressed_callback(
            self.leg_horizontal_top_entry))
        self.leg_vertical_entry.bind('<Up>',
                                     lambda event: self.on_up_key_pressed_callback(self.leg_vertical_entry))
        self.leg_vertical_entry.bind('<Down>',
                                     lambda event: self.on_down_key_pressed_callback(self.leg_vertical_entry))

        self.entry_state_map = [
            self.right_arm_horizontal_bottom_entry,
            self.right_arm_horizontal_top_entry,
            self.right_arm_vertical_entry,
            self.left_arm_horizontal_bottom_entry,
            self.left_arm_horizontal_top_entry,
            self.left_arm_vertical_entry,
            self.leg_horizontal_bottom_entry,
            self.leg_horizontal_top_entry,
            self.leg_vertical_entry
        ]

        self.right_arm_horizontal_bottom_label.grid(row=0, column=0)
        self.right_arm_horizontal_bottom_entry.grid(row=0, column=1)
        self.right_arm_horizontal_top_label.grid(row=1, column=0)
        self.right_arm_horizontal_top_entry.grid(row=1, column=1)
        self.right_arm_vertical_label.grid(row=2, column=0)
        self.right_arm_vertical_entry.grid(row=2, column=1)
        self.left_arm_horizontal_bottom_label.grid(row=3, column=0)
        self.left_arm_horizontal_bottom_entry.grid(row=3, column=1)
        self.left_arm_horizontal_top_label.grid(row=4, column=0)
        self.left_arm_horizontal_top_entry.grid(row=4, column=1)
        self.left_arm_vertical_label.grid(row=5, column=0)
        self.left_arm_vertical_entry.grid(row=5, column=1)
        self.leg_horizontal_bottom_label.grid(row=6, column=0)
        self.leg_horizontal_bottom_entry.grid(row=6, column=1)
        self.leg_horizontal_top_label.grid(row=7, column=0)
        self.leg_horizontal_top_entry.grid(row=7, column=1)
        self.leg_vertical_label.grid(row=8, column=0)
        self.leg_vertical_entry.grid(row=8, column=1)
        self.send_button.grid(row=9, columnspan=2, sticky=W + E)

        self.pack()

        self.goal_state = self.current_state
        self.right_arm_horizontal_bottom_entry.insert(0, self.goal_state[0])
        self.right_arm_horizontal_top_entry.insert(0, self.goal_state[1])
        self.right_arm_vertical_entry.insert(0, self.goal_state[2])
        self.left_arm_horizontal_bottom_entry.insert(0, self.goal_state[3])
        self.left_arm_horizontal_top_entry.insert(0, self.goal_state[4])
        self.left_arm_vertical_entry.insert(0, self.goal_state[5])
        self.leg_horizontal_bottom_entry.insert(0, self.goal_state[6])
        self.leg_horizontal_top_entry.insert(0, self.goal_state[7])
        self.leg_vertical_entry.insert(0, self.goal_state[8])


def main():
    root = Tkinter.Tk()
    app = ManualControl(root)
    root.mainloop()


if __name__ == '__main__':
    main()
