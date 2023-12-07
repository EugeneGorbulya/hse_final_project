import pandas as pd
from scipy import stats as st

def check_hypothesis(series_1: pd.Series, series_2: pd.Series, alpha=0.05) -> str:
    """
    здесь функция должна сравнивать значимость разницы в оценках между жанром 1 и жанром 2
    и возвращать, етсь эта разница или нет, и в чью пользу
    """
    series_1.dropna(inplace=True)
    series_2.dropna(inplace=True)
    std1 = series_1.std()
    std2 = series_2.std()

    result = st.ttest_ind(series_1, series_2, equal_var=(std1==std2))
    if result.pvalue < alpha:
        return "Можем отвергнуть гипотезу"
    else:
        return "Не можем отвергнуть гипотезу"


def make_series(df: pd.DataFrame, column_name: str, grouping_name: str) -> pd.Series:
    return df.loc[df[column_name] == grouping_name, "salary_in_usd"]
