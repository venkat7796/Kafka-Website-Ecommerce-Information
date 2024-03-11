from flask.views import MethodView
from flask_smorest import Blueprint
from flask import current_app

from schemas import EntityProductSchema
from kafkaProducer.producer import consumer_product_info

blp = Blueprint("entityproduct",__name__,description="Products created in the system")


@blp.route("/api/v1/product")
class ProductView(MethodView):
    @blp.arguments(EntityProductSchema)
    def post(self,product_payload):
        print(product_payload)
        current_app.queue.enqueue(consumer_product_info,product_payload)
        return {"Message": "Received"}, 200
    
        