import pandas as pd
import argparse
from xpoints import xpoints
from prepare_games import prepare_games

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_data",help="CSV file containing input data")
    parser.add_argument("-i","--img",help="Generate image for xpoints table",action="store_true")
    parser.add_argument("-j","--json",help="Save xpoints data as JSON",action="store_true")
    parser.add_argument("-c","--csv",help="Save xpoints data as CSV",action="store_true")
    args = parser.parse_args()
    results = pd.read_csv(str(args.input_data))
    results = prepare_games(results)
    xpoints_dict = xpoints(results)
    xpoints_df = pd.DataFrame.from_dict(xpoints_dict, orient='index', dtype='float64',columns=['xPoints'])
    xpoints_df.sort_values(by="xPoints",inplace=True,ascending=False)
    print(xpoints_df)



if __name__=='__main__':
    main()
