# API to communicate with the PiLC

__version__ = '0.0.0'

import socket
import logging
import os
import sys

import numpy

import PyTango

# FPGA
FREQUENCY_DIVIDER_REGISTER = 0x01
DELAY_REGISTER = 0x03
HIGH_TIME_REGISTER = 0x05
INTERNAL_GENERATOR_ENABLE_REGISTER = 0x07
INTERNAL_FREQUENCY_REGISTER = 0x09
EXTERNAL_TRIGGER_ACTIVE_REGISTER = 0x02

class PiLCAPI():
    
    def __init__ (self, pilc_connect):
        self.pilc = PyTango.DeviceProxy(pilc_connect)

    def InitPiLC (self):
        self.pilc.InitPiLC()

    def PiLCDeinit (self):
        self.pilc.PiLCDeinit()

    def WriteDisplay(self, command, value):
        cmd_args = [command, value]
        self.pilc.WriteDisplay(cmd_args)
        
    def ReadDisplay(self, command):
        return self.pilc.ReadDisplay(command)
    
    def WriteFPGA(self, address, data):
        cmd_args = [address, data]
        self.pilc.WriteFPGA(cmd_args)

    def ReadFPGA(self, address):
        return self.pilc.ReadFPGA(address)

    def FPGAReadBurst(self, address, nb_registers):
        cmd_args = [address, nb_registers]
        return self.pilc.FPGAReadBurst(cmd_args)

    def FPGAReadSDRAM(self, nb_registers):
        x = self.pilc.FPGAReadSDRAM(nb_registers)
        nx = numpy.array(x)
        return nx

    def WriteIOBoard(self, command, red, green, blue):
        cmd_args = [command, red, green, blue]
        self.pilc.WriteIOBoard(cmd_args)

    def ReadIOBoard(self, command):
        return self.pilc.ReadIOBoard(command)

    def WriteIOCard(self, module, command, value):
        cmd_args = [module, command, value]
        self.pilc.WriteIOCard(cmd_args)

    def ReadIOCard(self, module, command):
        cmd_args = [module, command]
        return self.pilc.ReadIOCard(cmd_args)
    
    def GetIOCardIDArray(self):
        return self.pilc.GetIOCardIDArray()

    def WriteMainBoard(self, command, value):
        cmd_args = [command, value]
        self.pilc.WriteMainBoard(cmd_args)

    def ReadMainBoard(self, command):
        return self.pilc.ReadMainBoard(command)

    def EPCSProgram(self, filename):
        self.pilc.EPSProgram(filename)
        
    def EventUpdate(self):
        return self.pilc.EventUpdate()
        
    def EventUpdateLib(self):
        self.pilc.EventUpdateLib()
        
    def LEDsUpdate(self):
        self.pilc.LEDsUpdate()
        
    def SPIEraseBluk(self):
        return self.pilc.SPIEraseBluk()

    def SPIErasePage(self, address):
        self.pilc.SPIErasePage(address)

    def SPIEraseSector(self, length):
        self.pilc.SPIEraseSector(length)

    def SPIReadByte(self, address, bytes_to_read):
        cmd_args = [address, bytes_to_read]
        self.pilc.SPIReadByte(cmd_args)

    def SPIReadID(self):
        return self.pilc.SPIReadID()
    
    def SPIReadStatus(self):
        # Read Read Status
        return self.pilc.SPIReadStatus()

    def SPISendBytes(self,operation_code, dd_bytes, debug_flag):
        cmd_args = [operation_code, dd_bytes, debug_flag]
        self.pilc.SPISendBytest(cmd_args)

    def SPIWrite(data):
        # Send data and wait until it finish
        return self.pilc.SPIWrite(data)
    
    def SPIWritePage(self, data, address):
        cmd_args = [data, address]
        self.pilc.SPIWritePage(cmd_args)
        
    def SPIWriteSector(self, data, length):
        cmd_args = [data, length]
        self.pilc.SPIWriteSector(cmd_args)
    
    def SPIWriteStatus(self):
        # Read Write Status
        return self.pilc.SPIWriteStatus()

    def USVUpdate(self, show_flag, shutdown_flag, shutdown_time):
        cmd_args = [show_flag, shutdown_flag, shutdown_time]
        self.pilc.USVUpdate(cmd_args)


    

        
        
