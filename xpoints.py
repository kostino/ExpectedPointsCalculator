import pandas as pd
import numpy as np
from scipy.stats import poisson

max_g = 20


def xpoints(matchlist):
    xpoints = {team:0 for team in matchlist['Home'].unique()}
    for index,match in matchlist.iterrows():
        homeG = float(match['xGHome'])
        awayG = float(match['xGAway'])
        probs = np.matmul(np.array([poisson.pmf(i,homeG) for i in range(max_g)]).reshape(max_g,1),np.array([poisson.pmf(i,awayG) for i in range(max_g)]).reshape(1,max_g))
        homeWP = np.tril(probs).sum()-np.trace(probs)
        awayWP = np.triu(probs).sum()-np.trace(probs)
        drawP = np.trace(probs)
        homeP = homeWP*3+drawP*1
        awayP = awayWP*3+drawP*1
        xpoints[match['Home']]+=homeP
        xpoints[match['Away']]+=awayP
    return xpoints
