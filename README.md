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
python calculator.py input_data.csv
```
Prints the expected points table for the league.  
* Save table as csv: --csv or -c
* Save table data as json: --json or -j
* Export as image: --img or -i
