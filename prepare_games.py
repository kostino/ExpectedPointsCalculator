import pandas as pd

def prepare_games(matchlist):
    matchlist = matchlist[['Home','xGHome','xGAway','Away']]
    matchlist=matchlist[matchlist['xGHome'].notna()]
    return matchlist

