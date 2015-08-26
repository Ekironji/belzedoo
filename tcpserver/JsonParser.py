import socket
import sys
import json
import serial
import time

INPUT = 0
OUTPUT = 1
LOW = 0
HIGH = 1

class Parser:

   ser = None
   ans = ''

   def writeToSerial(self, dataToSend):
      print "SERIAL> " + dataToSend
      return dataToSend
      try:
         if input == 'exit':
            ser.close()
            exit()
         else:
            ser.write(dataToSend + '\r\n')
            out = ''
            time.sleep(0.05)
            while ser.inWaiting() > 0:
               out += ser.read(1)
      except:
		  exit()		           
      print "SERIAL> " + out
      
   def __init__(self):
      self.pinMode = [\
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0]
      self.value = [
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,
      0,0,0,0]
      
      # configure the serial connections (the parameters differs on the device you are connecting to)
      try:
         self.ser = serial.Serial(
            port='/dev/ttymxc3',
            baudrate=115200
         )
      except:
		  print "Serial connection fail!"
		  exit()

   def processCommand(self, data):    
      try:
         decoded = json.loads(data)
      except (ValueError, KeyError, TypeError):
         print >> sys.stderr, "(Json parser) JSON format error"
         return -1
            
      if decoded['method'] == "pinMode":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:
            if int(decoded['value']) == 0:
               self.pinMode[int(decoded['value'])] = INPUT;
            else:
               self.pinMode[int(decoded['value'])] = OUTPUT;
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "digitalWrite":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:
            if int(decoded['value']) == 0:
               self.pinMode[int(decoded['value'])] = LOW;
            else:
               self.pinMode[int(decoded['value'])] = HIGH;
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "digitalRead":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:         
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "analogWrite":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 14:
            #controllo
            ans = self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "analogRead":
         if int(decoded['pin']) >= 0 and int(decoded['pin']) < 55:         
            self.writeToSerial(data)
         else:
            print >>sys.stderr, "Error: Invalid pin number"

      elif decoded['method'] == "map":
         print "map"

      else:
         print >>sys.stderr, "Error> method unkown"
      
      ### SCRIVI IN SERIALE E ASPETTA IL RISULTATO
      
      print "BAUUUUUUU" + ans   
      return ans   
