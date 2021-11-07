In the notebook there is 2 different classes compose the networks to replicate Sinatra's work. They are defined in the **Classes** section.
<ul>  
<li>Player</li>  
<li>Ultimatum Game (UG)</li>  
</ul># 


**Player**

`class Player(id, PlayerRole)`

Player has access to one of three different roles: Empathetic. Pragmatic, Independent. This role, as discussed in the paper, has impact on the q and p strategy.

**Ultimatum Game (UG)**

`class ultimatumGame( Nplayers, PlayerRole, ScaleFree=False)`

Ultimatum Game has access to either ER or SF networks (assigned by the argument ScaleFree)

---
When playing the game in the **Execution** section :

`game.runEpisode(iteration,offersDicInitial,offerDic,thresholdDicInitial,thresholdDic,stopsForGraphs, NaturalSelection=False, SocialPenalty=True)`

allows for having Natural Selection has an update rule or not. Same applies for Social Penalty. (assigned by the argument NaturalSelection and SocialPenalty, respectively)

`offersDicInitial,offerDic,thresholdDicInitial,thresholdDic` arguments are basically the dictionaries to store the information (offers p and q values) on a certain selection of rounds. These are used for plotting the graphs later.

On the **Future Works: Different Types of Players** section, there is defined a new Ultimatum Game class that allows for the presence of players with different player Roles in the network. This new class also affects how the update rules work in this context.
