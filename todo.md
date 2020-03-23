virtualenv venv
.venv/bin/activate or venv\Scripts\activate

pip install flask

python template-server.py

deactivate


常用的包文件
模板

基础模板



# 请求上下文
current_app
g
request
session


request.args.get('argv',alter)
request.headers
request.form

return somthing,404