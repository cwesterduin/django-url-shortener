
const db = connect("mongodb://localhost:27017/mydb")


db.urls.drop()

db.urls.insertMany([
    { url: "www.google.com" },

])