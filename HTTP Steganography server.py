import http.server

class MyServer(http.server.BaseHTTPRequestHandler):

    bits_list = []
    count = 0
    msg = ""

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        print(self.headers.get_all("Cookie"))
        if ';' in self.headers.get_all("Cookie")[0]:
            print("You have communicated 1")
            if self.count < 6:
                count = self.count + 1
                self.bits_list.append(1)
            
        else:
            print("You have communicated 0")
            if self.count < 6:
                count = self.count + 1
                self.bits_list.append(0)
        print(self.bits_list)
        if len(self.bits_list) >= 7:
            for i in self.bits_list:
                self.msg = self.msg + str(i)
            print(chr(int(bytes(self.msg,encoding="utf-8").decode(encoding="utf-8"),base=2)))
            self.bits_list.clear()
server = http.server.HTTPServer(("localhost",8080),MyServer)
server.serve_forever()