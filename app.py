import os

from flask import Flask, render_template, request, send_from_directory, \
    make_response, redirect, flash
from werkzeug import secure_filename
import pypandoc

app = Flask(__name__)
app.config.from_object("config")

format_file = ["commonmark", "docbook", "docx", "epub", "haddock", "html", 
    "json", "latex", "markdown", "markdown_github", "markdown_mmd", 
    "markdown_phpextra", "markdown_strict", "mediawiki", "native",
    "odt", "opml", "org", "rst", "t2t", "textile", "twiki"]

@app.before_first_request
def before_first_request():
    os.system("wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-linux.tar.gz&&tar -xzvf pandoc-2.7.3-linux.tar.gz&&export pandoc=/app/pandoc-2.7.3/bin/pandoc")

@app.route("/")
def index():
    return render_template("index.html", format_file = format_file)

@app.route("/before-convert", methods=["POST"])
def before_convert():
    to = request.form.get("select")
    if 'file' not in request.files:
        flash('没有文件上传')
        return redirect("/")
    file = request.files['file']
    if file.filename == '':
        flash('没有文件上传')
        return redirect("/")
    if file:
        filename = secure_filename(file.filename)
        file.save("convert/" + filename)
        try:
            content = pypandoc.convert_file("convert/" + filename, to)
        except RuntimeError:
            flash("文件格式错误！")
            return redirect("/")
        except OSError:
            flash("错误！")
            return redirect("/")
        os.remove("convert/" + filename)
        after_filename = filename.rsplit(".", 1)[0] + "." + to
        with open("convert/" + after_filename, "w", encoding="utf-8") as f:
            f.write(content)
        return redirect("/after-convert?filename=" + after_filename)

@app.route("/after-convert")
def convert_finish():
    filename = request.args.get("filename")
    return render_template("convert/after-convert.html", filename=filename)

@app.route("/download/<filename>")
def download(filename):
    directory = os.getcwd()
    response = make_response(send_from_directory(directory + "/convert", filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response

if __name__ == "__main__":
    app.run(port=9000, debug=True)