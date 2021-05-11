
const db = connect("mongodb://localhost:27017/mydb")


db.app_url.drop()

db.app_url.insertMany([
    { url: "www.google.com" },
])