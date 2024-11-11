import socket
import time
from colorama import Fore, Style, init
i = 1
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Wait max 1 second
    result = sock.connect_ex((host , port))
    sock.close()
    return result == 0
# Try connecting to a port
host = input("Enter the URL you want to scan")
while i <= 1024:
    port = i
    is_open = check_port(host , port)
    print(f"{Fore.YELLOW}Port {Fore.BLUE}{port} {Fore.MAGENTA}is {Fore.GREEN + 'open' if is_open else Fore.RED + 'closed'}{Style.RESET_ALL}")
    i = i + 1