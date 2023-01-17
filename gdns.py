import json
import requests
import argparse

parser = argparse.ArgumentParser(description='gcore ddns client')
parser.add_argument('--token', type=str, default='', help='token -> token text file path')
parser.add_argument('--domain', type=str, default='example.com', help='domain -> zone domain.')
parser.add_argument('--value', type=str, default='', help='value -> record ip. default is get from ipconfig.me')
parser.add_argument('--sub', type=str, default='s1', help='sub -> sub.domain')
parser.add_argument('--type', type=str, default='A', help='type -> default record type is A')
parser.add_argument('--ttl', type=int, default=300, help='ttl -> default record ttl is 300')
args = parser.parse_args()



if args.token == '':
    print(args)
    exit(1)
else:
    tokenfile = args.token 
    domain = args.domain
    domainValue = args.value
    sub = args.sub
    type = args.type
    ttl = args.ttl

    token = ''
    with open(tokenfile,'r') as f:
        token = f.read()

    api_base = "https://api.gcorelabs.com/dns/v2/zones/"
    APIKey = "APIKey " + token
    headers = {"Authorization": APIKey}

    def get_record():
        url = api_base + domain + "/" + sub + "." + domain + "/" + type
        result = requests.get(url, headers=headers)
        if str(result.text).find("error") >= 0:
            print("未找到子域，执行创建")
            data = {"filters":[{"type":"default"}],"resource_records":[{"content":["0.0.0.0"]}], "ttl": 60}
            requests.post(url, data=data)
            return "0"
        return json.loads(result.text)["resource_records"][0]["content"][0]
        

    def update_record(domainValue):
        url = api_base + domain + "/" + sub + "." + domain + "/" + type
        data = {"resource_records":[{"content":[domainValue]}], "ttl": 300}
        result = requests.put(url, headers=headers, json=data)
        print(result.text)

    if domainValue == '':
        local_ip = requests.get("http://ifconfig.me")
        domainValue = local_ip.text

    if domainValue != get_record():
        print("执行更新")
        update_record(domainValue)
    else:
        print("无需更新")
