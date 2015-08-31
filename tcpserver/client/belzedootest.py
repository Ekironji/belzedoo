#!/usr/bin/python

import socket
import sys
import json
import getopt

def printHelp():
   print 'Usage:'
   print '  test.py -m [ pinMode | digitalWrite | analogWrite ] -p <pin_number> -v <value>'
   print '  test.py -m [ hi | disconnect ]'
   print '  test.py -m delay -v <millis>'
   print '  test.py -m analogRead -p <pin_number>'

def main(argv):
   TCP_IP = '127.0.0.1'
   TCP_PORT = 10000
   BUFFER_SIZE = 1024
   		
   command = ''
   method = ''
   sensor = ''      
   pin = ''
   value = ''
   
   data = ''
   data_string = '' 
   
#   mode = ''
#   interrupt_id = ''
#   fromLow = ''
#   fromHigh = ''
#   toLow = ''
#   toHigh = ''
   
   try:
      opts, args = getopt.getopt(argv,"ha:m:s:p:v:",["address=","method=","sensor=","pin=","value="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         printHelp()
         sys.exit()
      elif opt in ("-a", "--address"):
         TCP_IP = arg
      elif opt in ("-m", "--method"):
         method = arg
         command = 'method'
      elif opt in ("-p", "--pin"):
         pin = arg
      elif opt in ("-v", "--value"):
         value = arg
      elif opt in ("-s", "--sensor"):
         sensor = arg
         command = 'sensor'
         
   if command == 'method':
      if method == 'pinMode' or method == 'digitalWrite' or method == 'analogWrite':
         if value == 'INPUT':
            value = 0
         elif value == 'OUTPUT':
            value = 1	    
         data = {'id':0,'method':method,'pin':int(pin),'value':int(value)}
      elif method == 'digitalWrite' or method == 'analogWrite':
		 data = {'id':0,'method':method,'pin':int(pin),'value':int(value)}
      elif method == 'hi' or method == 'disconnect':
         data = {'id':0,'method':method} 
      elif method == 'delay':
         data = {'id':0,'method':method,'value':value} 
      elif method == 'analogRead':
         data = {'id':0,'method':method,'pin':pin} 
      else:
         printHelp()
         sys.exit(2)
    
   elif command == 'sensor': 
      if sensor != '':
         data = {'id':0,'sensor':sensor,'value':value}
      else:
         printHelp()
         sys.exit(2)     
                 
   data_string = json.dumps(data)
   
   if data == '':
      printHelp() 
      sys.exit(2)
   else:
      print '(belzedootest.py) String to be send: ', data_string

   # connect client
   
   MESSAGE = data_string 
   try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((TCP_IP, TCP_PORT))
      s.send(MESSAGE)
      data = s.recv(BUFFER_SIZE)
      s.close()
   except KeyboardInterrupt:		
      s.close()
      print "INTERRUZIONE"  

   print "received data:", data

if __name__ == "__main__":
   main(sys.argv[1:])
