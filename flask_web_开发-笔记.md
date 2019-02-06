# 第一章 安装
virtualenv venv
.venv/bin/activate or venv\Scripts\activate

pip install flask

python template-server.py

deactivate
# 第二章 程序的基本结构
## 2.1 初始化
```python
from flask import Flasdk
app = Flask(__name__)
```
通过`__name__` 来决定程序的根目录,一遍稍后能够找到相对于程序根目录的资源文件位置

## 2.2 路由和试图函数
@app.route('/test')
def index():
    return 'Hello!'

@app.route('/var/<name>')
def index():
    return 'Hello!'

## 2.3 启动服务器

## 2.4 一个完整的程序

## 2.5 请求响应循环
### 2.5.1 程序和请求上下文
### 2.5.2 请求调度
### 2.5.3 请求钩子
### 2.5.4 响应

# 第三章 模板
# 第四章
# 第五章
# 第六章
# 第七章
# 第八章
# 第九章
# 第十章
# 第十一章
# 第十二章
# 第十三章
# 第十四章
# 第十五章
# 第十六章
# 第十七章
# 第十八章
