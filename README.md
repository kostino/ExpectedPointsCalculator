# ExpectedPointsCalculator
An expected points calculator for a football league

## Installation
```bash
git clone https://github.com/kostino/ExpectedPointsCalculator.git
pip install -r requirements.txt
```
For image exporting plotly orca is also required. Install as:
```bash
conda install -c plotly plotly-orca
```

## Usage
```bash
python calculator.py <input_file>
```
The input file should be a csv file with a ',' delimitter containing match logs and at least the columns: "Home", "xGHome", "Away", "xGAway". See example_data.csv for reference.  
Prints the expected points table for the league.  
* Save table as csv: --csv or -c
* Save table data as json: --json or -j
* Export as image: --img or -i

Example data extracted from [fbref](https://fbref.com/en/)

## How it works
This calculator works by evaluating each match separately and assigning each team an amount of expected points for the match. The final table is created by adding all the expected points each team has gathered from all their matches. The xPoints a team gains from each match are calculated as follows: ${xPoints = winProb\times3 + drawProb\times1}$
#### How win and draw probabilities are calculated
We can consider the goals a team scores in a match to be a random variable following a Bernoulli distribution with a mean value equal to their expected goals for said match. This way if we know the expected goals for both teams we can find the probability that they score 0,1,2,3,4... etc goals in the match and combining those probabilities for the two teams can give us the win and draw probabilities for the match.  
#### Example: Barcelona - Real Madrid 1-3 24/10/2020
[example](xPoints_Barcelona-RealMadrid_example.ipynb)
