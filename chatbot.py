from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Основни отговори на ключови думи
responses = {
    "hello": "Здравей! Какво искаш да знаеш за футбола?",
    "goodbye": "Довиждане! Ще се видим отново.",
    "exit": "Довиждане! Ще се видим отново."
}

# Допълнителни данни
formations = ["4-2-3-1", "4-3-3", "3-4-3", "4-2-4", "5-2-3", "5-4-1", "4-4-2", "4-4-1-1", "4-2-2-2", "3-5-2", "4-1-4-1", "3-2-4-1", "3-1-4-2"]

biggerst_derbys = ["Bayern vs BVB", "Levski vs CSKA", "Barca vs Real Madrid", "Arsenal vs Totenham", "Liverpool vs Everton"]

best_coaches = ["Jose Mourinho", "Pep Guardiola", "Alex Ferguson", "Urgen Klop", "Hansi Flick", "Joahim Low", "Lionel Scaloni", "Rodrigo de Zerby", "Johan Cruyf", "Carlo Ancelloty", "Rafa Benitez", "Muri Stoilov", "Unai Emery"]

Star_players = {
    "Ronaldo": [927, 240, 5, 4, "Portugal"],
    "Messi": [850, 381, 8, 6, "Argentina"],
    "Pele": [1283, 231, 3, 0, "Brazil"],
    # ... съкращено за четимост, включи всички останали от твоя списък
    "Fernando Torres": [302, 84, 0, 0, "Spain"]
}

unknown_answers = ["Haven't heard about that", "I don't think I understand you", "I don't know what you are talking about"]
happy_responses = ["That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"]
angry_responses = ["That doesn't seem good", "That is awful"]

competitions = [
    "Champions League is the best tournament that has 36 teams competing every year!",
    "Europa League is the second-best tournament in Europe!",
    "UEFA Conference League is the weakest European tournament, but still interesting!"
]

# Отбори и национални отбори
teams = {
    "Barcelona": ["La Liga", "Camp Nou", "Hansi Flick", 5, "Lewandowski", 27],
    "Real Madrid": ["La Liga", "Santiago Bernabéu", "Carlo Ancelotti", 15, "Vinicius Jr.", 35],
    "Manchester United": ["Premier League", "Old Trafford", "Ruben Amorim", 2, "Bruno Fernandes", 20],
    # ... добави останалите отбори тук
}

national_teams = {
    "Brazil": ["Maracanã", "Dorival Júnior", 5, "Pele"],
    "Argentina": ["Estadio Monumental", "Lionel Scaloni", 3, "Lionel Messi"],
    "France": ["Stade de France", "Didier Deschamps", 2, "Kylian Mbappé"],
    "Bulgaria": ["Vasil Levski", "Ilian Iliev", 0, "Stoichkov"]
    # ... добави още ако искаш
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Проверка за ключови думи
    for key in responses:
        if key in user_message:
            return jsonify({"response": responses[key]})

    # Проверка за думи като "formation", "coach", "derby", "competition"
    if "formation" in user_message:
        return jsonify({"response": f"Една от най-често използваните формации е {random.choice(formations)}."})

    if "derby" in user_message:
        return jsonify({"response": f"Едно от най-големите дербита е {random.choice(biggerst_derbys)}."})

    if "coach" in user_message or "manager" in user_message:
        return jsonify({"response": f"Един от най-добрите треньори е {random.choice(best_coaches)}."})

    if "competition" in user_message or "tournament" in user_message:
        return jsonify({"response": random.choice(competitions)})

    if "happy" in user_message:
        return jsonify({"response": random.choice(happy_responses)})

    if "angry" in user_message:
        return jsonify({"response": random.choice(angry_responses)})

    return jsonify({"response": random.choice(unknown_answers)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
