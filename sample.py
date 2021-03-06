import zoomeye.sdk as zoomeye
zm = zoomeye.ZoomEye(api_key="XXXXXXXX-XXXX-XXXXX-XXXX-XXXXXXXXXXX")
# pattern = 'apache country:cn'
pattern = input('pattern:')
# data = zm.dork_search(pattern)
# cidr:140.123.0.0/16
data = zm.multi_page_search(pattern,2)
# zoomeye.show_site_ip(data) # as it says, ex:None 69.163.238.224
# zoomeye.show_ip_port(data) # as it says, ex:45.116.241.186 40000

i=1
for l in data:
    print("num"+str(i))
    print("os: " + l['portinfo']['os'])
    print("ip: " + l['ip'])
    print("port: " + str(l['portinfo']['port']) + '\n')
    i=i+1

def dev_router(data):
    if(re.search('router',data['portinfo']['device'],re.I) != None):
        return data
    elif (re.search('router',data['portinfo']['app'],re.I) != None):
        return data
    else:
        return None

def dev_printer(data):
    if(re.search('printer',data['portinfo']['device'],re.I) != None):
        return data
    elif (re.search('printer',data['portinfo']['app'],re.I) != None):
        return data
    else:
        return None

def dev_cam(data):
    if(re.search('camera',data['portinfo']['device'],re.I) != None):
        return data
    elif(re.search('webcam',data['portinfo']['device'],re.I) != None):
        return data
    elif (re.search('camera',data['portinfo']['app'],re.I) != None):
        return data
    else:
        return None
    
    
def category_rec(data, device):
    state = 0
    for k,v in data.items():
        if type(v)==type(data):
            state = category_rec(v, device)
            if(state == 1):
                break
        else:
            if(re.search(device, str(v), re.I) != None):
                state = 1
                print(k,v)
                break
    return state
                
count = 0
for i in data:
    if (category_rec(i,r"\brouter\b")==1):
        count = count+1
        print(i['ip'])

count = 0
for i in data:
    if (category_rec(i,r"\bwap\b")==1):
        count = count+1
        print(i['ip'])
    
