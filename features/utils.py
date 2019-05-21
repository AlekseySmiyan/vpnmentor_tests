import http.client


def get_ip():
    con = http.client.HTTPConnection("ifconfig.me")
    con.request("GET", "/ip")
    ip = con.getresponse().read()
    return ip.decode('utf-8')

