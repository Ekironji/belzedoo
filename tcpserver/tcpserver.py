import socket
import sys
import json


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(('', 10000))

# Listen for incoming connections
sock.listen(1)

def processCommand():
	print "caneeeee"

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(128)
            print >>sys.stderr, 'received "%s"' % data
            if data:
				try:
   					decoded = json.loads(data)
					print data 
    				# pretty printing of json-formatted string
   					print json.dumps(decoded, sort_keys=True, indent=4)
     				## print "JSON parsing example: ", decoded['one']
    				## print "Complex JSON parsing example: ", decoded['two']['list'][1]['item']
					processCommand() 
				except (ValueError, KeyError, TypeError):
					print >>sys.stderr, "JSON format error"
                
				print >>sys.stderr, 'sending data back to the client'
				#connection.sendall(decoded)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
