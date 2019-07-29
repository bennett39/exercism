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
        else:
            response["error"] = "No such URL"
        return json.dumps(response)

    def post(self, url, payload=None):
        response = {}
        payload = json.loads(payload) if payload else None
        if url == '/add':
            try:
                username = payload["user"]
            except IndexError:
                raise IndexError("No username provided")
            new_user_record = {
                "name": username,
                "owes": {},
                "owed_by": {},
                "balance": 0
            }
            self.database["users"].append(new_user_record)
            response = json.dumps(self.database["users"][-1])
        if url == '/iou':
            try:
                lender, borrower = payload["lender"], payload["borrower"]
                leant = borrowed = payload["amount"]
            except IndexError:
                return json.dumps({'error': 'Provide lender, borrower, and amount'})
            for user in self.database["users"]:
                if user["name"] == lender:
                    user["balance"] += leant
                    if borrower in user["owes"]:
                        leant = leant - user["owes"][borrower]
                        if leant < 0:
                            user["owes"][borrower] = abs(leant)
                        else:
                            del user["owes"][borrower]
                    if borrower not in user["owes"] and leant != 0:
                        user["owed_by"].setdefault(borrower, 0)
                        user["owed_by"][borrower] += leant
                if user["name"] == borrower:
                    user["balance"] -= borrowed
                    if lender in user["owed_by"]:
                        borrowed = borrowed - user["owed_by"][lender]
                        if borrowed < 0:
                            user["owed_by"][lender] = abs(borrowed)
                        else:
                            del user["owed_by"][lender]
                    if lender not in user["owed_by"] and borrowed != 0:
                        user["owes"].setdefault(lender, 0)
                        user["owes"][lender] += borrowed
            response = self.get('/users', json.dumps({'users': [lender, borrower]}))
        else:
            response = json.dumps({'error': 'No such URL'})
        return response
