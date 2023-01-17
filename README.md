# gdns

## 使用说明
```
python gdns.py -h
usage: gddns.py [-h] [--token TOKEN] [--domain DOMAIN] [--value VALUE] [--sub SUB] [--type TYPE] [--ttl TTL]

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

# gcore-ddns.bat

## 使用说明
配合 CloudflareSpeedTest 进行使用。
配置信息：请在gcore-config.ini

以下命令，获取gcore cdn ip 池， 然后利用 CloudflareSpeedTest 找到速度快的， 更新 gcore dns 的记录。 s1~s9.example.com

```
gdns.bat
```
输出结果：
```
D:\v2rayN-Core\优选IP\CloudflareST_windows_amd64>gdns.bat
'更新 Gcore cdn IP 完成'
# XIU2/CloudflareSpeedTest v2.1.0

开始延迟测速（模式：TCP，端口：443，平均延迟上限：100 ms，平均延迟下限：0 ms)
492 / 492 [---------------------------------------------------------------------------------------------------] 100.00%
开始下载测速（下载速度下限：0.00 MB/s，下载测速数量：9，下载测速队列：9）：
9 / 9 [-------------------------------------------------------------------------------------------------------] 100.00%
IP 地址           已发送  已接收  丢包率  平均延迟  下载速度 (MB/s)
92.223.116.208    4       4       0.00    91.79     0.00
92.223.116.220    4       4       0.00    92.65     0.00
92.223.116.222    4       4       0.00    93.11     0.00
92.223.116.221    4       4       0.00    93.55     0.00
92.223.116.206    4       4       0.00    94.41     0.00
92.223.116.214    4       4       0.00    94.92     0.00
92.223.116.205    4       4       0.00    95.56     0.00
92.223.116.207    4       4       0.00    96.95     0.00
92.223.116.211    4       4       0.00    97.40     0.00

完整测速结果已写入 result_ddns.txt 文件，可使用记事本/表格软件查看。
按下 回车键 或 Ctrl+C 退出。执行更新
{"id":526608,"name":"s1.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964406701207000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900357,"content":["92.223.116.208"],"enabled":true,"meta":{}}]}

执行更新
{"id":526649,"name":"s2.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964411076731000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900358,"content":["92.223.116.220"],"enabled":true,"meta":{}}]}

执行更新
{"id":527562,"name":"s3.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964416936375000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900359,"content":["92.223.116.222"],"enabled":true,"meta":{}}]}

执行更新
{"id":527571,"name":"s4.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964425460580000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900361,"content":["92.223.116.221"],"enabled":true,"meta":{}}]}

执行更新
{"id":527623,"name":"s5.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964429203271000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900362,"content":["92.223.116.206"],"enabled":true,"meta":{}}]}

执行更新
{"id":527624,"name":"s6.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964432481607000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900363,"content":["92.223.116.214"],"enabled":true,"meta":{}}]}

无需更新
未找到子域，执行创建
执行更新
{"id":527628,"name":"s8.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964441090106000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900364,"content":["92.223.116.207"],"enabled":true,"meta":{}}]}

未找到子域，执行创建
执行更新
{"id":527629,"name":"s9.example.com","type":"A","ttl":300,"meta":{},"updated_at":1673964445510435000,"filter_set_id":null,"filters":null,"resource_records":[{"id":64900365,"content":["92.223.116.211"],"enabled":true,"meta":{}}]}

请按任意键继续. . .

```