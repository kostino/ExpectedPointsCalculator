import pandas as pd
import sys
from xpoints import xpoints
from prepare_games import prepare_games

def main():
    if len(sys.argv) != 2:
        print('Incorrect usage!. Use as:\n python3 calculator.py <results_file.csv>')
    print(sys.argv[1])
    results = pd.read_csv(sys.argv[1])
    results = prepare_games(results)
    xpoints_dict = xpoints(results)
    print(xpoints_dict)


if __name__=='__main__':
    main()
