virtualenv venv
.venv/bin/activate or venv\Scripts\activate

pip install flask

python template-server.py

deactivate


常用的包文件
模板

基础模板

# 上传下载文件
<form action="upload" method="POST" enctype=multipart/form-data>
    <input type="file" name="the_file">
    <button type="submit">确定</button>
</form>

<a download="filename" href="url">
定义和用法
download 属性规定被下载的超链接目标。

在 <a> 标签中必须设置 href 属性。

该属性也可以设置一个值来规定下载文件的名称。所允许的值没有限制，浏览器将自动检测正确的文件扩展名并添加到文件 (.img, .pdf, .txt, .html, 等等)。

# 请求上下文
current_app
g
request
session


request.args.get('argv',alter)
request.headers
request.form

return somthing,404