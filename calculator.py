import pandas as pd
import numpy as np
import argparse
import json
import plotly.figure_factory as ff
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
    xpoints_df.reset_index(inplace=True)
    xpoints_df.rename(inplace=True,columns={'index':'Team'})
    xpoints_df.index = np.arange(1, len(xpoints_df) + 1)
    print(xpoints_df)
    if args.json:
        with open(str(args.input_data).split('.')[0]+'-xPoints.json','w') as jsonfile:
            json.dump(xpoints_dict,jsonfile)

    if args.csv:
        with open(str(args.input_data).split('.')[0]+'-xPoints.csv','w') as csvfile:
            xpoints_df.to_csv(csvfile)

    if args.img:
        fig = ff.create_table(xpoints_df)
        fig.update_layout(autosize=False, height=30*len(xpoints_dict.keys()),width=300)
        fig.write_image(str(args.input_data).split('.')[0]+"-xPoints.png")

if __name__=='__main__':
    main()
