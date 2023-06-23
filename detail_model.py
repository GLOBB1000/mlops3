import pickle
import joblib
import message_constants as mc
from data_methods import to_polynom

model_file_path = "moons_model.pkl"
scaler_file_path = "moons_scaler.pkl"

try:
    with open(model_file_path, 'rb') as model_storage:
        model = pickle.load(model_storage)

except Exception as inst:
    print(f"{mc.MODEL_READ_ERROR} {model_file_path} {inst.args}")

try:
    with open(scaler_file_path, 'rb') as scaler_storage:
        scaler = joblib.load(scaler_storage)

except Exception as inst:
    print(f"{mc.MODEL_READ_ERROR} {scaler_file_path} {inst.args}")


class DetailModel:
    def __init__(self):
        self.model = model

    def predict(self, detail_length: float, detail_width: float):
        """Detail validity prediction using user input
        - **detail_length**: detail length
        - **detail_width**: detail width
        """
        if detail_length <= 0 or detail_width < 0:
            return "Invalid measurements "\
                      "Measurements should be more than 0."
        try:
            if (model is not None) and (scaler is not None):
                scaled = scaler.transform([[detail_length, detail_width]])
                scaled = to_polynom(scaled, order=3)
                return model.predict(scaled)
            else:
                return mc.MODEL_READ_ERROR
        except Exception as e:
            return f"Parameters are not valid. {e}."\
                    f"I don't know what to say"
