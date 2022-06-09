# Time-proof Time-series Reduction Algorithm

## TTRA is a lightweight algorithm reducing a time-series ommiting the time.</br> It has been described in the Master's Thesis.

## Example of real-time usage

![animation](https://user-images.githubusercontent.com/50794170/172917936-8bcaf164-5d1c-430f-9e98-23c48cc86816.gif)

## Installation

```bash
pip install -i https://test.pypi.org/simple/ ttra
```

## Usage

```python
import pandas as pd
from ttra import TTRA

# define minimal percentage change that should be detected by TTRA
PCT_CHANGE: float = 0.01
    
# let's take the inflation in Poland as an example
source: str = "https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultstronaopisowa/4741/1/1/miesieczne_wskazniki_cen_towarow_i_uslug_konsumpcyjnych_od_1982_roku_13-05-2022.csv"
    
# download and process data
inflation = pd.read_csv(source,encoding='ISO-8859-2',sep=';').sort_values(['Rok','Miesišc'])
inflation = inflation[inflation['Sposób prezentacji'] == 'Analogiczny miesišc poprzedniego roku = 100']
inflation = inflation['Wartoć'].dropna().map(lambda x: x.replace(',','.')).astype(float)
inflation = inflation.iloc[-12*25:].reset_index(drop=True) # last 25 years only to not obscure the newest data

# initiate TTRA and reduce data with a given PCT_CHANGE
tr = TTRA(inflation)
reduced = tr.run(PCT_CHANGE).x

# plot data, reduced data and an assumption of the current extremum
inflation.plot()
reduced.plot()
plt.scatter(tr.a.Index, tr.a.x, s= 150 , color='black')
```
### Output
![image](https://user-images.githubusercontent.com/50794170/172924805-bacaeda7-a88b-4726-bce6-1cf1ab5607e1.png)
