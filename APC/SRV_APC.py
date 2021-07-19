### IMPORTANT ###
# Le protocole mDNS est une version du même protocole mais en Multicast sur
# l’adresse 224.0.0.251 et le port 5353.

txt_record = "'192.168.0.10'._apc.itxpt_http._tcp.local 3600 IN SRV 0 0 9000 '192.168.0.1'"


from zeroconf import ServiceBrowser, Zeroconf


class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "apc", "9990._apc._itxpt_http._tcp.local", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()


