:: --------------------------------------------------------------
::	项目: CloudflareSpeedTest 自动更新域名解析记录
::	版本: 1.0.4
::	作者: XIU2
::	项目: https://github.com/XIU2/CloudflareSpeedTest
:: --------------------------------------------------------------
::  功能：获取最快的9个IP，更新到 s1.example.com  ~~ s9.example.com
::  作者：evlon
::  项目： https://github.com/evlon/gcore-ddns
:: --------------------------------------------------------------

@echo off
Setlocal Enabledelayedexpansion

:: 这里可以自己添加、修改 CloudflareST 的运行参数，echo.| 的作用是自动回车退出程序（不再需要加上 -p 0 参数了）
echo.|CloudflareST.exe -o "result_ddns.txt" -f GcoreCDN-ip.txt -tl 100

:: 判断结果文件是否存在，如果不存在说明结果为 0
if not exist result_ddns.txt (
    echo.
    echo CloudflareST 测速结果 IP 数量为 0，跳过下面步骤...
    goto :END
)

set /a n=0,idx=1
for /f "tokens=1 delims=," %%i in (result_ddns.txt) do (
    Set /a n+=1 
    if "%%i"=="" (
        echo.
        echo CloudflareST 测速结果 IP 数量为 0，跳过下面步骤...
        goto :END
    )
    If !n! geq 2 if !idx! leq 9 (
        python gcore-ddns.py --token .gcore-api-token --domain 5kmm.cc --sub s!idx! --value %%i --ttl 120
        set /a idx+=1
    )
    
)
:END
pause
