import pandas as pd

class TTRA:

    """
    Implementation of TTRA
    ...

    Attributes
    ----------
    data : pd.Series
        a data which is to be reduced

    Methods
    -------
    run(pct_change : float)
        Conducts the reduction of data
    """
    
    def __init__(self, data: pd.Series):
        self.data = data.reset_index(drop=True).dropna()
        self.pct_change = self.data.pct_change()
        self.df = pd.DataFrame({'x':self.data})

    def calc_change(self, xt: tuple) -> float:
        """
        Calculates a change between current observation and local extremum's assumption
        """
        x_now = xt[1]
        x_a = self.a[1]
        self.change = (x_now-x_a)/x_a
        
    def check_change(self) -> bool:
        """
        Checks whether the calc_change results exceedes the set threshold
        """
        return abs(self.change) >= self.min_change

    def reduce(self, min_change: float) -> pd.DataFrame:
        """
        Performs TTRA with a given threshold
        
        Parameters
        ----------
            min_change : float
                A threshold for finding only sufficiently big movements
        
        Returns
        -------
            reduced data : pd.DataFrame
        """
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