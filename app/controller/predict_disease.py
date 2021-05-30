from flask_restplus import Resource, Namespace
from flask import request
from app.services.predict_disease import predict_disease
import pandas as pd

ns = Namespace("Predict Disease", description="Predict Illness based on symptoms", path="/disease")

parser = ns.parser()
parser.add_argument('PatientData', type='FileStorage', location='files')


@ns.route("/get-tumor-status")
class UploadCSV(Resource):
    @ns.expect(parser)
    def post(self):
        patient_data = request.files['PatientData']
        patient_df = pd.read_csv(patient_data)
        return predict_disease(patient_df)
