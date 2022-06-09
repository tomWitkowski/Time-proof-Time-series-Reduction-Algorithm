import pandas as pd

class TTRA:

    """
    Klasa służąca do wykonania algorytmu TTRA
    """
    
    def __init__(self, data: pd.Series):
        self.data = data.reset_index(drop=True).dropna()
        self.pct_change = self.data.pct_change()
        self.df = pd.DataFrame({'x':self.data})

    def calc_change(self, xt: tuple) -> float:
        x_now = xt[1]
        x_a = self.a[1]
        self.change = (x_now-x_a)/x_a
        
    def check_change(self) -> bool:
        return abs(self.change) >= self.min_change

    def run(self, min_change: float) -> pd.DataFrame:

        self.min_change = min_change
        self.gather = []
        self.ad = True

        for self.i, self.xt in enumerate(self.df.itertuples()):
            if self.i == 0: 
                self.a = self.xt
            elif self.xt[0]>1:
                self.calc_change(self.xt)
                if self.ad:
                    if self.change>0:
                        self.a = self.xt
                    elif self.check_change():
                        self.ad = False
                        self.gather.append(self.a)
                        self.a = self.xt
                else:
                    if self.change<0:
                        self.a = self.xt
                    elif self.check_change():
                        self.ad = True
                        self.gather.append(self.a)
                        self.a = self.xt
                    
        return pd.DataFrame(self.gather).set_index('Index')