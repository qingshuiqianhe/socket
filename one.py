# coding:utf-8
import socket, sys
port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket[socket.AF_INET, socket.SOCK_STREAM]
try:
    s.connect((host, port))
except socket.gaierror, e:
    print ' error connecting to server:%s' %e
    sys.exit(1)

s.sendall(filename + "\r\n")
while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)


def test2():
    host = ''
    port = 51423
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    print "server is running on port %d;paress ti terminate"% port
    while 1:
        clientscok, clientaddr = s.accept()
        clientfile = clientscok.makefile('rw', 0)
        clientfile.write('welcome ' + str(clientaddr) + '\n')
        clientfile.write('please enter a string')
        line = clientfile.readline().strip()
        clientfile.write('you entered %d characters.\n' % len(line))
        clientfile.close()
        clientscok.close()


def test3():
    import urllib, sys
    host = sys.argv[1]
    file = sys.argv[2]

    f = urllib.urlopen('gopher://%s%s' % (host, port))
    for line in f.readlines:
        sys.stdout.write(line)


def test4():
    import urllib, sys
    f = urllib.urlopen(sys.argv[1])
    while 1:
        buf = f.read(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)


