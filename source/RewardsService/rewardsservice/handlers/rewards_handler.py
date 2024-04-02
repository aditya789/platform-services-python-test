import json
import tornado.web
import motor
from pymongo import MongoClient
from tornado.gen import coroutine

class RewardsHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        rewards = list(db.rewards.find({}, {"_id": 0}))
        self.write(json.dumps(rewards))

class TestHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        self.render('base_page.html')


class FetchCustomerDataHandler(tornado.web.RequestHandler):
    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client.get_database("Rewards")  
        collection = db.get_collection("Customer")  
        customers = list(collection.find())
        self.render("index.html", customers=customers)

class AddCustomerDataHandler(tornado.web.RedirectHandler):
    @coroutine
    def post(self):
        customer_email = self.get_argument("customer_email")
        order = self.get_argument("order")
        client = MongoClient("mongodb", 27017)
        db = client.get_database("Rewards")
        collection = db.get_collection("Customer")
        collection.insert_one({"customer_email": customer_email, "order": order,})
        self.redirect("/")

    