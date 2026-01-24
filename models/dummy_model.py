import random

DIALECTS = [
    "Dhaka", "Chittagong", "Sylhet", "Rajshahi",
    "Rangpur", "Khulna", "Barisal", "Mymensingh",
    "Noakhali", "Comilla", "Faridpur", "Pabna"
]

def predict(audio):
    probs = [random.random() for _ in DIALECTS]
    total = sum(probs)
    probs = [p / total for p in probs]
    return dict(zip(DIALECTS, probs))
