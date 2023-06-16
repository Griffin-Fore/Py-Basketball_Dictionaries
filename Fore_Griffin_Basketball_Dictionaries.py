class Player:
    # ... (class definition and large list of players here)
    # Write your for loop here to populate the new_team variable with Player objects.
    new_team = []
    # step 5 - apply the init to the item
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.possition = player["position"]
        self.team = player["team"]

    @classmethod
    # step 2 - take in the players list, name it players_list
    def store_player(cls, players_list):
        # step 3 for each item in th list
        for player in players_list:
            # step 4 - pass to the init
            new_player = cls(player)
            #
            cls.new_team.append(new_player)
            print(player)


players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
    },
    {
	"name": "Kyrie Irving", 
	"age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
    },
    {
	"name": "Damian Lillard", 
	"age":33, "position": "Point Guard", 
	"team": "Portland Trailblazers"
    },
    {
	"name": "Joel Embiid", 
	"age":32, "position": "Power Foward", 
	"team": "Philidelphia 76ers"
    },
    {
	"name": "", 
	"age":16, 
	"position": "P", 
	"team": "en"
    }
]



# Create your Player instances here!
# player_jason = ???
player_kevin  = Player(players[0])
player_jason = Player(players[1])
player_kyrie = Player(players[2])

print(player_kevin.name)
# step 1 - take in a list
Player.store_player(players)