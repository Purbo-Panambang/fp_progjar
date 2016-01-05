import socket
import sys
import pickle

host = 'localhost'
print "port:"
port = input()
alamat = (host,port)
BUFFSIZE = 1024
hasil = list()
message = list()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(alamat)

def showCard():
    if hasil:
        temp = 0
        for item in range(0,len(hasil[1])):
            print "%i."%temp,hasil[1][item]
            temp += 1
        print "99. Exit"
        
    else:
        print "Selamat Datang Game Kartu"

def pilihan():
    if hasil:
        showCard()
    else:
        print "9. Play"
        print "99. Exit"

try:
    while True:
        pilihan()
        respons = input()
        
        if respons == 9:
            client.send(str(respons))
        elif respons > -1 and respons < 6 :
			#temp = str(respons)+" "+str(hasil[0][1])
			#print temp
			client.send(str(respons)+" "+str(hasil[0][1]))
        elif respons == 99:
            break
        else:
            showCard()
        #id_socket = client.recv(BUFFSIZE)
        #client.send(id_socket)
        
        m_header = client.recv(BUFFSIZE)
        #print str(m_header)
        hasil = pickle.loads(m_header)
        #print hasil[0][1]
        print hasil

except KeyboardInterrupt:
    print "Good bye"
    client.close()
    sys.exit(0)
