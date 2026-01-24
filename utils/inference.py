from models.dummy_model import predict

def run_inference(audio):
    preds = predict(audio)
    return sorted(preds.items(), key=lambda x: x[1], reverse=True)
