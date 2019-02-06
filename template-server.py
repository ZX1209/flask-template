from flask import Flask,current_app,g,session,request,render_template,jsonify
app = Flask(__name__)

# route specify
@app.route('/test/hello')
def hello():
    return '<h1>Hello !</h1>'
@app.route('/test/var/<var>')
def testVar(var):
    return str(var)
@app.route('/test/int/<int:var>')
def testint(var):
    return str(var)
@app.route('/test/path/<path:var>')
def testPath(var):
    return str(var)
@app.route('/test/float/<float:var>')
def testFloat(var):
    return str(var)
@app.route('/test/float/<int:var>') # 只会匹配动态片段 var 为 int的url
def testFloatInt(var):
    return str(var)
@app.route('/test/float/<int:var>',methods=["POST"]) # method 默认get,,
def testPostFloatInt(var):
    return str(var)



if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)