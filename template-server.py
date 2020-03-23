from flask import Flask, current_app, g, session, request, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/test/video")
def hellovideo():
    return render_template("video.html")


# route specify
@app.route("/test/hello")
def hello():
    return "<h1>Hello !</h1>"


@app.route("/test/var/<var>")
def testVar(var):
    return str(var)


@app.route("/test/int/<int:var>")
def testint(var):
    return str(var)


@app.route("/test/path/<path:var>")
def testPath(var):
    return str(var)


@app.route("/test/float/<float:var>")
def testFloat(var):
    return str(var)


@app.route("/test/float/<int:var>")  # 只会匹配动态片段 var 为 int的url
def testFloatInt(var):
    return str(var)


@app.route("/test/float/<int:var>", methods=["POST"])  # method 默认get,,
def testPostFloatInt(var):
    return str(var)


@app.route("/test/pon")  # method 默认get,,
def pon():
    return jsonify([request.method, str(request.headers)], str(request.args))


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["the_file"]
        f.save("./static/" + secure_filename(f.filename))
        return "finished"
    else:
        return render_template("uploadFile.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
