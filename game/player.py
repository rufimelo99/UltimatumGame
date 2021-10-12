import random
import numpy as np
import numpy.random as rnd
import math

class Player:
    def __init__(self, id, Neigbours) -> None:
        self.id=id
        self.bargainValues=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        self.mapValuesIndex = {0: 0, 0.1: 1, 0.2: 2, 0.3: 3, 0.4:4, 0.5: 5, 0.6: 6, 0.7: 7, 0.8: 8, 0.9: 9, 1: 1}
        self.mapIndexValues = {0: 0, 1: 0.1, 2: 0.2, 3: 0.3, 4:0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 1: 1}
        self.neighbours=[]
        self.AvgComulativePayoff=0
        self.qinitProposer = np.zeros((len(self.bargainValues), 2))
        self.qinitCorrespondent = np.zeros((len(self.bargainValues), 2))
        
        """
                #payoff per bargain value-> either accept or not
        Qinit = [0  0
                0   0
                0   0
                .
                .
                .        ]
        """        

    def qlearningIterationProposer(self, bargainAccepted, bargainIndexOnTable):
        #bargainAccepted: 0 or 1 which also works as position in the qinit
        #reward also works as position in qinit
        
        #need conversion->multiples of 10 that gives position. otherwise, a dic would be recommended
        
        action = bargainAccepted

        self.qinitProposer[bargainIndexOnTable][action] += 0.3*(bargainIndexOnTable*bargainAccepted + 0.9 * np.max(self.qinitProposer[bargainIndexOnTable]) - self.qinitProposer[bargainIndexOnTable][action])

    def qlearningIterationCorrespondent(self, bargainAccepted, bargainIndexOnTable):
        #bargainAccepted: 0 or 1 which also works as position in the qinit
        #reward also works as position in qinit
        
        #need conversion->multiples of 10 that gives position. otherwise, a dic would be recommended
        
        action = bargainAccepted

        self.qinitCorrespondent[bargainIndexOnTable][action] += 0.3*(bargainIndexOnTable*bargainAccepted + 0.9 * np.max(self.qinitCorrespondent[bargainIndexOnTable]) - self.qinitCorrespondent[bargainIndexOnTable][action])

    def makeOffer(self):
        #returns index of bargain proposal

        #yes or no
        #print(self.qinit)
        #print(self.qinit[:,1])
        #print(np.where(self.qinit[:,1] == np.max(self.qinit[:,1]))[0])
        
        bargainValueIndex = rnd.choice(np.where(self.qinitProposer[:,1] == np.max(self.qinitProposer[:,1]))[0])     #offer what is best for himself according to its policy
        #print(aux)
        #print(self.bargainValues[aux])
        
        print("\nPlayer " + str(self.id) +" made offer of: "+str(self.bargainValues[bargainValueIndex]))
        return bargainValueIndex

    def bargainDecision(self, bargainValueIndex):
        print("Proposer reward in question: "+str(self.bargainValues[bargainValueIndex]))
        print("Correspondent reward in question: "+str(self.bargainValues[-(bargainValueIndex+1)]))
        
        correspondentValueIndex = self.bargainValues.index(self.bargainValues[-(bargainValueIndex+1)])
        print("Correspondent index: "+str(correspondentValueIndex))

        #yes or no
        #model if there was more option other than accepting and rejecting
        #print(self.qinit[reward])
        aux = rnd.choice(2)     #len of options        
        aux1 = rnd.choice(np.where(self.qinitCorrespondent[correspondentValueIndex] == np.max(self.qinitCorrespondent[correspondentValueIndex]))[0])    #most profitable choice
        
        #print("aux: "+str(aux))
        #print("aux1: "+str(aux1))


        index = rnd.choice([aux, aux1], p = [0.15, 0.85])

        #TODO
        #? is the index correct with 0/1
        print("\nPlayer " + str(self.id) +" made the decision of "+ str(index)+" (accepting/rejecting) on the offer of reciving: "+str(self.bargainValues[-(bargainValueIndex+1)]))
        
        return index, correspondentValueIndex

        

