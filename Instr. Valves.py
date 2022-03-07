# -*- coding: utf-8 -*-
import visa
import time
import numpy as np
import pyfirmata
from pyfirmata import util
import serial

# import importlib.util
# spec = importlib.util.spec_from_file_location("Valves","C:\\Users\\TuckerVana\\PycharmProjects\\GUI Project 2.0\\PyGMI-master\\PyGMI_files\\Instruments_panels")
# ValveStuff = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(spec)
# ValveStuff.Panel.change_valve_state_GUI()

# from importlib.machinery import SourceFileLoader
# ValveStuffs = SourceFileLoader('Valves',"C:\\Users\\TuckerVana\\PycharmProjects\\GUI Project 2.0\\PyGMI-master\\PyGMI_files\\Instruments_panels").load_module()
# ValveStuffs.Panel.change_valve_state_GUI()

class Connect_Instrument():
    def __init__(self,COM_port='COM10',debug=False):
        """
        part to be run at instrument initialization,
        the following commands are mandatory
        """
        #self.debug=debug
        self.io = serial.Serial(COM_port)
        it = util.Iterator(self.io)
        it.start()
        print(self.query_unit_Id())


    def query_unit_Id(self):
        """
        mandatory function
        return instrument identification.
        This command is common to almost all GPIB instruments.
        Modify if necessary.
        """
        return 'Arduino Board'

    def initialize(self):
        """
        mandatory function that will be called just after the computer
        successfully connected to the instrument.
        If you don't need it, just leave it empty but do leave the command
        "return 1"
        """
        #self.check_to_see_what_valves_are_open()
        # time.sleep(2)  # needed for the arduino stream to catch the transmission
        # self.io.write(b'1')  # need to encode the message for the pin
        # time.sleep(0)
        # valve_state_array = []
        # i = 0
        # while i < 25:
        #     state_unstripped = self.io.readlines(2)
        #     state_stripped = state_unstripped[0].decode('UTF-8')
        #     valve_state_array.append(state_stripped[0])
        #     i = 1 + i
        # print(str(valve_state_array))
        # valve_state_vector = str(valve_state_array)
        # # ValveStuff.Panel.change_valve_state_GUI(valve_state_vector)
        # ValveStuffs.Panel.change_valve_state_GUI(valve_state_vector)


        return 1

    # def check_to_see_what_valves_are_open(self):
    #     time.sleep(0.2)
    #     valve_state_array=[]
    #     self.io.write(b'1')
    #     valve_state_array.append(self.io.readlines())
    #     print(str(valve_state_array))
    #     print('valves are checked')

    def open_valve(self, command_key):
        self.io.write(command_key)
        print("Valve Opening")

    def close_valve(self, command_key):
        self.io.write(command_key)
        print("Valve Closing")

    def check_state(self):
        #if valve is on, and the button is clicked, change state
        print("Checking Valve State")

    def change_valve_state_GUI(self, valve_state_vector):

        print('Valve State\'s Verified')

    def write_command_to_update_valves(self):
        self.io.reset_output_buffer()
        self.io.write(b'1')
        print("Command Sent")

    def recieve_command(self):
        self.io.reset_input_buffer()

