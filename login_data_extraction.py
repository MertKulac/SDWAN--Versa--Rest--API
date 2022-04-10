def uuid (organization,device,headers,body,directory):
                uri= "https://" + directory + "/vnms/dashboard/applianceLocation/" + organization
                res = requests.get(uri, headers = headers ,data = body, verify=False)
                # print("uuid",res.text)
                veri = json.loads(res.text)
                veriuzunluk = len(veri['List']['value'])
 
                for i in range(veriuzunluk) :
                               if device in veri['List']['value'][i]['applianceName'] :
                                               uuid = veri['List']['value'][i]['applianceUuid']
                                               break
                return uuid
 
headers = {
"Authorization": "Basic XXXXXXXXXXXXXXXXXXXXXX=",  # This is your username/password encoded in Basic
                "Content-Type": "application/json",
                "Accept": "application/json"
 
}
body = {}             
 
uri = "https://" + directory + "/api/operational/devices/device/" + device + "/live-status/orgs/org/" + organization + "/sd-wan/sla-monitor/status/" + center + "/path-status"  
res = requests.get(uri, headers = headers ,data = body, verify=False)
# print(res.text)
veri = json.loads(res.text)
 
uuid1 = uuid(organization,device,headers,body,directory)
uri = "https://" + directory + "/vnms/dashboard/appliance/" + device + "/live?uuid=" + uuid1 + "&command=orgs/org/" + organization + "/sd-wan/sla-monitor/metrics/last-10s/" + center + "?deep"
res = requests.get(uri, headers = headers ,data = body, verify=False)
veri = json.loads(res.text)
