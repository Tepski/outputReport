import socket, time

class PLCListener:
    addr = ()
    BUFFER = 1024
    dm_list = []
    mode = 0

    def __init__(self, host, port):
        self.addr = (host, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.settimeout(2)

    def do(self, action, retries=3, delay=1):
        attempt = 0
        time_now = time.localtime()
        while attempt < retries:
            try:
                self.client.sendto(action.encode(), self.addr)

                response = self.client.recv(self.BUFFER)

                return response.decode()
            
            except socket.timeout:
                attempt += 1
                print(f"Timeout occured at: {time_now.tm_hour}:{time_now.tm_min}")
                print(attempt)

            except Exception as e:
                print(e)


    def read_val(self, action):
        val = self.do(f"RD {action}\r")

        return val

    def write(self, action, value):
        val = f"WR {action} {value}\r"
        res = self.do(val)

        return res

    def set(self, value):
        val = f"ST {value}\r"
        res = self.do(val)

        return res
    
    def reset(self, value):
        val = f"RS {value}\r"
        res = self.do(val)

        return res

    def mode(self, action):
        mode = f"M{action}\r"
        res = self.do(mode)

        return res
    
    def string2dec(self, s):
        if len(s) != 2:
            raise ValueError("Input string must be exactly 2 characters long.")
        
        ascii1 = ord(s[0])  
        ascii2 = ord(s[1])  
        
        combined_value = (ascii1 << 8) + ascii2
        
        return combined_value
    
    def handleString2Dec(self, string, target):
        dm_init = 35003

        if len(string) % 2 != 0:
            string += " "

        for i in range(0, len(string), 2):
            s = string[i] + string[i + 1]
            code = self.string2dec(s)
            self.write(f"DM{dm_init}", code)
            self.dm_list.append(dm_init)
            dm_init += 1

        self.set(f"R{target}5000")

    def clear_string(self, target, all=True):
        self.reset(f"R{target}5000")
        if all:
            for i in range(35000, 35050):
                self.write(f"DM{i}", 0)
            
        else: 
            for i in self.dm_list:
                self.write(f"DM{i}", 0)
        self.dm_list = []
    

if __name__ == "__main__":
    listener = PLCListener("192.168.1.254", 8500)

    listener.write("DM57002", 0)