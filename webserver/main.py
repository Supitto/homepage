from flask import Flask, render_template

php = Flask(__name__)

@php.route("/",methods=['GET'])
def root():
    return render_template("root.html")

php.run(host="0.0.0.0",port=80)
