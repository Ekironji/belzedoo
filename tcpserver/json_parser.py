import socket
import sys
import json

pinMode = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
value   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

INPUT = 0
OUTPUT = 1
LOW = 0
HIGH = 1

def processCommand():
	if decoded['method'] == "pinMode":
		if decoded['pin'] >= 0 and decoded['pin'] < 55:
			if decoded['value'] == 0:
				pinMode[decoded['value']] = INPUT;
			else:
				pinMode[decoded['value']] = OUTPUT;
			writeToSerial(data)
		else:
			print >>sys.stderr, "Error: Invalid pin number"

	elif decoded['method'] == "digitalWrite":
		if decoded['pin'] >= 0 and decoded['pin'] < 55:
			if decoded['value'] == 0:
				pinMode[decoded['value']] = LOW;
			else:
				pinMode[decoded['value']] = HIGH;
			writeToSerial(data)
		else:
			print >>sys.stderr, "Error: Invalid pin number"

	elif decoded['method'] == "digitalRead":
		if decoded['pin'] >= 0 and decoded['pin'] < 55:			
			writeToSerial(data)
		else:
			print >>sys.stderr, "Error: Invalid pin number"

	elif decoded['method'] == "analogWrite":
		if decoded['pin'] >= 0 and decoded['pin'] < 14:
			#controllo
			writeToSerial(data)
		else:
			print >>sys.stderr, "Error: Invalid pin number"

	elif decoded['method'] == "analogRead":
		if decoded['pin'] >= 0 and decoded['pin'] < 55:			
			writeToSerial(data)
		else:
			print >>sys.stderr, "Error: Invalid pin number"

	elif decoded['method'] == "map":
		print "map"
	else:
		print >>sys.stderr, "Error> method unkown"



def writeToSerial(dataToSend):
	print "SERIAL> " + dataToSend

data = "{\"method\":\"pinMode\",\"pin\":13,\"value\":1}"

try:
	decoded = json.loads(data)
	#  print data 
	#  print json.dumps(decoded, sort_keys=True, indent=4)
	## print "JSON parsing example: ", decoded['one']
	## print "Complex JSON parsing example: ", decoded['two']['list'][1]['item']
	processCommand() 
except (ValueError, KeyError, TypeError):
	print >>sys.stderr, "JSON format error"
	#connection.sendall(decoded)

