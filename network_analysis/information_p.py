from scapy.all import *
from print_p import PRINT_LAST as PL
from parameters_p import ADDITIONAL_GET as AG
import socket,requests,json,mechanize,threading
import pandas as pd


def CONNECT_SITE(target_site):
    try:
        brows_ac = mechanize.Browser()
        brows_ac.set_handle_robots(False)
        brows_ac.open(target_site)
        print("IT'S OPEN: "+str(target_site))
        print("---"*7)
    except:
        pass

class NETWORK_OPS():
    def CONNECTION_MAC(target_ip):
        try:
            a_s = ARP(pdst=target_ip)
            b_b = Ether(dst="ff:ff:ff:ff:ff:ff")
            a_b = b_b/a_s
            a_l = srp(a_b,
                      timeout=2,
                      verbose=False)[0]
            return a_l[0][1].hwsrc
        except:
            pass
    def NETWORK_PACK(pkt_l):
        try:
            r_c = pd.read_csv("tracker_spec_ip.csv")
            r_p = pkt_l.sprintf("%Raw.load%")
            src_ip = pkt_l.getlayer(IP).src
            dst_ip = pkt_l.getlayer(IP).dst
            for ip_t in r_c["IP"]:
                if str(src_ip) == str(ip_t) or str(dst_ip) == str(ip_t):
                    PL.OUT().green_out(f"[>] TRACKER FOUND [IP]: {str(ip_t)}")
                else:
                    pass
        except:
            pass
    def NETWORK_LISTEN(self):
        try:
            sniff(filter="tcp",iface="Wi-Fi",
                  prn=NETWORK_OPS.NETWORK_PACK,
                  store=0)
        except:
            PL.OUT().unk_error()
            pass
    def SHOW_MAC(self,target_ip):
        try:
            c_m = NETWORK_OPS.CONNECTION_MAC(target_ip)
            if c_m != None and c_m:
                PL.OUT().info_out(f"[>] IP: {str(target_ip)} WITH MAC: {str(c_m)}")
            else:
                pass
        except:
            pass
    def INFO_SRC_DST_OPS(pkt_l):
        try:
            header_rand=AG.GET_HEADER_EXAMPLE()
            r_c = pd.read_csv("tracker_spec_ip.csv")
            r_p = pkt_l.sprintf("{IP:%IP.src% -> %IP.dst%\n}")
            src_ip = pkt_l.getlayer(IP).src
            dst_ip = pkt_l.getlayer(IP).dst
            print("[>>] INTERACTION - IP --> ",str(src_ip))
            if src_ip in r_c["IP"].values:
                if str(src_ip):
                    info_s = f"http://ipinfo.io/{str(src_ip)}/json"
                    att_req=requests.get(info_s,
                                         headers=header_rand,
                                         verify=False,
                                         timeout=3)
                    if att_req.status_code == 200:
                        Json_Res=json.loads(att_req.text)
                        print("---"*7)
                        try:
                            print("[>>] SRC INFO IP ",str(src_ip))
                        except:
                            pass
                        try:
                            print("HOSTNAME ",Json_Res["hostname"])
                        except:
                            pass
                        try:
                            print("CITY ",Json_Res["city"])
                        except:
                            pass
                        try:
                            print("ORGANIZATION ",Json_Res["org"])
                        except:
                            pass
                        print("---"*7)
                else:
                    pass
        except:
            pass
    def INFO_SRC_DST_ALL_OPS(pkt_l):
        try:
            header_rand=AG.GET_HEADER_EXAMPLE()
            r_c = pd.read_csv("tracker_spec_ip.csv")
            r_p = pkt_l.sprintf("{IP:%IP.src% -> %IP.dst%\n}")
            src_ip = pkt_l.getlayer(IP).src
            dst_ip = pkt_l.getlayer(IP).dst
            print("[>>] INTERACTION - IP --> ",str(src_ip))
            # if str(src_ip):
            #     info_s = f"http://ipinfo.io/{str(src_ip)}/json"
            #     att_req=requests.get(info_s,
            #                              headers=header_rand,
            #                              verify=False,
            #                              timeout=3)
            # if att_req.status_code == 200:
            #     Json_Res=json.loads(att_req.text)
            #     print("---"*7)
            #     try:
            #         print("HOSTNAME ",Json_Res["hostname"])
            #     except:
            #         pass
            #     try:
            #         print("CITY ",Json_Res["city"])
            #     except:
            #         pass
            #     try:
            #         print("ORGANIZATION ",Json_Res["org"])
            #     except:
            #         pass
            #     print("---"*7)
            # else:
            #     pass
        except Exception as err:
            print(str(err))
            pass
    def NETWORK_PACK_TCP_IP_SESSION(pkt_l):
        try:
            r_c = pd.read_csv("tracker_spec_ip.csv")
            r_p = pkt_l.sprintf("{IP:%IP.src% -> %IP.dst%\n}")
            src_ip = pkt_l.getlayer(IP).src
            dst_ip = pkt_l.getlayer(IP).dst
            for ip_t in r_c["IP"]:
                if str(src_ip) == str(ip_t):
                    PL.OUT().green_out(f"[>] SRC TRACKER FOUND [IP]: {str(ip_t)}")
                elif str(dst_ip) == str(ip_t):
                    PL.OUT().green_out(f"[>] DST TRACKER FOUND [IP]: {str(ip_t)}")
                else:
                    pass
        except:
            pass
    def SHOW_IP_SRC_CONNECTION_INFORMATIONS(self):
        try:
            sniff(filter="tcp",session=TCPSession,
                      prn=NETWORK_OPS.INFO_SRC_DST_OPS,
                      store=0)
        except:
            PL.OUT().unk_error()
            pass
    def SHOW_IP_SRC_CONNECTION_ALL_INFORMATIONS(self):
        try:
            sniff(filter="tcp",session=TCPSession,
                      prn=NETWORK_OPS.INFO_SRC_DST_ALL_OPS,
                      store=0)
        except:
            PL.OUT().unk_error()
            pass
    def TCPSESSION_LISTEN(self):
        try:
            un_r = sniff(session=TCPSession,
                  prn=NETWORK_OPS.NETWORK_PACK_TCP_IP_SESSION,
                  store=False)
        except:
            PL.OUT().unk_error()
            pass
    def IPSESSION_LISTEN(self):
        try:
            un_r = sniff(session=IPSession,
                  prn=NETWORK_OPS.NETWORK_PACK_TCP_IP_SESSION,
                  store=False)
        except:
            PL.OUT().unk_error()
            pass
        
        
class IP_URL_SOCKET():
    def GET_URL_IP(self,dom_host=str):
        try:
            n_s = dom_host.replace(" ","")\
                .replace("https://","")\
                    .replace("http://","")\
                        .replace("www.","")
            ip_s = socket.gethostbyname(n_s)
            return ip_s,n_s
        except:
            pass
        
        
class CONNECTION_OPS():
    def LAUNCH_PROCESS():
        c_o = type("INFORMATION MAC",
                   (NETWORK_OPS,
                    IP_URL_SOCKET,),
                   {})
        co_l = c_o()
        return co_l