from flask import Flask, render_template, request, jsonify
import torch
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models

app = Flask(__name__)

correct_count = int(0.9899 * 1184)
wrong_count = int((1 - 0.9899) * 1184)


# using model trained  in Pytorch_Day_04
model = models.resnet18()
model.load_state_dict(torch.load("../model_sec"))
model.eval()

classes = ["Chihuahua", "Muffin"]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


@app.route("/")
def main():
    total = correct_count + wrong_count
    accuracy = correct_count / total if total > 0 else 0
    return render_template(
        "main.html",
        correct=correct_count,
        wrong=wrong_count,
        accuracy=accuracy
    )


@app.route("/predict", methods=["POST", "GET"])
def predict():
    file = request.files["image"]
    image = Image.open(file).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
    return jsonify({
        "prediction": classes[preds.item()]
    })


@app.route("/feedback", methods=["POST"])
def feedback():
    global correct_count, wrong_count

    data = request.get_json()
    if data["correct"]:
        correct_count += 1
    else:
        wrong_count += 1

    total = correct_count + wrong_count
    accuracy = (correct_count / total)

    return jsonify({
        "correct": correct_count,
        "wrong": wrong_count,
        "accuracy": accuracy
    })


if __name__ == "__main__":
    app.run(port=5068, debug=True)

