from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    doc = nlp(user_input)
    intents = [ent.label_ for ent in doc.ents]
    return jsonify({"intents": intents, "response": "Intent processed successfully"})

if __name__ == "__main__":
    app.run(debug=True)
