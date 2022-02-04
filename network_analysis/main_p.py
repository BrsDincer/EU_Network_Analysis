from print_p import PRINT_LAST as PL
from loop_p import LOOP_OPS as LO
from document_p import TRANSFER_OUT as TO
from parameters_p import ADDITIONAL_GET as AG
from information_p import CONNECTION_OPS as CO
import mechanize,socket,re,webbrowser
from scapy.all import *
import pandas as pd


# TO.GET_INFO().domain_sub
# TO.GET_INFO().main_entry
# TO.GET_INFO().domain_list

# frame_dif = {}
# all_list = AG.GET_SPEC()
# for x_u in all_list:
#     for x_d in x_u:
#         try:
#             frame_dif[str(x_d)] = []
#             ip_h,_=CO.LAUNCH_PROCESS().GET_URL_IP(x_d)
#             PL.OUT().green_out(f"[>] IP: {str(ip_h)} TARGET: {str(x_d)}")
#             frame_dif[str(x_d)].append(str(ip_h))
#             CO.LAUNCH_PROCESS().SHOW_MAC(ip_h)
#         except:
#               pass
# series_spec = pd.Series(frame_dif)
# series_spec.to_csv("tracker_spec_ip.csv")
# print(frame_dif)


    
CO.LAUNCH_PROCESS().SHOW_IP_SRC_CONNECTION_ALL_INFORMATIONS()












