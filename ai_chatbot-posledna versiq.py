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


formations = [
    "4-2-3-1", "4-3-3", "3-4-3", "4-2-4", "5-2-3", "5-4-1",
    "4-4-2", "4-4-1-1", "4-2-2-2", "3-5-2", "4-1-4-1",
    "3-2-4-1", "3-1-4-2", "5-2-1-2",
   
    "4-3-2-1", "4-5-1", "4-1-3-2", "3-3-4", "3-6-1", "4-6-0",
    "2-3-5", "3-3-3-1", "5-3-2", "5-3-1-1", "3-4-1-2",
    "4-3-1-2", "4-2-1-3", "3-4-2-1", "4-3-3 (False 9)", "4-3-3 (Wide wingers)",
    "3-5-1-1", "4-1-2-1-2", "4-1-2-3", "3-4-3 (Diamond midfield)", "3-4-3 (Flat midfield)",
    "4-2-3-1 (Wide midfielders)", "4-4-2 Diamond", "4-2-3-1 (Narrow midfield)", "3-5-2 (Wingbacks)"
]


biggerst_derbys = [
    "Bayern vs BVB",
    "Levski vs CSKA",
    "Barca vs Real Madrid",
    "Arsenal vs Tottenham",
    "Liverpool vs Everton",
    "Chelsea vs Tottenham",
    "Arsenal vs Chelsea",
    "AEK vs PAOK",
    "Manchester City vs Manchester United",
    "AC Milan vs Inter Milan",
    "Barcelona vs Real Madrid",
    "Liverpool vs Manchester United",
    "Bayern Munich vs Borussia Dortmund",
    "Sevilla vs Real Betis",
    "Liverpool vs Everton",
    "Celtic vs Rangers",
    "AS Roma vs Lazio",
    "Arsenal vs Tottenham Hotspur",
    "Real Madrid vs Atlético Madrid",
    "Benfica vs Sporting CP"
]


best_coaches = [
    "Jose Mourinho", "Pep Guardiola", "Alex Ferguson", "Urgen Klop", "Hansi Flick",
    "Joahim Low", "Lionel Scaloni", "Rodrigo de Zerby", "Johan Cruyf", "Carlo Ancelloty",
    "Rafa Benitez", "Muri Stoilov", "Unai Emery",
    "Zinedine Zidane", "Antonio Conte", "Marcelo Bielsa", "Didier Deschamps", "Diego Simeone",
    "Luis Enrique", "Thomas Tuchel", "Frank Rijkaard", "Roberto Mancini", "Arsène Wenger",
    "Mauricio Pochettino", "Ottmar Hitzfeld", "Vicente del Bosque", "Louis van Gaal", "Erik ten Hag"
]


Star_players = {
    "Ronaldo": [927, 240, 5, 4, "Portugal"],
    "Messi": [850, 381, 8, 6, "Argentina"],
    "Pele": [1283, 231, 3, 0, "Brazil"],
    "Fernando Torres": [302, 84, 0, 0, "Spain"],
        "Gerd Müller": [735, 200, 2, 4, "Germany"],
    "Luis Figo": [200, 180, 1, 0, "Portugal"],
    "Johan Cruyff": [400, 300, 3, 0, "Netherlands"],
    "Marco van Basten": [277, 120, 3, 1, "Netherlands"],
    "Raúl González": [323, 150, 0, 0, "Spain"],
    "Eusébio": [473, 200, 0, 1, "Portugal"],
    "Frank Lampard": [210, 180, 0, 0, "England"],
    "Steven Gerrard": [186, 150, 0, 0, "England"],
    "Clarence Seedorf": [120, 130, 0, 0, "Netherlands"],
    "Kaká": [170, 110, 1, 0, "Brazil"],
    "Dennis Bergkamp": [120, 150, 0, 0, "Netherlands"],
    "Roberto Carlos": [130, 110, 0, 0, "Brazil"],
    "Sergio Ramos": [120, 70, 0, 0, "Spain"],
    "Thiago Silva": [50, 30, 0, 0, "Brazil"],
    "David Beckham": [130, 150, 0, 0, "England"],
    "Alessandro Del Piero": [290, 120, 0, 0, "Italy"],
    "Zlatan Ibrahimović": [570, 180, 0, 0, "Sweden"],
    "Luis Suárez": [512, 225, 0, 0, "Uruguay"],
    "Wayne Rooney": [366, 145, 0, 0, "England"],
    "Raheem Sterling": [150, 90, 0, 0, "England"],
    "Sergio Agüero": [380, 110, 0, 0, "Argentina"],
    "Yaya Touré": [80, 100, 0, 0, "Ivory Coast"],
    "Paul Pogba": [90, 95, 0, 0, "France"],
    "Cesc Fàbregas": [100, 130, 0, 0, "Spain"],
    "Mesut Özil": [85, 170, 0, 0, "Germany"],
    "Angel Di María": [110, 150, 0, 0, "Argentina"],
    "Carlos Tévez": [210, 70, 0, 0, "Argentina"],
    "Roberto Mancini": [150, 90, 0, 0, "Italy"],
    "Gianfranco Zola": [160, 110, 0, 0, "Italy"],
    "Andriy Shevchenko": [175, 90, 1, 1, "Ukraine"],
    "Edinson Cavani": [250, 70, 0, 0, "Uruguay"],
    "Fernando Redondo": [40, 60, 0, 0, "Argentina"],
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
    "Porto": ["Primeira Liga", "Estádio do Dragão", "Sérgio Conceição", 30, "Diogo Costa"],
    "Ajax": ["Eredivisie", "Johan Cruyff Arena", "Mauricio Pochettino", 36, "Steven Berghuis"],
    "PSV Eindhoven": ["Eredivisie", "Philips Stadion", "Ruud van Nistelrooy", 24, "Joey Veerman"],
    "Feyenoord": ["Eredivisie", "De Kuip", "Arne Slot", 16, "Bryan Linssen"],
    "Galatasaray": ["Süper Lig", "Nef Stadium", "Okan Buruk", 23, "Kerem Aktürkoğlu"],
    "Fenerbahçe": ["Süper Lig", "Şükrü Saracoğlu Stadium", "İsmail Kartal", 29, "Enner Valencia"],
    "Beşiktaş": ["Süper Lig", "Vodafone Park", "Şenol Güneş", 17, "Rachid Ghezzal"],
    "Celtic": ["Scottish Premiership", "Celtic Park", " Brendan Rodgers", 53, "Kyogo Furuhashi"],
    "Rangers": ["Scottish Premiership", "Ibrox Stadium", "Michael Beale", 56, "James Tavernier"],
    "Olympiacos": ["Super League Greece", "Karaiskakis Stadium", "Michele Farris", 47, "Youssef El-Arabi"],
    "Panathinaikos": ["Super League Greece", "Apostolos Nikolaidis Stadium", "Ivan Jovanović", 20, "Dimitris Kourbelis"],
    "Shakhtar Donetsk": ["Ukrainian Premier League", "NSC Olimpiyskiy (temporary)", "Igor Jovićević", 13, "Marcos Antônio"],
    "Dynamo Kyiv": ["Ukrainian Premier League", "NSC Olimpiyskiy", "Mircea Lucescu", 16, "Viktor Tsyhankov"],
    "Zenit St Petersburg": ["Russian Premier League", "Krestovsky Stadium", "Sergey Semak", 9, "Sardar Azmoun"],
    "CSKA Moscow": ["Russian Premier League", "VEB Arena", "Viktor Goncharenko", 13, "Fedor Chalov"],
    "Spartak Moscow": ["Russian Premier League", "Otkritie Arena", "Oleg Kononov", 23, "Jordan Larsson"],
    "Lazio": ["Serie A", "Stadio Olimpico", "Maurizio Sarri", 2, "Ciro Immobile"],
    "Roma": ["Serie A", "Stadio Olimpico", "Claudio Raniery", 3, "Paulo Dybala"],
    "Sassuolo": ["Serie A", "Mapei Stadium", "Paolo Nicolato", 0, "Domenico Berardi"],
    "Bologna": ["Serie A", "Stadio Renato Dall'Ara", "Vincenco Italiano", 0, "Riccardo Orsolini"],
    "Torino": ["Serie A", "Stadio Olimpico Grande Torino", "Ivan Jurić", 7, "Sasa Lukic"],
    "Real Betis": ["La Liga", "Benito Villamarín", "Manuel Pellegrini", 1, "Nabil Fekir"],
    "Villarreal": ["La Liga", "Estadio de la Cerámica", "Quique Setién", 0, "Arnaut Danjuma"],
    "Athletic Bilbao": ["La Liga", "San Mamés", "Ernesto Valverde", 8, "Iker Muniain"],
    "Espanyol": ["La Liga", "RCDE Stadium", "Luis García", 0, "Raúl de Tomás"],
    "Levante": ["La Liga", "Ciutat de València", "Javi Calleja", 0, "José Luis Morales"],
    "Real Valladolid": ["La Liga", "José Zorrilla Stadium", "Pacheta", 0, "Óscar Plano"],
    "Santos": ["Brasileirão", "Vila Belmiro", "Osmar Loss", 8, "Marinho"],
    "Flamengo": ["Brasileirão", "Maracanã", "Vanderlei Luxemburgo", 8, "Gabriel Barbosa"],
    "Palmeiras": ["Brasileirão", "Allianz Parque", "Abel Ferreira", 12, "Raphael Veiga"],
    "Corinthians": ["Brasileirão", "Neo Química Arena", "Vítor Pereira", 7, "Willian"],
    "São Paulo FC": ["Brasileirão", "Morumbi", "Rogério Ceni", 6, "Jonathan Calleri"],
    "Boca Juniors": ["Primera División Argentina", "La Bombonera", "Sebastián Battaglia", 35, "Darío Benedetto"],
    "River Plate": ["Primera División Argentina", "Monumental", "Marcelo Gallardo", 38, "Julián Álvarez"],
    "Vasco da Gama": ["Brasileirão", "São Januário", "Lisca", 4, "Andrey"],
    "Grêmio": ["Brasileirão", "Arena do Grêmio", "Renato Portaluppi", 3, "Ferreira"],
    "Cruz Azul": ["Liga MX", "Estadio Azteca", "Ricardo Ferretti", 9, "Orbelín Pineda"],
    "América": ["Liga MX", "Estadio Azteca", "Fernando Ortiz", 14, "Henry Martín"],
    "Chivas Guadalajara": ["Liga MX", "Estadio Akron", "Veljko Paunović", 12, "José Juan Macías"],
    "Tigres UANL": ["Liga MX", "Estadio Universitario", "Miguel Herrera", 8, "André-Pierre Gignac"],
    "Monterrey": ["Liga MX", "Estadio BBVA", "Víctor Manuel Vucetich", 5, "Rogelio Funes Mori"],
    "Al Ahly": ["Egyptian Premier League", "Cairo International Stadium", "Juan Carlos Osorio", 43, "Mohamed Sherif"],
    "Zamalek": ["Egyptian Premier League", "Cairo International Stadium", "Juan Carlos Osorio", 14, "Shikabala"],
    "Al Hilal": ["Saudi Pro League", "King Fahd Stadium", "Rene Weiler", 19, "Salem Al-Dawsari"],
    "Al Nassr": ["Saudi Pro League", "Mrsool Park", "Rudi Garcia", 10, "Talisca"],
    "Melbourne Victory": ["A-League", "AAMI Park", "Tony Popovic", 4, "Jake Brimmer"],
    "Sydney FC": ["A-League", "Allianz Stadium", "Steve Corica", 5, "Kosta Barbarouses"],
    "LA Galaxy": ["MLS", "Dignity Health Sports Park", "Greg Vanney", 5, "Chicharito"],
    "Atlanta United": ["MLS", "Mercedes-Benz Stadium", "Gonzalo Pineda", 1, "Miguel Almirón"],
    "Seattle Sounders": ["MLS", "Lumen Field", "Brian Schmetzer", 2, "Raúl Ruidíaz"]
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
    "Mexico": ["Estadio Azteca", "Jaime Lozano", 0, "Hirving Lozano"],
    "USA": ["Mercedes-Benz Stadium", "Gregg Berhalter", 0, "Christian Pulisic"],
    "Japan": ["Saitama Stadium", "Hajime Moriyasu", 0, "Takefusa Kubo"],
    "South Korea": ["Seoul World Cup Stadium", "Jürgen Klinsmann", 0, "Son Heung-min"],
    "Australia": ["Stadium Australia", "Graham Arnold", 0, "Mathew Leckie"],
    "Switzerland": ["St. Jakob-Park", "Murat Yakin", 0, "Granit Xhaka"],
    "Poland": ["National Stadium Warsaw", "Michał Probierz", 0, "Robert Lewandowski"],
    "Serbia": ["Rajko Mitić Stadium", "Dragan Stojković", 0, "Dušan Vlahović"],
    "Colombia": ["Metropolitano Stadium", "Néstor Lorenzo", 0, "Luis Díaz"],
    "Chile": ["Estadio Nacional", "Ricardo Gareca", 0, "Alexis Sánchez"],
    "Turkey": ["Atatürk Olympic Stadium", "Vincenzo Montella", 0, "Hakan Çalhanoğlu"],
    "Norway": ["Ullevaal Stadion", "Ståle Solbakken", 0, "Erling Haaland"],
    "Sweden": ["Friends Arena", "Janne Andersson", 0, "Alexander Isak"],
    "Ukraine": ["NSC Olimpiyskiy", "Serhiy Rebrov", 0, "Mykhailo Mudryk"],
    "Czech Republic": ["Eden Arena", "Jaroslav Šilhavý", 0, "Patrik Schick"],
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
               if player.lower() in user_message.lower():
                 info = Star_players[player]
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