from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# อ่านค่าจาก env (ตั้งใน docker-compose)
client = MongoClient(os.environ.get("MONGO_URI", "mongodb://mongo:27017/"))
db = client[os.environ.get("MONGO_DB", "netops")]
routers = db[os.environ.get("MONGO_COLL", "routers")]

@app.route("/")
def main():
    data = list(routers.find())
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_router():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")
    if ip and username and password:
        routers.insert_one({"ip": ip, "username": username, "password": password})
    return redirect(url_for("main"))

@app.route("/delete/<rid>", methods=["POST"])
def delete_router(rid):
    routers.delete_one({"_id": ObjectId(rid)})
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
