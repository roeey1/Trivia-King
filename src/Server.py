import socket
import struct
import time


class Server:

    def __init__(self):
        self.MAGIC_COOKIE = 0xabcddcba
        self.SERVER_PORT = 13117
        self.MESSAGE_TYPE = 0x2
        self.TEAM_NAME = "Mystic"
        self.SERVER_NAME = "EchoNexus".ljust(32, ' ')
        self.UDP_BROADCAST_ADDRESS = "<broadcast>"
        self.player_online_count = 0
        self.client_list = {}
        self.serverUDP()


    def serverUDP(self):
        ## create a socket object using udp

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket created")

        ## get local ip address
        host = socket.gethostbyname(socket.gethostname())

        ## bind to the port
        socket_server.bind((host, self.SERVER_PORT))

        print("Server UDP socket binded to %s" % (self.SERVER_PORT))

        # Build the packet
        packet = struct.pack('!IBI32sH', self.MAGIC_COOKIE, self.MESSAGE_TYPE,
                             len(self.SERVER_NAME.encode('utf-8')),
                             self.SERVER_NAME.encode('utf-8'), self.SERVER_PORT)

        ## broadcast the server to clients
        socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print("Server started, listening on IP address " + host)


        is_there_players = False
        while not is_there_players:

            # Broadcasting loop
            for i in range(10):
                socket_server.sendto(packet, (self.UDP_BROADCAST_ADDRESS, self.SERVER_PORT))
                time.sleep(1)


            if self.player_online_count > 0:
                pass


    # create tcp server
    def serverTCP(self):
        TCP_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCP_server.bind((socket.gethostbyname(socket.gethostname()), self.SERVER_PORT))
        TCP_server.listen(1)
        pass

