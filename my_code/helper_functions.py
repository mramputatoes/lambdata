



def __init__(self):
    return
def null_count(self, df):
    return df.isnull().sum().sum()


def split_date(self):
    """Split Date into month/day/year columns"""
    for item in self.df:
        if self.df[item].dtypes == '<M8[ns]':
            self.df[item+'_month'] = self.df[item].dt.month
            self.df[item+'_day'] = self.df[item].dt.day
            self.df[item+'_year'] = self.df[item].dt.yearh