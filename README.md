# UltimatumGame
 
2 different classes compose the networks

**Player**

**Ultimatum Game (UG)**

Player( id, PlayerRole)

Player has access to one of three different roles: Empathetic. Pragmatic, Independent.

This role has impact on the q and p strategy.

ultimatumGame( Nplayers, PlayerRole, ScaleFree=False)

Ultimatum Game has access to either ER or SF networks (attribute ScaleFree)

When playing the game:

game.runEpisode(iteration,offersDicInitial,offerDic,thresholdDicInitial,thresholdDic,stopsForGraphs, NaturalSelection=False, SocialPenalty=True)

allows for having Natural Selection has an update rule or not.

Same for Social Penalty "offersDicInitial,offerDic,thresholdDicInitial,thresholdDic" are bassically the dicionaries to store the information (offers p and q values) on a certain selection of rounds
