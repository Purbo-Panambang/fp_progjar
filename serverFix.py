import select
import socket
import sys
import os
import pickle
import random
import threading
import re

host = 'localhost'
#print "port:"
#port = input()
#alamat = (host,port)

#server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#server.bind(alamat)
#server.listen(100)
id_pemain = int()
pemain = list()
#input_socket = [server]


deck = list()
#deck2 = list()
pegangan = list()
pegangan2 = list()
kartu1 = list()
kartu2 = list()
global glob
global glob2


# Mulai Kartu
class Card:
    def __init__(self, faceNum, suitNum):
        self.faceNum = faceNum
        self.suitNum = suitNum

    def getCardName(self):
          nameSuit = ['As','2','3','4','5','6','7','8','9','10','Jek','Queen','King']
          nameFace = ['Wajik','Waru','Semanggi','Hati']
          return "%s %s %s" % (self.suitNum, nameSuit[self.suitNum], nameFace[self.faceNum])

    def __str__(self):
        carte_print1 = str(self.faceNum)
        carte_print2 = str(self.suitNum)
        return carte_print1 +('-')+ carte_print2

class Player:
    def __init__(self,ID,Card):
        #self.PlayerID = ID
        #print Card
        self.PlayerID = ID
        self.deck = Card # this will hold a list of Card objects
    def flag(self):
        return self.PlayerID,self.deck


def deck():
	deck = []
	for suitNum in range(13):
		for faceNum in range(4):
			deck.append(Card(faceNum, suitNum))
	return deck

deck = deck()
#deck2 = deck()


#print Player.flag(player1)
#print Player.flag(player2)

def bandingKartu(x,y):
	if x > y:
		return x
	elif x == y:
		return "podo"
	else:
		return y
	# akhir kartu

	# Kelas Server



class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5215
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host,self.port))
        self.server.listen(100)
        
    def run(self):
        self.open_socket()
        input = [self.server, sys.stdin]
        running = 1
        while running:
            inputready,outputready,exceptready = select.select(input,[],[])

            for s in inputready:

                if s == self.server:
                    # handle the server socket
                    c = Client(self.server.accept())
                    c.start()
                    self.threads.append(c)

                elif s == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = 0
                    test = sock.recv(1024)
                    [(k,v)]=pemain.items()
                    print k,":",test
                    p = pickle.dumps(Player.flag(player1))
                    #sock.send(p)
			#id_pemain += 1
                #tanda_client = str(client_address[1])
                #sock.send(tanda_client)
                #id_client = sock.recv(1024)
                
                #temp = pemain[0]
                #print pemain
                
                #print type(k)
                #temp == k
                """
                if k == 1:
                    #print "tes"
                    
                if k == 2:
                    #print "tes"
                    p = pickle.dumps(Player.flag(player2))
                    sock.send(p)
                """
                #testhilangkartu(test)
                #print Player.flag(player1)
                #header = 7389        
        

        # close all threads

        self.server.close()
        for c in self.threads:
            c.join()
def pemenang(count2, count):
	if count2 > count:
		print "Pemain 2 Menang"
		print count2
		print count
		exit()
	else:
		print "Pemain 1 Menang"
		print count2
		print count
		exit()
def hilangkartu(x):
	pegangan.pop(x)
	pegangan2.pop(x)

def simpanpemain(x):
	pemain.append(x)	


for card in range(0,5):
	pegangan.append(deck[card].getCardName())
	random.shuffle(deck)
	pegangan2.append(deck[card].getCardName())

class Client(threading.Thread):
    def __init__(self,(client,address)):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        player1 = Player(self.address, pegangan)
        player2 = Player(self.address, pegangan2)
        count = 0
        count2 = 0
        tempo = 0
        simpanpemain(self.address[1])
        while running:
			print len(kartu1)
			print len(kartu2)
			
			#print Player.flag(player1)
			data = self.client.recv(self.size)
			tmp = data.split(" ")
			coba = int(tmp[0])
			print coba
			if len(kartu1) == len(kartu2) and (len(kartu1) > 0 and len(kartu2)>0) and tempo != 10:
				if kartu1[coba] > kartu2[coba]:
					#if len(kartu1) != 5 and len(kartu2) != 5:
						if len(pegangan) > 0:
							pegangan.pop(coba)
						if len(pegangan2) > 0:
							pegangan2.pop(coba)
						notif1 = "client 1 menang"
						pegangan.append(notif1)
						pegangan2.append(notif1)
						count += 1
						tempo += 1
					#else:
					#	pemenang(count2,count)
				if kartu2[coba] > kartu1[coba]:		
					#if len(kartu1) != 5 and len(kartu2) != 5:
						if len(pegangan) > 0:
							pegangan.pop(coba)
						if len(pegangan2) > 0:
							pegangan2.pop(coba)
						notif = "client 2 menang"
						pegangan.append(notif)
						pegangan2.append(notif)
						count2 += 1
						tempo += 1
					#else:
					#	pemenang(count2,count)
			"""
			if len(kartu1) == 5 and len(kartu2) == 5:
				if count2 > count:
					print "Pemain 2 Menang"
					#print count2
				else:
					print "Pemain 1 Menang"
			"""
			p = pickle.dumps(Player.flag(player1))
			p2 = pickle.dumps(Player.flag(player2))
			print tempo		
			#temp = data.split(" ")
			#print temp
			if data != '9':
				temp = data.split(" ")
				print data
				if int(temp[1]) == pemain[0]:
					print 'menerima dari: ', self.address[1], temp[0]
					kartu1.append(pegangan[int(temp[0])])
					#glob = int(temp[0])
					self.client.send(p)
				elif int(temp[1]) == pemain[1]:
					print 'menerima dari: ', self.address[1], temp[0]
					kartu2.append(pegangan2[int(temp[0])])
					glob2 = int(temp[0])
					print glob2
					self.client.send(p2)
				
			elif data == '9':
				if pemain[0] == self.address[1]:
					#print 'menerima dari: ', self.address[1], data
					self.client.send(p)
				else:
					self.client.send(p2)
			else:
				self.client.close()
				running = 0
				
		
			
if __name__ == "__main__":
    s = Server()
    s.run() 
