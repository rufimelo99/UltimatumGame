from game.playerRole import playerRole
from game.ultimatumGame import ultimatumGame
from game.player import Player
NPLAYERS = 16
NITERATIONS = 500

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
                playerBargainIndex=player.makeOffer()
                rewardAcceptedOrNot, neighbourBargainIndex = neighbour.bargainDecision(playerBargainIndex)
                player.qlearningIteration(rewardAcceptedOrNot, playerBargainIndex)
                neighbour.qlearningIteration(rewardAcceptedOrNot, neighbourBargainIndex)
    for player in game.Players:
         print(player.qinit)

if __name__ == "__main__":
    main()