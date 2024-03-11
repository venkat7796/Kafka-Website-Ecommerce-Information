from flask.views import MethodView
from flask_smorest import Blueprint
from kafkaProducer.producer import consume_user_info
from schemas import EntityUserSchema
from flask import current_app
blp = Blueprint("entityuser",__name__,description="Customers created in the system")


@blp.route("/api/v1/customer")
class CustomerView(MethodView):
    @blp.arguments(EntityUserSchema)
    def post(self,customer_payload):
        print(customer_payload)
        current_app.queue.enqueue(consume_user_info,customer_payload)
        return {"Message": "Received"}, 200

        