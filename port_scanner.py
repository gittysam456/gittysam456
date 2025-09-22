import socket
def port_scanner(target, start_port, end_port): #a function that sccans the port
    print(f'Scanning {target} from {start_port}, to {end_port}.....') # eg: print the input ports for the scannning
    for port in range(start_port,end_port+1):  #a loop  that will scan the ports in the range
        scanner=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # inet for ipv4 and sock_steam for tcp connction
        scanner.settimeout(1.0)  # time out for the response
        res=scanner.connect_ex((target,port))
        if res==0:
            print(f'port {port} is open')
        else:
            print(f'port {port} is closed')
        scanner.close()


print(port_scanner('www.psit.ac.in',80,85))

    