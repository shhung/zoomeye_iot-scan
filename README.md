# zoomeye_iot-scan

## zoomeye sdk

[doc](https://www.zoomeye.org/doc)
```=python
import zoomeye.sdk as zoomeye
zm = zoomeye.ZoomEye(api_key="3******f-b**9-a***c-3**5-28******fd8") #API-KEY for 認證
pattern = 'apache country:cn'
page = input("page")
#data = zm.dork_search(pattern)
data = zm.multi_page_search(pattern,page)
# multi_page_search(dork, page=1, resource="host", facets=None)
#zoomeye.show_site_ip(data) # as it #says, ex:None 69.163.238.224
#zoomeye.show_ip_port(data) # as it says, ex:45.116.241.186 40000

i=1
for l in data:
    print("num"+str(i))
    print("os: " + l['portinfo']['os'])
    print("ip: " + l['ip'])
    print("port: " + str(l['portinfo']['port']) + '\n')
    i=i+1

```
## 建構搜尋關鍵字
category:value
邏輯運算表示
' ' 為 or 運算符
'+' 為 and 運算符-
'-' 為 not 運算符

## return of dork_search
data is list of dict, and there is still dict in dict.

## strucuture of dictionary of data

- protocol
    - application
    - transport
    - probe
    - probe_type
- ip
- geoinfo
    - continent
        - code
        - names
            - en
            - zh-CN
        - geoname_id
- protinfo
    - hostname
    - os
    - port
    - service
    - title
    - version
    - device
    - extrainfo
    - guess_service
    - rdns
    - app
    - banner
- timestamp
- honeypot
