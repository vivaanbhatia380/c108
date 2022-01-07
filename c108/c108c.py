import random
import plotly.figure_factory as ff

diceresult=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    

fig=ff.create_distplot([diceresult],['diceresult'],show_hist=False)
fig.show()