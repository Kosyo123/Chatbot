import random

def football_chatbot():
    print("⚽ Welcome to the Football Chatbot! ⚽")
    print("Ask me about teams, players, or football in general. Type 'exit' to end the chat.")
    formations = ["4-2-3-1", "4-3-3", "3-4-3", "4-2-4", "5-2-3", "5-4-1", "4-4-2", "4-4-1-1", "4-2-2-2", "3-5-2","4-1-4-1", "3-2-4-1", "3-1-4-2" ]
    biggerst_derbys  = ["Bayern vs BVB" , "Levski vs CSKA",  "Barca  vs Real Madrid" , "Arsenal vs Totenham" , "Liverpool vs Everton"]
    best_coaches = ["Jose Mourinho", "Pep Guardiola", "Alex Ferguson", "Urgen Klop", "Hansi Flick", "Joahim Low", "Lionel Scaloni", "Rodrigo de Zerby", "Johan Cruyf", "Carlo Ancelloty", "Rafa Benitez", "Muri Stoilov", "Unai Emery"]
    Star_players = {
        "Ronaldo": [927, 240, 5, 4, "Portugal"],
        "Messi": [850, 381, 8, 6, "Argentina"],
         "Pele": [1283, 231, 3, 0, "Brazil"],
        "Maradona": [345, 226, 1, 0, "Argentina"],
        "Zidane": [125, 165, 1, 0, "France"],
        "Neymar": [450, 290, 0, 0, "Brazil"],
        "Mbappe": [256, 122, 0, 1 , "France"],
        "Henry": [411, 207, 0, 2, "France"],
        "Ronaldo (R9)": [414, 113, 2, 1, "Brazil"],
        "Hristo Stoichkov": [332, 115, 1, 1, "Bulgaria"],
        "Cruyff": [433, 170, 3, 0, "Netherlands"],
        "Benzema": [457, 211, 1, 0, "France"],
        "Suarez": [521, 278, 0, 2, "Uruguay"],
        "Thomas Muller": [249, 264, 0, 0, "Germany"],
        "Franz Beckenbauer": [112, 74, 2, 0, "Germany"],
        "Roberto Baggio": [291, 130, 0, 0, "Italy"],
        "George Best": [205, 108, 0, 0, "Northern Ireland"],
        "Garrincha": [267, 85, 0, 0, "Brazil"],
        "Paolo Maldini": [40, 25, 0, 0, "Italy"],
        "Andrea Pirlo": [73, 140, 0, 0, "Italy"],
        "Xavi": [85, 185, 0, 0, "Spain"],
        "Iniesta": [57, 170, 0, 0, "Spain"],
        "Eusebio": [733, 231, 1, 0, "Portugal"],
        "Gerd Muller": [735, 103, 1, 0, "Germany"],
        "Marco van Basten": [300, 92, 3, 0, "Netherlands"],
        "Michel Platini": [312, 101, 3, 0, "France"],
        "Ronaldinho": [313, 162, 1, 0, "Brazil"],
        "Samuel Eto'o": [426, 118, 0, 0, "Cameroon"],
        "David Beckham": [146, 211, 0, 0, "England"],
        "Steven Gerrard": [185, 154, 0, 0, "England"],
        "Frank Lampard": [303, 174, 0, 0, "England"],
        "Didier Drogba": [362, 116, 0, 0, "Ivory Coast"],
        "Kaka": [237, 164, 1, 0, "Brazil"],
        "Wayne Rooney": [366, 206, 0, 0, "England"],
        "Ryan Giggs": [168, 247, 0, 0, "Wales"],
        "Alessandro Del Piero": [346, 145, 0, 0, "Italy"],
        "Cafu": [40, 98, 0, 0, "Brazil"],
        "Patrick Vieira": [68, 82, 0, 0, "France"],
        "Andriy Shevchenko": [376, 102, 0, 1, "Ukraine"],
        "Lothar Matthaus": [227, 151, 1, 0, "Germany"],
        "Raul": [435, 143, 0, 0, "Spain"],
        "Carlos Valderrama": [74, 215, 0, 0, "Colombia"],
        "Zico": [516, 130, 0, 0, "Brazil"],
        "Eric Cantona": [166, 88, 0, 0, "France"],
        "Clarence Seedorf": [135, 125, 0, 0, "Netherlands"],
        "Rivaldo": [389, 138, 1, 0, "Brazil"],
        "Fernando Torres": [302, 84, 0, 0, "Spain"]
    }

    teams = {
    "Barcelona": ["La Liga", "Camp Nou", "Hansi Flick", 5, "Lewandowski", 27],
    "Real Madrid": ["La Liga", "Santiago Bernabéu", "Carlo Ancelotti", 15, "Vinicius Jr.", 35],
    "Manchester United": ["Premier League", "Old Trafford", "Ruben Amorim", 2, "Bruno Fernandes", 20],
    "Liverpool": ["Premier League", "Anfield", "Arne Slot", 6, "Salah", 19],
    "Bayern Munich": ["Bundesliga", "Allianz Arena", "Vincent Kompany", 6, "Kane", 32],
    "Atletico Madrid": ["La Liga", "Metropolitano", "Diego Simeone", 0, "Julian Alvarez", 11],
    "Bayer Leverkusen": ["Bundesliga", "Bay Arena", "Xabi Alonso", 0, "Florian Wirtz", 1],
    "Milan": ["Serie A", "San Siro", "Sergio Conceicao", 7, "Rafael Leao", 19],
    "Inter Milan": ["Serie A", "Giuseppe Meazza", "Simone Inzaghi", 3, "Lautaro Martinez", 19],
    "Manchester City": ["Premier League", "Etihad", "Pep Guardiola", 1, "Erling Haaland", 9],
    "PSG": ["Ligue 1", "Parc des Princes", "Luis Enrique", 0, "Ousmane Dembele", 11],
    "Juventus": ["Serie A", "Allianz Stadium", "Thiago Motta", 2, "Dusan Vlahovic", 36],
    "Chelsea": ["Premier League", "Stamford Bridge", "Enzo Maresca", 2, "Cole Palmer", 6],
    "Arsenal": ["Premier League", "Emirates Stadium", "Mikel Arteta", 0, "Bukayo Saka", 13],
    "Borussia Dortmund": ["Bundesliga", "Signal Iduna Park", "Niko Kovac", 1, "Sergej Giurassi", 5],
    "Sevilla": ["La Liga", "Ramón Sánchez Pizjuán", "Quique Sánchez Flores", 1, "Youssef En-Nesyri", 1],
    "Roma": ["Serie A", "Stadio Olimpico", "Claudio Ranieri", 0, "Paulo Dybala", 3],
    "Levski": ["efbet liga", "Gerena", "Hulio Velazquez", 0, "Sangare", 27],
    "Aston Villa": ["Premier League", "Villa Park", "Unai Emery", 0, "Morgan Rogers", 7],
    "CSKA": ["efbet liga", "Bulgarska armiq", "Aleksandur Tomash", 0, "Estrada", 31],
    "Minyor Bobovdol" : ["a okrujna", "Shulc", "Kaloqn", 0, "Gosho", 0],
    "Everton" : ["Premier League", "Goodinson park" , "David Moyes",0, "Calvert-Lewin", 9],
    "Totenham Hotspur" : ["Premier League", "Tottenham hotspur stadium", "Ange Postecoglu", 0, "Son", 0],
    "Sporting" : ["Portugal League", "Estadio Jose Alvalade", "Joao Pereira", 0,"Victor Gyokeres", 24],
    "Porto" : ["Portugal League", "Estadio Dedragao", " Martin Anselmi" , 2, "Diogo Costa", 30 ],
    "Leeds United": ["Championship", "Elland Road", "Daniel Farke", 0, "Daniel James", 3],
    "Southampton": ["Championship", "St Mary's Stadium", "Russell Martin", 0, "Adam Armstrong", 2],
    "Leicester City": ["Premier League", "King Power Stadium", "Ruud Van Nilsteroy", 0, "Jamie Vardy", 2],
    "Ipswich Town": ["Premier League", "Portman Road", "Kieran McKenna", 0, "Conor Chaplin", 1],
    "Sunderland": ["Championship", "Stadium of Light", "Michael Beale", 0, "Jack Clarke", 2],
    "Benfica": ["Portugal League", "Estádio da Luz", "Roger Schmidt", 2, "João Neves", 38],
    "Braga": ["Portugal League", "Estádio Municipal de Braga", "Artur Jorge", 3, "Ricardo Horta", 8],
    "Vitória SC": ["Portugal League", "Estádio D. Afonso Henriques", "Álvaro Pacheco", 3, "André Silva", 0],
    "Ajax": ["Eredivisie", "Johan Cruyff Arena", "John van 't Schip", 2, "Brian Brobbey", 36],
    "PSV Eindhoven": ["Eredivisie", "Philips Stadion", "Peter Bosz", 0, "Neo Lang", 24],
    "Feyenoord": ["Eredivisie", "De Kuip", "Robin Van Persie", 0, "Santiago Giménez", 16],
    "AZ Alkmaar": ["Eredivisie", "AFAS Stadion", "Pascal Jansen", 0, "Vangelis Pavlidis", 9],
    "Twente": ["Eredivisie", "De Grolsch Veste", "Joseph Oosting", 0, "Sem Steijn", 0],
    "Marseille": ["Ligue 1", "Stade Vélodrome", "Jean-Louis Gasset", 0, "Pierre-Emerick Aubameyang", 10],
    "Lyon": ["Ligue 1", "Groupama Stadium", "Pierre Sage", 0, "Ryan Cherki", 7],
    "Monaco": ["Ligue 1", "Stade Louis II", "Adi Hütter", 0, "Wissam Ben Yedder", 18],
    "Lille": ["Ligue 1", "Stade Pierre-Mauroy", "Paulo Fonseca", 0, "Jonathan David", 9]

    }
    national_teams = {
        
    "Brazil": [ "Maracanã", "Dorival Júnior", 5, "Pele"],
    "Argentina": [ "Estadio Monumental", "Lionel Scaloni", 3, "Lionel Messi"],
    "France": [ "Stade de France", "Didier Deschamps", 2, "Kylian Mbappé"],
    "Germany": [ "Allianz Arena", "Julian Nagelsmann", 4, "Franc Bekenbauer"],
    "Spain": [ "Santiago Bernabéu", "Luis de la Fuente", 1, "Iniesta"],
    "England": [ "Wembley Stadium", "Thomas Tuchel", 1, "Bobby Charalton"],
    "Portugal": [ "Estádio da Luz", "Roberto Martínez", 0, "Cristiano Ronaldo"],
    "Italy": [ "Stadio Olimpico", "Luciano Spalletti", 4, "Felipe Inzagi"],
    "Netherlands": [ "Johan Cruyff Arena", "Ronald Koeman", 0, "Yohan Cruyf"],
    "Uruguay": [ "Estadio Centenario", "Marcelo Bielsa", 2, "Luis Suarez"],
    "Bulgaria" : ["Vasil Levski", "Ilian Iliev", 0, "Stoichkov"]
    }

    unknown_answers = ["Haven't heard about that", "I dont think i understand you", "I dont know what you are talking about"]
    happy_responses = [
        "That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"
    ]

    competitions = [
        "Champions League is the best tournament that has 36 teams competing every year!",
        "Europa League is the second-best tournament in Europe!",
        "UEFA Conference League is the weakest European tournament, but still interesting!"
    ]

    angry_responses = ["That doesn't seem good", "That is awful"]

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit' or user_input == "bye":
            print("Goodbye! ⚽")
            break
        elif "great players" in user_input:
            print ("I know a lot of good players")
            for man in Star_players:
                print(man)
        elif any(player.lower() in user_input for player in Star_players):
            for player, info in Star_players.items():
                if player.lower() in user_input:
                    print(f"{player} has scored {info[0]} goals, provided {info[1]} assists, won {info[2]} Ballon d'Ors, and {info[3]} Golden Boots. He is from {info[4]}")
        elif "derby" in user_input:
            print("I know some derbyes in Europe")
            for i in biggerst_derbys:
                print(i)
        elif "team" in user_input:
            print("I know about these teams:", ", ".join(teams.keys()))
        elif "show me a random team" in user_input:
            print(random.choice(teams))
        elif any(team.lower() in user_input for team in teams):
            for team, info in teams.items():
                if team.lower() in user_input:
                    print(f"{team} plays in the {info[0]}, their stadium is {info[1]}, the coach is {info[2]}, they have won {info[3]} Champions Leagues, and their star player is {info[4]} , and thay have won {info[5]} leagues.")
        elif    "formations" in user_input:
            print("I know quite a lot football formations")
            for i in  formations:
                print(i)
        elif "players" in user_input:
            print("I know these famous players: Lewandowski, Vinicius Jr., Rashford, Salah, Kane")
        elif "coaches" in user_input:
            print("There are a lot of great coaches that achieved a lot in their careers")
            for y in best_coaches:
                print(y)
     
        elif "national teams" in user_input:
            print("I know some national teams")
            for i in national_teams:
                print(i)
        elif "who is your favorite team" in user_input:
            print("I don't have favorites, but I admire every team!")
        elif any(team.lower() in user_input for team in national_teams):
            for team, info in national_teams.items():
                if team.lower() in user_input:
                    print(f"{team}  their stadium is {info[0]}, the coach is {info[1]}, they have won {info[2]} world cups, and their all time best player is  {info[3]}" )
        elif "goat" in user_input:
            print("For me, the GOAT is Ronaldo!")

        elif "do you know" in user_input:
            print(random.choice(happy_responses))

        elif "injury" in user_input or "he is going to be out" in user_input:
            print(random.choice(angry_responses))

        elif "champions league" in user_input:
            print(competitions[0])

        elif "europa league" in user_input:
            print(competitions[1])

        elif "conference league" in user_input:
            print(competitions[2])
        elif "Ludogorets" in user_input:
            print("Kak moje da si fen na tupite krenvirshi")

        else:
            print(random.choice(unknown_answers))



if __name__ == "__main__":
    football_chatbot()