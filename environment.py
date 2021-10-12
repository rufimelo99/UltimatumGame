from game.playerRole import playerRole
from game.ultimatumGame import ultimatumGame
from game.player import Player
NPLAYERS = 8
NITERATIONS = 1

def main():
    game = ultimatumGame(NPLAYERS)
    
    #game.printGraph()
    
    #create all players
    for i in range(NPLAYERS):
        player = Player(i, list(game.graph.adj[i]))
        game.Players.append(player)

    for id in range(len(game.Players)):
        for neighbourId in range(len(game.Players)):
            if neighbourId in list(game.graph.adj[id]):
                game.Players[id].neighbours.append(game.Players[neighbourId])

    for i in range(NITERATIONS):
        for player in game.Players:
            #player.bargainDecision()
            for neighbour in player.neighbours:
                playerReward=player.makeOffer()
                rewardAcceptedOrNot = neighbour.bargainDecision(playerReward)
                player.qlearningIteration(rewardAcceptedOrNot, playerReward)
                neighbour.qlearningIteration(rewardAcceptedOrNot, 1-playerReward)
    for player in game.Players:
         print(player.qinit)

if __name__ == "__main__":
    main()