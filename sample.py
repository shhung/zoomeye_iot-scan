import zoomeye.sdk as zoomeye
zm = zoomeye.ZoomEye(api_key="XXXXXXXX-XXXX-XXXXX-XXXX-XXXXXXXXXXX")
pattern = 'apache country:cn'
data = zm.dork_search(pattern)
# zoomeye.show_site_ip(data) # as it says, ex:None 69.163.238.224
# zoomeye.show_ip_port(data) # as it says, ex:45.116.241.186 40000

i=1
for l in data:
    print("num"+str(i))
    print("os: " + l['portinfo']['os'])
    print("ip: " + l['ip'])
    print("port: " + str(l['portinfo']['port']) + '\n')
    i=i+1
