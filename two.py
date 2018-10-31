# coding:utf-8

def test1():
    import socket

    print 'create socket'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'done'
    print ' connecting to remote host'
    s.connect(('www.baidu.com', 80))
    print 'done1'


def test2():
    """寻找端口号"""
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = socket.getservbyname('http', 'tcp')
    s.connect('www.baidu.com', port)
    print 'connected from', s.getsockname()
    print 'connected to', s.getpeername()


def test3():
    """异常"""
    import socket, sys, time
    print sys.argv
    host = sys.argv[1]
    textport = sys.argv[2]
    filename = sys.argv[3]

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print 'strang error creating socket: %s' % e
        sys.exit(1)
    try:
        port = int(textport)
    except ValueError:
        try:
            port = socket.getservbyname(textport, 'tcp')
        except socket.error as e:
            print 'couldnt find your port: %e' % e
            sys.exit(1)
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print 'address error connecting to server:%s' % e
        sys.exit(1)
    except socket.error, e:
        print 'connection error %s' % e
        sys.exit(1)
    print 'sleeping'
    time.sleep(10)
    print 'continuing'
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print 'error sending data:%s' % s
        sys.exit(1)

    try:
        s.shutdown(1)
    except socket.error, e:
        print 'error sending data(detected by shutdown): %s' % e
        sys.exit(1)

    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print 'error receiving data:%s' % e
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)


def test4():
    """udp"""
    import socket, sys
    host = sys.argv[1]
    textport = sys.argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        port = int(textport)
    except ValueError:
        port = socket.getservbyname(textport, 'udp')

    s.connect((host, port))
    data = sys.stdin.readline().strip()
    s.sendall(data)
    print 'looking for replies; press,ctrl +c to stop'
    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
