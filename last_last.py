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
important_rules = [
    "The game is played with two teams of 11 players each.",
    "The objective is to score more goals than the opponent within 90 minutes.",
    "The ball must completely cross the goal line between the goalposts and under the crossbar to count as a goal.",
    "Offside rule: a player is offside if they are nearer to the opponent's goal line than both the ball and the second-last defender when receiving a pass.",
    "No use of hands by outfield players except the goalkeeper within their penalty area.",
    "A foul is awarded when a player commits an unfair act like tripping, pushing, or handball.",
    "Free kicks and penalty kicks are awarded depending on the location and severity of fouls.",
    "The referee enforces the rules and can issue yellow and red cards for misconduct.",
    "The match is divided into two 45-minute halves with added stoppage time.",
    "If the game is tied in knockout matches, extra time and possibly penalty shootouts determine the winner."
]



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
    "Bayern vs BVB derby",
    "Levski vs CSKA derby",
    "Barca vs Real Madrid derby",
    "Arsenal vs Tottenham derby",
    "Liverpool vs Everton derby",
    "Chelsea vs Tottenham derby",
    "Arsenal vs Chelsea derby",
    "AEK vs PAOK derby",
    "Manchester City vs Manchester United derby",
    "AC Milan vs Inter Milan derby",
    "Barcelona vs Real Madrid derby",
    "Liverpool vs Manchester United derby",
    "Bayern Munich vs Borussia Dortmund derby",
    "Sevilla vs Real Betis derby",
    "Liverpool vs Everton derby",
    "Celtic vs Rangers derby",
    "AS Roma vs Lazio derby",
    "Arsenal vs Tottenham Hotspur derby",
    "Real Madrid vs Atlético Madrid derby",
    "Benfica vs Sporting CP derby"
]

best_coaches = [
    "Jose Mourinho coach",
    "Pep Guardiola coach",
    "Alex Ferguson coach",
    "Urgen Klop coach",
    "Hansi Flick coach",
    "Joahim Low coach",
    "Lionel Scaloni coach",
    "Rodrigo de Zerby coach",
    "Johan Cruyf coach",
    "Carlo Ancelloty coach",
    "Rafa Benitez coach",
    "Muri Stoilov coach",
    "Unai Emery coach",
    "Zinedine Zidane coach",
    "Antonio Conte coach",
    "Marcelo Bielsa coach",
    "Didier Deschamps coach",
    "Diego Simeone coach",
    "Luis Enrique coach",
    "Thomas Tuchel coach",
    "Frank Rijkaard coach",
    "Roberto Mancini coach",
    "Arsène Wenger coach",
    "Mauricio Pochettino coach",
    "Ottmar Hitzfeld coach",
    "Vicente del Bosque coach",
    "Louis van Gaal coach",
    "Erik ten Hag coach",
    "Luciano Spalletti coach",
    "Rudi Garcia coach",
    "Julian Nagelsmann coach",
    "Brendan Rodgers coach",
    "Graham Potter coach",
    "Xabi Alonso coach",
    "Fernando Santos coach",
    "Manuel Pellegrini coach",
    "Jesse Marsch coach",
    "Patrick Vieira coach",
    "Phil Neville coach",
    "Gerardo Martino coach",
    "Leonardo Jardim coach",
    "Ralph Hasenhüttl coach",
    "Slaven Bilić coach",
    "André Villas-Boas coach",
    "Cesare Prandelli coach",
    "Clarence Seedorf coach",
    "Marc Wilmots coach",
    "Hervé Renard coach"
]


Star_players = {
    "Ronaldo player": [927, 240, 5, 4, "Portugal"],
    "Messi player": [850, 381, 8, 6, "Argentina"],
    "Pele player": [1283, 231, 3, 0, "Brazil"],
    "Fernando Torres player": [302, 84, 0, 0, "Spain"],
    "Gerd Müller player": [735, 200, 2, 4, "Germany"],
    "Luis Figo player": [200, 180, 1, 0, "Portugal"],
    "Johan Cruyff player": [400, 300, 3, 0, "Netherlands"],
    "Marco van Basten player": [277, 120, 3, 1, "Netherlands"],
    "Raúl González player": [323, 150, 0, 0, "Spain"],
    "Eusébio player": [473, 200, 0, 1, "Portugal"],
    "Frank Lampard player": [210, 180, 0, 0, "England"],
    "Steven Gerrard player": [186, 150, 0, 0, "England"],
    "Clarence Seedorf player": [120, 130, 0, 0, "Netherlands"],
    "Kaká player": [170, 110, 1, 0, "Brazil"],
    "Dennis Bergkamp player": [120, 150, 0, 0, "Netherlands"],
    "Roberto Carlos player": [130, 110, 0, 0, "Brazil"],
    "Sergio Ramos player": [120, 70, 0, 0, "Spain"],
    "Thiago Silva player": [50, 30, 0, 0, "Brazil"],
    "David Beckham player": [130, 150, 0, 0, "England"],
    "Alessandro Del Piero player": [290, 120, 0, 0, "Italy"],
    "Zlatan Ibrahimović player": [570, 180, 0, 0, "Sweden"],
    "Luis Suárez player": [512, 225, 0, 0, "Uruguay"],
    "Wayne Rooney player": [366, 145, 0, 0, "England"],
    "Raheem Sterling player": [150, 90, 0, 0, "England"],
    "Sergio Agüero player": [380, 110, 0, 0, "Argentina"],
    "Yaya Touré player": [80, 100, 0, 0, "Ivory Coast"],
    "Paul Pogba player": [90, 95, 0, 0, "France"],
    "Cesc Fàbregas player": [100, 130, 0, 0, "Spain"],
    "Mesut Özil player": [85, 170, 0, 0, "Germany"],
    "Angel Di María player": [110, 150, 0, 0, "Argentina"],
    "Carlos Tévez player": [210, 70, 0, 0, "Argentina"],
    "Roberto Mancini player": [150, 90, 0, 0, "Italy"],
    "Gianfranco Zola player": [160, 110, 0, 0, "Italy"],
    "Andriy Shevchenko player": [175, 90, 1, 1, "Ukraine"],
    "Edinson Cavani player": [250, 70, 0, 0, "Uruguay"],
    "Fernando Redondo player": [40, 60, 0, 0, "Argentina"],
    "Zinedine Zidane player": [125, 100, 1, 1, "France"],
    "Ronaldinho player": [280, 165, 1, 1, "Brazil"],
    "Diego Maradona player": [312, 152, 0, 1, "Argentina"],
    "Cristiano Ronaldo player": [890, 250, 5, 0, "Portugal"],
    "Thierry Henry player": [411, 160, 0, 1, "France"],
    "Kylian Mbappé player": [280, 120, 0, 1, "France"],
    "Erling Haaland player": [200, 45, 0, 0, "Norway"],
    "Neymar player": [450, 260, 0, 0, "Brazil"],
    "Robert Lewandowski player": [640, 170, 0, 0, "Poland"],
    "Karim Benzema player": [435, 155, 1, 0, "France"],
    "Luka Modrić player": [130, 130, 1, 0, "Croatia"],
    "Mohamed Salah player": [300, 150, 0, 0, "Egypt"],
    "Sadio Mané player": [250, 120, 0, 0, "Senegal"],
    "Xavi Hernández player": [100, 200, 0, 1, "Spain"],
    "Andrés Iniesta player": [110, 190, 0, 1, "Spain"],
    "Gianluigi Buffon player": [0, 0, 0, 1, "Italy"],
    "Andrea Pirlo player": [80, 120, 0, 1, "Italy"],
    "Paolo Maldini player": [40, 35, 0, 0, "Italy"],
    "Franz Beckenbauer player": [75, 60, 2, 1, "Germany"],
    "Miroslav Klose player": [280, 90, 0, 1, "Germany"],
    "Thomas Müller player": [250, 190, 0, 1, "Germany"],
    "David Villa player": [390, 90, 0, 1, "Spain"],
    "Antoine Griezmann player": [260, 160, 0, 1, "France"],
    "Harry Kane player": [350, 120, 0, 0, "England"],
    "George Weah player": [200, 90, 1, 0, "Liberia"],
    "Didier Drogba player": [300, 120, 0, 0, "Ivory Coast"],
    "Rivaldo player": [336, 120, 1, 1, "Brazil"],
    "Roberto Baggio player": [291, 100, 1, 0, "Italy"],
    "Gabriel Batistuta player": [356, 100, 0, 0, "Argentina"],
    "Michael Owen player": [222, 50, 0, 0, "England"],
    "Hristo Stoichkov player": [309, 120, 1, 1, "Bulgaria"],
    "Davor Šuker player": [230, 80, 0, 1, "Croatia"],
    "Rui Costa player": [130, 150, 0, 0, "Portugal"],
    "Alan Shearer player": [409, 64, 0, 0, "England"],
    "Emmanuel Adebayor player": [200, 50, 0, 0, "Togo"],
    "Andres Guardado player": [80, 110, 0, 0, "Mexico"],
    "Park Ji-sung player": [90, 80, 0, 0, "South Korea"],
    "Javier Zanetti player": [40, 60, 0, 0, "Argentina"],
    "Hernán Crespo player": [273, 50, 0, 0, "Argentina"],
    "Diego Forlán player": [248, 80, 0, 1, "Uruguay"],
    "Freddie Ljungberg player": [130, 70, 0, 0, "Sweden"],
    "Arjen Robben player": [250, 120, 0, 0, "Netherlands"],
    "Franck Ribéry player": [240, 140, 0, 1, "France"],
    "Claude Makélélé player": [20, 40, 0, 0, "France"],
    "Nemanja Vidić player": [30, 20, 0, 0, "Serbia"],
    "Patrice Evra player": [15, 35, 0, 0, "France"],
    "Carlos Valderrama player": [50, 180, 0, 0, "Colombia"],
    "Jay-Jay Okocha player": [75, 100, 0, 0, "Nigeria"],
    "Hakan Şükür player": [250, 60, 0, 0, "Turkey"],
    "Samuel Eto'o player": [370, 90, 0, 1, "Cameroon"],
    "Dani Alves player": [60, 120, 0, 1, "Brazil"],
    "Keylor Navas player": [0, 0, 0, 1, "Costa Rica"],
    "Pavel Nedvěd player": [160, 100, 1, 0, "Czech Republic"],
    "Jan Oblak player": [0, 0, 0, 0, "Slovenia"],
    "Christian Pulisic player": [75, 60, 0, 0, "USA"],
    "João Félix player": [90, 40, 0, 0, "Portugal"],
    "Ángel Correa player": [100, 45, 0, 0, "Argentina"],
    "Hakim Ziyech player": [80, 95, 0, 0, "Morocco"],
    "Martin Ødegaard player": [60, 90, 0, 0, "Norway"],
    "Bukayo Saka player": [65, 55, 0, 0, "England"],
    "Pedri player": [25, 45, 0, 0, "Spain"],
    "Gavi player": [20, 30, 0, 0, "Spain"],
    "Joško Gvardiol player": [10, 15, 0, 0, "Croatia"],
    "Jude Bellingham player": [50, 40, 0, 0, "England"],
    "Phil Foden player": [70, 50, 0, 0, "England"],
    "Kai Havertz player": [65, 45, 0, 0, "Germany"],
    "Mason Mount player": [55, 35, 0, 0, "England"],
    "Declan Rice player": [30, 25, 0, 0, "England"],
    "Riyad Mahrez player": [120, 110, 0, 0, "Algeria"],
    "Ilkay Gündogan player": [100, 80, 0, 0, "Germany"],
    "Toni Kroos player": [90, 120, 0, 1, "Germany"],
    "Ivan Rakitić player": [85, 100, 0, 0, "Croatia"],
    "Álvaro Morata player": [180, 60, 0, 0, "Spain"],
    "Gerard Piqué player": [60, 40, 0, 1, "Spain"],
    "Jordi Alba player": [45, 70, 0, 1, "Spain"],
    "Philipp Lahm player": [35, 70, 0, 1, "Germany"],
    "Mats Hummels player": [30, 20, 0, 1, "Germany"],
    "Manuel Neuer player": [0, 3, 0, 1, "Germany"],
    "Petr Čech player": [0, 1, 0, 0, "Czech Republic"],
    "Thibaut Courtois player": [0, 1, 0, 0, "Belgium"],
    "Vinícius Júnior player": [75, 65, 0, 0, "Brazil"],
    "Rodrygo player": [60, 40, 0, 0, "Brazil"],
    "Raphinha player": [50, 35, 0, 0, "Brazil"],
    "Lautaro Martínez player": [110, 45, 0, 1, "Argentina"],
    "Paulo Dybala player": [120, 60, 0, 1, "Argentina"],
    "Richarlison player": [75, 40, 0, 1, "Brazil"],
    "Lucas Paquetá player": [40, 60, 0, 0, "Brazil"],
    "Nicolò Barella player": [45, 55, 0, 0, "Italy"],
    "Federico Chiesa player": [60, 40, 0, 1, "Italy"],
    "Serge Gnabry player": [100, 60, 0, 0, "Germany"],
    "Leroy Sané player": [95, 70, 0, 0, "Germany"],
    "Kingsley Coman player": [85, 65, 0, 1, "France"],
    "Adrien Rabiot player": [45, 50, 0, 1, "France"],
    "Aurélien Tchouaméni player": [15, 25, 0, 0, "France"],
    "Eduardo Camavinga player": [10, 20, 0, 1, "France"],
    "Matteo Guendouzi player": [25, 30, 0, 0, "France"],
    "João Cancelo player": [35, 50, 0, 0, "Portugal"],
    "Rúben Dias player": [20, 20, 0, 0, "Portugal"],
    "Diogo Jota player": [80, 40, 0, 0, "Portugal"],
    "Bruno Fernandes player": [115, 100, 0, 0, "Portugal"],
    "Bernardo Silva player": [90, 110, 0, 1, "Portugal"],
    "Dominik Szoboszlai player": [40, 50, 0, 0, "Hungary"],
    "Christopher Nkunku player": [70, 45, 0, 0, "France"],
    "Takefusa Kubo player": [35, 40, 0, 0, "Japan"],
    "Heung-min Son player": [190, 85, 0, 0, "South Korea"],
    "Wojciech Szczęsny player": [0, 0, 0, 0, "Poland"],
    "Granit Xhaka player": [45, 50, 0, 0, "Switzerland"],
    "James Rodríguez player": [110, 95, 0, 0, "Colombia"],
    "Radamel Falcao player": [250, 60, 0, 0, "Colombia"],
    "Arturo Vidal player": [100, 80, 0, 0, "Chile"],
    "Alexis Sánchez player": [195, 90, 0, 0, "Chile"],
    "Marcelo player": [45, 85, 0, 1, "Brazil"],
    "Keylor Navas player": [0, 0, 0, 0, "Costa Rica"],
    "Clint Dempsey player": [150, 70, 0, 0, "USA"],
    "Landon Donovan player": [160, 90, 0, 0, "USA"],
    "Héctor Herrera player": [40, 60, 0, 0, "Mexico"],
    "Javier Hernández player": [210, 40, 0, 0, "Mexico"],
    "André-Pierre Gignac player": [250, 55, 0, 0, "France"],
    "João Félix player": [65, 35, 0, 0, "Portugal"],
    "Frenkie de Jong player": [30, 45, 0, 0, "Netherlands"],
    "Memphis Depay player": [130, 80, 0, 0, "Netherlands"],
    "Dusan Vlahović player": [85, 25, 0, 0, "Serbia"],
    "Sergej Milinković-Savić player": [75, 50, 0, 0, "Serbia"],
    "Aleksandar Mitrović player": [230, 30, 0, 0, "Serbia"],
    "Achraf Hakimi player": [40, 60, 0, 0, "Morocco"],
    "Yassine Bounou player": [0, 0, 0, 0, "Morocco"],
    "Sofyan Amrabat player": [10, 30, 0, 0, "Morocco"]
}



unknown_answers = ["Haven't heard about that", "I don't think I understand you", "I don't know what you are talking about"]
happy_responses = ["That's interesting!", "I didn't know that!", "Tell me more!", "Football is amazing!", "Wow, fascinating!"]
angry_responses = ["That doesn't seem good", "That is awful"]

competitions = [
    "Champions League is the best tournament in Europe!",
    "Europa League is the second-best tournament in Europe!",
    "UEFA Conference League is the weakest European tournament, but still interesting!",
    "FIFA World Cup is the biggest international football tournament, held every four years!",
    "UEFA European Championship (Euro) is the premier European national team competition!",
    "Copa America is the South American championship for national teams!",
    "Africa Cup of Nations (AFCON) is the main continental tournament for African national teams!",
    "CONCACAF Gold Cup is the championship for North and Central America and the Caribbean!",
    "AFC Asian Cup is the top continental tournament for Asian national teams!",
    "Oceania Nations Cup is the primary competition for national teams in Oceania!",
    "FIFA Confederations Cup was a tournament between continental champions, now discontinued!",
    "Olympic Football Tournament is held every four years featuring mostly U-23 national teams!",
    "FIFA U-20 World Cup is the top international competition for under-20 national teams!",
    "FIFA U-17 World Cup is the main youth competition for under-17 national teams!",
    "UEFA Nations League is a newer competition for European national teams to increase competitive matches!",
    "FIFA Club World Cup features champion clubs from each continent competing globally!"
]



teams = {
    "Barcelona team": ["La Liga", "Camp Nou", "Hansi Flick", 5, "Lewandowski"],
    "Real Madrid team": ["La Liga", "Santiago Bernabéu", "Carlo Ancelotti", 15, "Vinicius Jr."],
    "Manchester United team": ["Premier League", "Old Trafford", "Ruben Amorim", 2, "Bruno Fernandes"],
    "Manchester City team": ["Premier League", "Etihad Stadium", "Pep Guardiola", 9, "Erling Haaland"],
    "Liverpool team": ["Premier League", "Anfield", "Arne Slot", 6, "Mohamed Salah"],
    "Chelsea team": ["Premier League", "Stamford Bridge", "Enzo Maresca", 6, "Cole Palmer"],
    "Arsenal team": ["Premier League", "Emirates Stadium", "Mikel Arteta", 13, "Bukayo Saka"],
    "Tottenham Hotspur team": ["Premier League", "Tottenham Hotspur Stadium", "Ange Postecoglou", 2, "Heung-Min Son"],
    "Newcastle United team": ["Premier League", "St James' Park", "Eddie Howe", 4, "Alexander Isak"],
    "Bayern Munich team": ["Bundesliga", "Allianz Arena", "Vincent Kompany", 32, "Jamal Musiala"],
    "Borussia Dortmund team": ["Bundesliga", "Signal Iduna Park", "Edin Terzić", 8, "Julian Brandt"],
    "RB Leipzig team": ["Bundesliga", "Red Bull Arena", "Marco Rose", 0, "Dani Olmo"],
    "Bayer Leverkusen team": ["Bundesliga", "BayArena", "Xabi Alonso", 1, "Florian Wirtz"],
    "PSG team": ["Ligue 1", "Parc des Princes", "Luis Enrique", 11, "Kylian Mbappé"],
    "Marseille team": ["Ligue 1", "Stade Vélodrome", "Jean-Louis Gasset", 9, "Pierre-Emerick Aubameyang"],
    "Lyon team": ["Ligue 1", "Groupama Stadium", "Pierre Sage", 7, "Alexandre Lacazette"],
    "Monaco team": ["Ligue 1", "Stade Louis II", "Adi Hütter", 8, "Wissam Ben Yedder"],
    "Inter Milan team": ["Serie A", "San Siro", "Simone Inzaghi", 20, "Lautaro Martínez"],
    "AC Milan team": ["Serie A", "San Siro", "Stefano Pioli", 19, "Rafael Leão"],
    "Juventus team": ["Serie A", "Allianz Stadium", "Thiago Motta", 36, "Dusan Vlahovic"],
    "Napoli team": ["Serie A", "Diego Armando Maradona Stadium", "Antonio Conte", 3, "Victor Osimhen"],
    "Atletico Madrid team": ["La Liga", "Metropolitano", "Diego Simeone", 11, "Antoine Griezmann"],
    "Sevilla team": ["La Liga", "Ramón Sánchez Pizjuán", "Quique Sánchez Flores", 1, "Youssef En-Nesyri"],
    "Real Sociedad team": ["La Liga", "Reale Arena", "Imanol Alguacil", 2, "Mikel Oyarzabal"],
    "Benfica team": ["Primeira Liga", "Estádio da Luz", "Roger Schmidt", 38, "Ángel Di María"],
    "Porto team": ["Primeira Liga", "Estádio do Dragão", "Sérgio Conceição", 30, "Diogo Costa"],
    "Ajax team": ["Eredivisie", "Johan Cruyff Arena", "Mauricio Pochettino", 36, "Steven Berghuis"],
    "PSV Eindhoven team ": ["Eredivisie", "Philips Stadion", "Ruud van Nistelrooy", 24, "Joey Veerman"],
    "Feyenoord team": ["Eredivisie", "De Kuip", "Arne Slot", 16, "Bryan Linssen"],
    "Galatasaray team": ["Süper Lig", "Nef Stadium", "Okan Buruk", 23, "Kerem Aktürkoğlu"],
    "Fenerbahçe team": ["Süper Lig", "Şükrü Saracoğlu Stadium", "İsmail Kartal", 29, "Enner Valencia"],
    "Beşiktaş team": ["Süper Lig", "Vodafone Park", "Şenol Güneş", 17, "Rachid Ghezzal"],
    "Celtic team": ["Scottish Premiership", "Celtic Park", " Brendan Rodgers", 53, "Kyogo Furuhashi"],
    "Rangers team ": ["Scottish Premiership", "Ibrox Stadium", "Michael Beale", 56, "James Tavernier"],
    "Olympiacos team ": ["Super League Greece", "Karaiskakis Stadium", "Michele Farris", 47, "Youssef El-Arabi"],
    "Panathinaikos team": ["Super League Greece", "Apostolos Nikolaidis Stadium", "Ivan Jovanović", 20, "Dimitris Kourbelis"],
    "Shakhtar Donetsk team": ["Ukrainian Premier League", "NSC Olimpiyskiy (temporary)", "Igor Jovićević", 13, "Marcos Antônio"],
    "Dynamo Kyiv team ": ["Ukrainian Premier League", "NSC Olimpiyskiy", "Mircea Lucescu", 16, "Viktor Tsyhankov"],
    "Zenit St Petersburg team": ["Russian Premier League", "Krestovsky Stadium", "Sergey Semak", 9, "Sardar Azmoun"],
    "CSKA Moscow team": ["Russian Premier League", "VEB Arena", "Viktor Goncharenko", 13, "Fedor Chalov"],
    "Spartak Moscow team": ["Russian Premier League", "Otkritie Arena", "Oleg Kononov", 23, "Jordan Larsson"],
    "Lazio team": ["Serie A", "Stadio Olimpico", "Maurizio Sarri", 2, "Ciro Immobile"],
    "Roma team": ["Serie A", "Stadio Olimpico", "Claudio Raniery", 3, "Paulo Dybala"],
    "Sassuolo team": ["Serie A", "Mapei Stadium", "Paolo Nicolato", 0, "Domenico Berardi"],
    "Bologna team ": ["Serie A", "Stadio Renato Dall'Ara", "Vincenco Italiano", 0, "Riccardo Orsolini"],
    "Torino team ": ["Serie A", "Stadio Olimpico Grande Torino", "Ivan Jurić", 7, "Sasa Lukic"],
    "Real Betis team ": ["La Liga", "Benito Villamarín", "Manuel Pellegrini", 1, "Nabil Fekir"],
    "Villarreal team": ["La Liga", "Estadio de la Cerámica", "Quique Setién", 0, "Arnaut Danjuma"],
    "Athletic Bilbao team": ["La Liga", "San Mamés", "Ernesto Valverde", 8, "Iker Muniain"],
    "Espanyol team": ["La Liga", "RCDE Stadium", "Luis García", 0, "Raúl de Tomás"],
    "Levante team": ["La Liga", "Ciutat de València", "Javi Calleja", 0, "José Luis Morales"],
    "Real Valladolid team": ["La Liga", "José Zorrilla Stadium", "Pacheta", 0, "Óscar Plano"],
    "Santos team": ["Brasileirão", "Vila Belmiro", "Osmar Loss", 8, "Marinho"],
    "Flamengo team ": ["Brasileirão", "Maracanã", "Vanderlei Luxemburgo", 8, "Gabriel Barbosa"],
    "Palmeiras team ": ["Brasileirão", "Allianz Parque", "Abel Ferreira", 12, "Raphael Veiga"],
    "Corinthians team": ["Brasileirão", "Neo Química Arena", "Vítor Pereira", 7, "Willian"],
    "São Paulo FC team": ["Brasileirão", "Morumbi", "Rogério Ceni", 6, "Jonathan Calleri"],
    "Boca Juniors team": ["Primera División Argentina", "La Bombonera", "Sebastián Battaglia", 35, "Darío Benedetto"],
    "River Plate team": ["Primera División Argentina", "Monumental", "Marcelo Gallardo", 38, "Julián Álvarez"],
    "Vasco da Gama team": ["Brasileirão", "São Januário", "Lisca", 4, "Andrey"],
    "Grêmio team": ["Brasileirão", "Arena do Grêmio", "Renato Portaluppi", 3, "Ferreira"],
    "Cruz Azul team": ["Liga MX", "Estadio Azteca", "Ricardo Ferretti", 9, "Orbelín Pineda"],
    "América team": ["Liga MX", "Estadio Azteca", "Fernando Ortiz", 14, "Henry Martín"],
    "Chivas Guadalajara team": ["Liga MX", "Estadio Akron", "Veljko Paunović", 12, "José Juan Macías"],
    "Tigres UANL team": ["Liga MX", "Estadio Universitario", "Miguel Herrera", 8, "André-Pierre Gignac"],
    "Monterrey team": ["Liga MX", "Estadio BBVA", "Víctor Manuel Vucetich", 5, "Rogelio Funes Mori"],
    "Al Ahly team": ["Egyptian Premier League", "Cairo International Stadium", "Juan Carlos Osorio", 43, "Mohamed Sherif"],
    "Zamalek team": ["Egyptian Premier League", "Cairo International Stadium", "Juan Carlos Osorio", 14, "Shikabala"],
    "Al Hilal team": ["Saudi Pro League", "King Fahd Stadium", "Rene Weiler", 19, "Salem Al-Dawsari"],
    "Al Nassr team": ["Saudi Pro League", "Mrsool Park", "Rudi Garcia", 10, "Talisca"],
    "Melbourne Victory team": ["A-League", "AAMI Park", "Tony Popovic", 4, "Jake Brimmer"],
    "Sydney FC team": ["A-League", "Allianz Stadium", "Steve Corica", 5, "Kosta Barbarouses"],
    "LA Galaxy team": ["MLS", "Dignity Health Sports Park", "Greg Vanney", 5, "Chicharito"],
    "Atlanta United team": ["MLS", "Mercedes-Benz Stadium", "Gonzalo Pineda", 1, "Miguel Almirón"],
    "Seattle Sounders team": ["MLS", "Lumen Field", "Brian Schmetzer", 2, "Raúl Ruidíaz"],
    
    "Ludogorets Razgrad team": ["First Professional Football League", "Ludogorets Arena", "Ante Šimundža", 12, "Claudiu Keșerü"],
    "CSKA Sofia team": ["First Professional Football League", "Balgarska Armia Stadium", "Stanimir Stoilov", 31, "Ali Sowe"],
    "Levski Sofia team": ["First Professional Football League", "Georgi Asparuhov Stadium", "Elin Topuzakov", 26, "Pieros Sotiriou"],
    "Cherno More Varna team": ["First Professional Football League", "Ticha Stadium", "Ilian Iliev", 4, "Ricardo Nunes"],
    "Arda Kardzhali team": ["First Professional Football League", "Arena Arda", "Aleksandar Tunchev", 0, "Iliyan Mitsanski"],
    "Botev Plovdiv team": ["First Professional Football League", "Hristo Botev Stadium", "Azrudin Valentić", 2, "Rafinha"],
    "Spartak Varna team": ["First Professional Football League", "Spartak Stadium", "Veselin Velikov", 0, "Kristiyan Dobrev"],
    "Beroe Stara Zagora team": ["First Professional Football League", "Beroe Stadium", "Petar Hubchev", 1, "Yuri Lavrinenko"],
    "Slavia Sofia team": ["First Professional Football League", "Slavia Stadium", "Nikolay Kostov", 7, "Marquinhos Pedroso"],
    "CSKA 1948 Sofia team": ["First Professional Football League", "Balgarska Armia Stadium (shared)", "Nikolay Kirov", 0, "Emil Stoyanov"],
    "Lokomotiv Plovdiv team": ["First Professional Football League", "Lokomotiv Stadium", "Nikolay Mitov", 3, "Dimitar Iliev"],
    "Hebar Pazardzhik team": ["First Professional Football League", "Georgi Benkovski Stadium", "Slaviša Božičić", 0, "Yordan Minev"],
    "Lokomotiv Sofia team": ["First Professional Football League", "Lokomotiv Stadium", "Vasil Petrov", 4, "Radoslav Kirilov"],
    "Septemvri Sofia team": ["First Professional Football League", "Septemvri Stadium", "Nikolay Mitov", 0, "Viktor Genev"],
    "Botev Vratsa team": ["First Professional Football League", "Hristo Botev Stadium (Vratsa)", "Petar Kolev", 0, "Marek Kuzma"],
    "Krumovgrad team": ["First Professional Football League", "Krumovgrad Stadium", "Stoycho Stoev", 0, "Dimitar Iliev"],

   
    "Dobrudzha Dobrich team": ["Second Professional Football League", "Dobrich Stadium", "Ivan Iliev", 0, "Georgi Kostadinov"],
    "Montana team": ["Second Professional Football League", "Ogosta Stadium", "Dimitar Dimitrov", 0, "Petar Vitanov"],
    "Pirin Blagoevgrad team": ["Second Professional Football League", "Hristo Botev Stadium (Blagoevgrad)", "Yancho Andreev", 1, "Plamen Krumov"],
    "Etar Veliko Tarnovo team": ["Second Professional Football League", "Ivaylo Stadium", "Nikolay Kirov", 2, "Andon Gushterov"],
    "Sozopol team": ["Second Professional Football League", "Sozopol Stadium", "Iliyan Iliev", 0, "Dimitar Georgiev"],
    "Minyor Pernik team": ["Second Professional Football League", "Minyor Stadium", "Nikolay Kirov", 0, "Kiril Denev"],
    "Maritsa Plovdiv team": ["Second Professional Football League", "Maritsa Stadium", "Dimitar Dimitrov", 0, "Ivan Chakarov"],
    "Yantra Gabrovo team": ["Second Professional Football League", "Hristo Botev Stadium (Gabrovo)", "Dimitar Iliev", 0, "Ivan Petkov"],
    "Strumska Slava Radomir team": ["Second Professional Football League", "Strumska Slava Stadium", "Zdravko Zdravkov", 0, "Martin Vasilev"],
    "Litex Lovech team": ["Second Professional Football League", "Lovech Stadium", "Emil Velev", 4, "Ivan Stoyanov"],
    "Minior Bobov dol team":["A okrujna " , "Shultz" , "Kaloqn " , 0, "Atanas"],
    "Nacional Sofia":["A okrujna " , "NSA estestven teren", "Stanislav Katrankov", 0, "Stoqn Stoqnov"]
}






national_teams = { 
    "Brazil national team": ["Maracanã", "Dorival Júnior", 5, "Pele"],
    "Argentina national team": ["Estadio Monumental", "Lionel Scaloni", 3, "Lionel Messi"],
    "France national team": ["Stade de France", "Didier Deschamps", 2, "Kylian Mbappé"],
    "Bulgaria national team": ["Vasil Levski", "Ilian Iliev", 0, "Stoichkov"],
    "Germany national team": ["Allianz Arena", "Julian Nagelsmann", 4, "Jamal Musiala"],
    "Spain national team": ["Santiago Bernabéu", "Luis de la Fuente", 1, "Pedri"],
    "England national team": ["Wembley Stadium", "Gareth Southgate", 1, "Harry Kane"],
    "Portugal national team": ["Estádio da Luz", "Roberto Martínez", 0, "Cristiano Ronaldo"],
    "Italy national team": ["Stadio Olimpico", "Luciano Spalletti", 4, "Federico Chiesa"],
    "Netherlands national team": ["Johan Cruyff Arena", "Ronald Koeman", 0, "Cody Gakpo"],
    "Uruguay national team": ["Estadio Centenario", "Marcelo Bielsa", 2, "Federico Valverde"],
    "Croatia national team": ["Stadion Maksimir", "Zlatko Dalić", 0, "Luka Modrić"],
    "Belgium national team": ["King Baudouin Stadium", "Domenico Tedesco", 0, "Kevin De Bruyne"],
    "Morocco national team": ["Prince Moulay Abdellah Stadium", "Walid Regragui", 0, "Achraf Hakimi"],
    "Mexico national team": ["Estadio Azteca", "Jaime Lozano", 0, "Hirving Lozano"],
    "USA national team": ["Mercedes-Benz Stadium", "Gregg Berhalter", 0, "Christian Pulisic"],
    "Japan national team": ["Saitama Stadium", "Hajime Moriyasu", 0, "Takefusa Kubo"],
    "South Korea national team": ["Seoul World Cup Stadium", "Jürgen Klinsmann", 0, "Son Heung-min"],
    "Australia national team": ["Stadium Australia", "Graham Arnold", 0, "Mathew Leckie"],
    "Switzerland national team": ["St. Jakob-Park", "Murat Yakin", 0, "Granit Xhaka"],
    "Poland national team": ["National Stadium Warsaw", "Michał Probierz", 0, "Robert Lewandowski"],
    "Serbia national team": ["Rajko Mitić Stadium", "Dragan Stojković", 0, "Dušan Vlahović"],
    "Colombia national team": ["Metropolitano Stadium", "Néstor Lorenzo", 0, "Luis Díaz"],
    "Chile national team": ["Estadio Nacional", "Ricardo Gareca", 0, "Alexis Sánchez"],
    "Turkey national team": ["Atatürk Olympic Stadium", "Vincenzo Montella", 0, "Hakan Çalhanoğlu"],
    "Norway national team": ["Ullevaal Stadion", "Ståle Solbakken", 0, "Erling Haaland"],
    "Sweden national team": ["Friends Arena", "Janne Andersson", 0, "Alexander Isak"],
    "Ukraine national team": ["NSC Olimpiyskiy", "Serhiy Rebrov", 0, "Mykhailo Mudryk"],
    "Czech Republic national team": ["Eden Arena", "Jaroslav Šilhavý", 0, "Patrik Schick"],
    "Senegal national team": ["Stade Léopold Sédar Senghor", "Aliou Cissé", 0, "Sadio Mané"]
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
    if "rules" in user_message:
        return jsonify({"response:" f"This are the most common rules in football {important_rules}"})
    if "teams" in user_message:
        return jsonify({"response:" f"I know a lot of teams {teams}"})
    if "national teams" in user_message:
            for team in national_teams:
               if team.lower() in user_message.lower():
                 info = national_teams[team]
                 return jsonify({
                    "response": f"{team} plays on {info[0]}, their manager  is {info[1]}, they have won {info[2]} world cups , their best player of all time is {info[3]}."
            })
 
    if  "manager" in user_message:
        return jsonify({"response": f"One of the best coaches is {random.choice(best_coaches)}."})
    if "coaches" in user_message:
     return jsonify({"response": f"I know a lot of coaches {best_coaches}."})
    if "coach" in user_message:
      for coach in best_coaches:
               if coach.lower() in user_message.lower():
                 info = best_coaches[coach]
                 return jsonify({
                    "response": f"{coach}."
            })
    if "player" in user_message:
        for player in Star_players:
               if player.lower() in user_message.lower():
                 info = Star_players[player]
                 return jsonify({
                    "response": f"{player} has {info[0]} goals and  {info[1]} assists,  {info[2]} ballon'ors  and  {info[3]} golden boots, he is from {info[4]} ."
            })
 

    if "competition" in  user_message:
        return jsonify({"response": f"One of the best competitions is {random.choice(competitions)}."})
    if "competition" in  user_message:
        return jsonify({"response": f"I know a lot of competitions {competitions}."})
    if "UCL" in user_message:
        return jsonify({"response": competitions[0]})
    if "UEL" in  user_message:
        return jsonify({"response": competitions[1]})
    if "UECL"  in user_message:
        return jsonify({"response": competitions[2]})
    if "World cup"  in user_message:
        return jsonify({"response": competitions[3]}) 
    

    if "happy" in user_message:
        return jsonify({"response": random.choice(happy_responses)})

    if "angry" in user_message:
        return jsonify({"response": random.choice(angry_responses)})

    return jsonify({"response": random.choice(unknown_answers)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)