import random
def football_chatbot():
    print("⚽ Welcome to the Football Chatbot! ⚽")
    print("Ask me about teams, players, or football in general. Type 'exit' to end the chat.")

    teams = {
        "Barcelona": ["La Liga", "Camp Nou", "Hamsi Flick", 5,"Lewandowski"],
        "Real Madrid": ["La Liga", "Santiago Bernabéu", " Carlo Ancelotti",15, "Vinicius Jr."],
        "Manchester United": ["Premier League", "Old Trafford", "Ruben Amorim",2, "Bruno Fernandes"],
        "Liverpool": ["Premier League", "Anfield", "Arme Slot",6, "Salah"],
        "Bayern Munich": ["Bundesliga", "Allianz Arena", "Vincent Company",6, "Kane"],
        "Atletico madrid": ["La liga", "Metropolitano", "Diego Simeone",0, "Julian Alvarez"],
        "Bayer Leverkusen" : ["Bundesliga", "Bay arena", "Xabi Alonso",0, "Florian Wirtz"],
        "Milan" : ["Seria A", " San Siro", "Sergio Conceisao", 7,"Rafael Leao"],
    }
  
    happy_responses = [
        "That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"
    ]
    competitions = ["Champions leauge is the best tourament that has 36 teams to play every year!", "Europa leauge is the second best tournament in europe !", "Uefa Conference leauge is the weakest european tournament but that does not mean that is not interesting"]
    angry_responses = ["That dont seem good", "That is awful"]


    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit' or user_input == "bye":
            print("Goodbye! ⚽")
            break

        elif "team" in user_input:
            print("I know about these teams:", ", ".join(teams.keys()))

        elif any(team.lower() in user_input for team in teams):
            for team, info in teams.items():
                if team.lower() in user_input:
                    print(f"{team} plays in the {info[0]}, their stadium is {info[1]}, the coach is {info[2]},They  have won {info[3]} Champions leauges and their star player is {info[4]}.")

        elif "players" in user_input:
            print("I know these famous players: Lewandowski, Vinicius Jr., Rashford, Salah, Kane")

        elif "who is your favorite team" in user_input:
            print("I don't have favorites, but I admire every team!")
        elif "goat" in user_input:
            print("For me the goat is Ronaldo")
        elif "do you know" in user_input:
            print(random.choice(happy_responses))
        
        elif "injury" in user_input:
            print(random.choice(angry_responses))
        elif "he is going to be out" in user_input:
            print(random.choice(angry_responses))
        elif "champions league" in user_input:
            print(competitions[0])
        elif "europa leauge" in user_input:
            print(competitions[1])
        elif "conference league" in user_input:
            print(competitions[2])
        else:
            print(random.choice(happy_responses))

if __name__ == "__main__":
    football_chatbot()