# Srun_Autologin
深澜软件校园网自动登录（忽略证书验证）----南昌工学院实例 2023/10 
求个Star
# 安装依赖
 使用pip安装Selenium，运行命令
 ```
 pip install selenium
```
# 环境要求
确保您的系统上安装了Google Chrome浏览器（其他的也行，推荐Google）
因为用了
```
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
```
来忽略证书验证来直接进入Srun登录页面
# 食用方法
打开 Srun_Autologin.py
```
schoolWebURL = '你的校园网登录网址' 
username = '校园网账号'   
password = '校园网密码'    
domain = '运营商名称'  
```
输入完保存，运行即可（记得安装selenium依赖）
# 开机自动运行和记住密码
恩...在搞了（挖个坑，最近课太多了）
# 其他问题
大部分代码都有注释，有问题加QQ1824272506，备注Github
