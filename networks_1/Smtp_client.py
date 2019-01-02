import ssl
import base64
from socket import *
import sys
class Smtp_client:
    
    def __init__(self, hostname, port, adress, password):
        self.adress = adress
        self.password = password
        simple_socket = socket()
        try:
            simple_socket.connect((hostname, port))
            context = ssl.create_default_context()
            self.socket = context.wrap_socket(simple_socket, server_hostname=hostname)
            r = self.socket.recv(10000).decode()
            print(r)
            r = r.split(" ",1)[0]
            if(r != "220"):
                raise error
        except gaierror as e:
            print(type(e))
            print("chromey dino!")
            sys.exit()
            
          
        
    
    def sendssl(self, data):
                command  = str(data) + "\r\n"
                print("CLIENT: " + command)
                enc = bytes(command, "utf-8")
                self.socket.sendall(enc)
                answer = self.socket.recv(1000000)
                return answer
            
    def sendmail(self, rcpt, subject, message):
        
        user = self.adress
        header_from = "From: "  + self.adress + " \r\n"
        header_to = "To: " + rcpt + " \r\n"
        header_subject = "Subject: " + subject + " \r\n"
        data = header_from + header_to + header_subject + message + "\r\n.\r\n"
        euser = base64.b64encode((bytes(user,"utf-8"))).decode("utf-8")
        epass = base64.b64encode((bytes(self.password,"utf-8"))).decode("utf-8")
        
        commands = {}
        commands["helo"] = "HELO snow"
        commands["login request"] = "AUTH LOGIN"
        commands["encoded username"] = euser
        commands["encoded passord"] = epass
        commands["client adress"] = "MAIL From:<" + self.adress + ">"
        commands["rcpt"] = "RCPT To:<" + rcpt + ">"
        commands["data request"] = "DATA"
        commands["data"] = data
        commands["quit"] = "QUIT"
        
        return_codes = {}
        return_codes["helo"] = "250"
        return_codes["login request"] = "334"
        return_codes["encoded username"] = "334"
        return_codes["encoded passord"] = "235"
        return_codes["client adress"] = "250"
        return_codes["rcpt"] = "250"
        return_codes["data request"] = "354"
        return_codes["data"] = "250"
        return_codes["quit"] = "221"
        
        for command in commands:
            try:
                r = self.sendssl(commands[command])
                print("SERVER: " + str(r))
                r = r.decode().split(" ",1)[0]
                if(r != return_codes[command]):
                    raise error
            except error:
                print("dat' ain't right you diny chrome dino")
                self.socket.close()
                sys.exit()
            
                    
            
            



