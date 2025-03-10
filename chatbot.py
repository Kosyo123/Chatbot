import random
def football_chatbot():
    print("⚽ Welcome to the Football Chatbot! ⚽")
    print("Ask me about teams, players, or football in general. Type 'exit' to end the chat.")

    teams = {
        "Barcelona": ["La Liga", "Camp Nou", "Xavi", "Lewandowski"],
        "Real Madrid": ["La Liga", "Santiago Bernabéu", "Ancelotti", "Vinicius Jr."],
        "Manchester United": ["Premier League", "Old Trafford", "Ten Hag", "Rashford"],
        "Liverpool": ["Premier League", "Anfield", "Klopp", "Salah"],
        "Bayern Munich": ["Bundesliga", "Allianz Arena", "Tuchel", "Kane"],
    }

    responses = [
        "That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"
    ]

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Goodbye! ⚽")
            break

        elif "team" in user_input:
            print("I know about these teams:", ", ".join(teams.keys()))

        elif any(team.lower() in user_input for team in teams):
            for team, info in teams.items():
                if team.lower() in user_input:
                    print(f"{team} plays in the {info[0]}, their stadium is {info[1]}, the coach is {info[2]}, and their star player is {info[3]}.")

        elif "player" in user_input:
            print("I know these famous players: Lewandowski, Vinicius Jr., Rashford, Salah, Kane")

        elif "who is your favorite team" in user_input:
            print("I don't have favorites, but I admire every team!")

        else:
            print(random.choice(responses))

if __name__ == "__main__":
    football_chatbot()