#!/usr/bin/python
import threading
import SocketServer
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format=('%(asctime)s: %(message)s:'))

class ThreadedUDPRequestHandler(
	SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        port = self.client_address[1]
        socket = self.request[1]
        client_address = (self.client_address[0])
        cur_thread = threading.current_thread()
        print ("thread %s" %cur_thread.name)
        print ("received call from client address :%s" %client_address)
        print ("received data from port [%s]: %s" %(port,data))
        logging.info(str(data))

class ThreadedUDPServer(
SocketServer.ThreadingMixIn, 
SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 8888

    server = ThreadedUDPServer((HOST, PORT), 
		ThreadedUDPRequestHandler)
    ip, port = server.server_address
    server.serve_forever()
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    server.shutdown()