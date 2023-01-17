# gcore-ddns

## 配置项
```
python gcore-ddns.py -h
usage: gcore-ddns.py [-h] [--token TOKEN] [--domain DOMAIN] [--value VALUE] [--sub SUB] [--type TYPE] [--ttl TTL]

gcore ddns client

options:
  -h, --help       show this help message and exit
  --token TOKEN    token -> token text file path
  --domain DOMAIN  domain -> zone domain.
  --value VALUE    value -> record ip. default is get from ipconfig.me
  --sub SUB        sub -> sub.domain
  --type TYPE      type -> default record type is A
  --ttl TTL        ttl -> default record ttl is 300
```
## 如何使用
填上配置项直接运行即可，子域不存在会自动创建。

IP 与远程一致则不会执行更新

预设获取 IP 接口为 ifconfig.me ，可自行更换。
