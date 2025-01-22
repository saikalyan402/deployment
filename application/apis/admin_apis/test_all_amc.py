from application.model.model import db, Company
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from application.apis.helper_fun import is_admin

class test_AllAmcNames(Resource):
    def get(self):
        try:
            companys = Company.query.all()
            all_amc_names = [company.name for company in companys]
            return {"status": "success", "data": all_amc_names}, 200
        except Exception as e:
            print(f"Error fetching AMC names: {e}")
            return {"status": "error", "message": e}, 500
