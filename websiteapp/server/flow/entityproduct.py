from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import EntityProductSchema

blp = Blueprint("entityproduct",__name__,description="Products created in the system")


@blp.route("/api/v1/product")
class ProductView(MethodView):
    @blp.arguments(EntityProductSchema)
    def post(self,product_payload):
        print(product_payload)
        return {"Message": "Received"}, 200
    
        