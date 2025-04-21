from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


responses = {
    "hello": "Hi , what do you want to know about football",
    "goodbye": "Goodbye, see you soon.",
    "exit": "Goodbye, see you soon."
}


formations = ["4-2-3-1", "4-3-3", "3-4-3", "4-2-4", "5-2-3", "5-4-1", "4-4-2", "4-4-1-1", "4-2-2-2", "3-5-2", "4-1-4-1", "3-2-4-1", "3-1-4-2", "5-2-1-2" ]

biggerst_derbys = ["Bayern vs BVB", "Levski vs CSKA", "Barca vs Real Madrid", "Arsenal vs Totenham", "Liverpool vs Everton", "Chelsea  vs Totenham" , "Arsenal vs Chelsea", "AEK vs PAOK", "Machester City vs Manchestar United "]

best_coaches = ["Jose Mourinho", "Pep Guardiola", "Alex Ferguson", "Urgen Klop", "Hansi Flick", "Joahim Low", "Lionel Scaloni", "Rodrigo de Zerby", "Johan Cruyf", "Carlo Ancelloty", "Rafa Benitez", "Muri Stoilov", "Unai Emery"]

Star_players = {
    "Ronaldo": [927, 240, 5, 4, "Portugal"],
    "Messi": [850, 381, 8, 6, "Argentina"],
    "Pele": [1283, 231, 3, 0, "Brazil"],
    "Fernando Torres": [302, 84, 0, 0, "Spain"],
    
    "Zinedine Zidane": [125, 100, 1, 1, "France"],
    "Ronaldinho": [280, 165, 1, 1, "Brazil"],
    "Diego Maradona": [312, 152, 0, 1, "Argentina"],
    "Cristiano Ronaldo": [890, 250, 5, 0, "Portugal"],
    "Thierry Henry": [411, 160, 0, 1, "France"],
    "Wayne Rooney": [366, 145, 0, 0, "England"],
    "Kylian Mbappé": [280, 120, 0, 1, "France"],
    "Erling Haaland": [200, 45, 0, 0, "Norway"],
    "Neymar": [450, 260, 0, 0, "Brazil"],
    "Luis Suárez": [512, 225, 0, 0, "Uruguay"],
    "Robert Lewandowski": [640, 170, 0, 0, "Poland"],
    "Karim Benzema": [435, 155, 1, 0, "France"],
    "Luka Modrić": [130, 130, 1, 0, "Croatia"],
    "Mohamed Salah": [300, 150, 0, 0, "Egypt"],
    "Sadio Mané": [250, 120, 0, 0, "Senegal"],
    "Zlatan Ibrahimović": [570, 180, 0, 0, "Sweden"],
    "Xavi Hernández": [100, 200, 0, 1, "Spain"],
    "Andrés Iniesta": [110, 190, 0, 1, "Spain"],
    "Gianluigi Buffon": [0, 0, 0, 1, "Italy"],
    "Andrea Pirlo": [80, 120, 0, 1, "Italy"],
    "Paolo Maldini": [40, 35, 0, 0, "Italy"],
    "Franz Beckenbauer": [75, 60, 2, 1, "Germany"],
    "Miroslav Klose": [280, 90, 0, 1, "Germany"],
    "Thomas Müller": [250, 190, 0, 1, "Germany"],
    "David Villa": [390, 90, 0, 1, "Spain"],
    "Antoine Griezmann": [260, 160, 0, 1, "France"],
    "Harry Kane": [350, 120, 0, 0, "England"],
    "George Weah": [200, 90, 1, 0, "Liberia"],
    "Didier Drogba": [300, 120, 0, 0, "Ivory Coast"],
    "Rivaldo": [336, 120, 1, 1, "Brazil"],
    "Roberto Baggio": [291, 100, 1, 0, "Italy"]
}


unknown_answers = ["Haven't heard about that", "I don't think I understand you", "I don't know what you are talking about"]
happy_responses = ["That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"]
angry_responses = ["That doesn't seem good", "That is awful"]

competitions = [
    "Champions League is the best tournament that has 36 teams competing every year!",
    "Europa League is the second-best tournament in Europe!",
    "UEFA Conference League is the weakest European tournament, but still interesting!"
]


teams = {
    "Barcelona": ["La Liga", "Camp Nou", "Hansi Flick", 5, "Lewandowski"],
    "Real Madrid": ["La Liga", "Santiago Bernabéu", "Carlo Ancelotti", 15, "Vinicius Jr."],
    "Manchester United": ["Premier League", "Old Trafford", "Ruben Amorim", 2, "Bruno Fernandes"],
    "Manchester City": ["Premier League", "Etihad Stadium", "Pep Guardiola", 9, "Erling Haaland"],
    "Liverpool": ["Premier League", "Anfield", "Arne Slot", 6, "Mohamed Salah"],
    "Chelsea": ["Premier League", "Stamford Bridge", "Enzo Maresca", 6, "Cole Palmer"],
    "Arsenal": ["Premier League", "Emirates Stadium", "Mikel Arteta", 13, "Bukayo Saka"],
    "Tottenham Hotspur": ["Premier League", "Tottenham Hotspur Stadium", "Ange Postecoglou", 2, "Heung-Min Son"],
    "Newcastle United": ["Premier League", "St James' Park", "Eddie Howe", 4, "Alexander Isak"],
    "Bayern Munich": ["Bundesliga", "Allianz Arena", "Vincent Kompany", 32, "Jamal Musiala"],
    "Borussia Dortmund": ["Bundesliga", "Signal Iduna Park", "Edin Terzić", 8, "Julian Brandt"],
    "RB Leipzig": ["Bundesliga", "Red Bull Arena", "Marco Rose", 0, "Dani Olmo"],
    "Bayer Leverkusen": ["Bundesliga", "BayArena", "Xabi Alonso", 1, "Florian Wirtz"],
    "PSG": ["Ligue 1", "Parc des Princes", "Luis Enrique", 11, "Kylian Mbappé"],
    "Marseille": ["Ligue 1", "Stade Vélodrome", "Jean-Louis Gasset", 9, "Pierre-Emerick Aubameyang"],
    "Lyon": ["Ligue 1", "Groupama Stadium", "Pierre Sage", 7, "Alexandre Lacazette"],
    "Monaco": ["Ligue 1", "Stade Louis II", "Adi Hütter", 8, "Wissam Ben Yedder"],
    "Inter Milan": ["Serie A", "San Siro", "Simone Inzaghi", 20, "Lautaro Martínez"],
    "AC Milan": ["Serie A", "San Siro", "Stefano Pioli", 19, "Rafael Leão"],
    "Juventus": ["Serie A", "Allianz Stadium", "Thiago Motta", 36, "Dusan Vlahovic"],
    "Napoli": ["Serie A", "Diego Armando Maradona Stadium", "Antonio Conte", 3, "Victor Osimhen"],
    "Atletico Madrid": ["La Liga", "Metropolitano", "Diego Simeone", 11, "Antoine Griezmann"],
    "Sevilla": ["La Liga", "Ramón Sánchez Pizjuán", "Quique Sánchez Flores", 1, "Youssef En-Nesyri"],
    "Real Sociedad": ["La Liga", "Reale Arena", "Imanol Alguacil", 2, "Mikel Oyarzabal"],
    "Benfica": ["Primeira Liga", "Estádio da Luz", "Roger Schmidt", 38, "Ángel Di María"],
    "Porto": ["Primeira Liga", "Estádio do Dragão", "Sérgio Conceição", 30, "Diogo Costa"]
}


national_teams = { 
    "Brazil": ["Maracanã", "Dorival Júnior", 5, "Pele"],
    "Argentina": ["Estadio Monumental", "Lionel Scaloni", 3, "Lionel Messi"],
    "France": ["Stade de France", "Didier Deschamps", 2, "Kylian Mbappé"],
    "Bulgaria": ["Vasil Levski", "Ilian Iliev", 0, "Stoichkov"],
    "Germany": ["Allianz Arena", "Julian Nagelsmann", 4, "Jamal Musiala"],
    "Spain": ["Santiago Bernabéu", "Luis de la Fuente", 1, "Pedri"],
    "England": ["Wembley Stadium", "Gareth Southgate", 1, "Harry Kane"],
    "Portugal": ["Estádio da Luz", "Roberto Martínez", 0, "Cristiano Ronaldo"],
    "Italy": ["Stadio Olimpico", "Luciano Spalletti", 4, "Federico Chiesa"],
    "Netherlands": ["Johan Cruyff Arena", "Ronald Koeman", 0, "Cody Gakpo"],
    "Uruguay": ["Estadio Centenario", "Marcelo Bielsa", 2, "Federico Valverde"],
    "Croatia": ["Stadion Maksimir", "Zlatko Dalić", 0, "Luka Modrić"],
    "Belgium": ["King Baudouin Stadium", "Domenico Tedesco", 0, "Kevin De Bruyne"],
    "Morocco": ["Prince Moulay Abdellah Stadium", "Walid Regragui", 0, "Achraf Hakimi"],
    "Senegal": ["Stade Léopold Sédar Senghor", "Aliou Cissé", 0, "Sadio Mané"]
}


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

   
    for key in responses:
        if key in user_message:
            return jsonify({"response": responses[key]})


    if "formation" in user_message:
        return jsonify({"response": f"One of the most used formations is {random.choice(formations)}."})
    if "formations" in user_message:
        return jsonify({"response": f"Here are all the formations I know {formations}."})

    if "derby" in user_message:
        return jsonify({"response": f"One of the biggest derbies is {random.choice(biggerst_derbys)}."})
    if "derbys" in user_message:
        return jsonify({"response": f"I know some derbies  {biggerst_derbys}."})
    if "team" in user_message:
     for team in teams:
        if team.lower() in user_message.lower():
            info = teams[team]
            return jsonify({
                "response": f"{team} plays in {info[0]}, their stadium is {info[1]}, the manager is {info[2]}, they’ve won {info[3]} titles, and their star player is {info[4]} ."
            })

    if "teams" in user_message:
        return jsonify({"response:" f"I know a lot of teams {teams}"})
    if "national teams" in user_message:
            for team in national_teams:
               if team.lower() in user_message.lower():
                 info = national_teams[team]
                 return jsonify({
                    "response": f"{team} plays on {info[0]}, their manager  is {info[1]}, they have won {info[2]} world cups , their best player of all time is {info[3]}."
            })
 
    if "coach" in user_message or "manager" in user_message:
        return jsonify({"response": f"One of the best couches is {random.choice(best_coaches)}."})
    if "player" in user_message:
        for player in Star_players:
               if team.lower() in user_message.lower():
                 info = Star_players[team]
                 return jsonify({
                    "response": f"{player} has {info[0]} goals and  {info[1]} assists,  {info[2]} ballon'ors  and  {info[3]} golden boots, he is from {info[4]} ."
            })
 

    if "competition" in user_message or "tournament" in user_message:
        return jsonify({"response": random.choice(competitions)})

    if "happy" in user_message:
        return jsonify({"response": random.choice(happy_responses)})

    if "angry" in user_message:
        return jsonify({"response": random.choice(angry_responses)})

    return jsonify({"response": random.choice(unknown_answers)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)