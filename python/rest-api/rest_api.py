import json

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        response = {}
        payload = json.loads(payload) if payload else None
        if url == '/users':
            if not payload:
                response["users"] = self.database["users"]
            else:
                response["users"] = [user for user in self.database["users"] if user["name"] in payload["users"]]
        return json.dumps(response)

    def post(self, url, payload=None):
        response = {}
        payload = json.loads(payload) if payload else None
        if url == '/add':
            try:
                username = payload["user"]
            except:
                raise IndexError("No username provided")
            new_user_record = {
                "name": username,
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(new_user_record)
            response = self.database["users"][-1]
        if url == '/iou':
            try:
                lender = payload["lender"]
                borrower = payload["borrower"]
                amount = payload["amount"]
            except:
                raise IndexError("Provide lender, borrower, and amount")
            for user in self.database["users"]:
                if user["name"] == lender:
                    user["owed_by"].setdefault(borrower, 0)
                    user["owed_by"][borrower] += amount
                    user["balance"] += amount
                if user["name"] == borrower:
                    user["owes"].setdefault(lender, 0)
                    user["owes"][lender] += amount
                    user["balance"] -= amount
            response = json.loads(self.get('/users', json.dumps({
                'users': [lender, borrower]
            })))
        return json.dumps(response)
