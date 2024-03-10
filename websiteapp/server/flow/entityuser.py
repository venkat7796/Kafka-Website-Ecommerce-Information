from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import EntityUserSchema

blp = Blueprint("entityuser",__name__,description="Customers created in the system")


@blp.route("/api/v1/customer")
class CustomerView(MethodView):
    @blp.arguments(EntityUserSchema)
    def post(self,customer_payload):
        print(customer_payload)
        return {"Message": "Received"}, 200

        