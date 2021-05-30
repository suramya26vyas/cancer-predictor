from ..utilities import LibraryUtilities


def predict_disease(patient_df):
    try:
        malign_status = False
        scalar, model = LibraryUtilities.get_trained_model_and_scalar()
        data_set = scalar.transform(patient_df.values.reshape(-1, 30))
        is_malign = model.predict_classes(data_set).reshape(1,)[0]
        if is_malign:
            malign_status = True
        return {"status": "Success", "TumorMalignant": malign_status}
    except Exception:
        raise
