from app import 
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage

api = Api(app, version='1.0', title='Team G API')
ns = api.namespace('api', description='API')

@ns.route('/predict', methods=['POST'])
@ns.expect(upload_parser)
class predictPost(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args['file']
        pass #return Response(json.dumps(predict_breed(file)), mimetype='application/json') # 