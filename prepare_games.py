import pandas as pd

def prepare_games(matchlist):
    matchlist = matchlist[['Home','xGHome','Score','xGAway','Away']]
    matchlist=matchlist[matchlist['xGHome'].notna()]
    return matchlist

