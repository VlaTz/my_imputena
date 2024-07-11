import pandas as pd
import numpy as np


def generate_example_df():
    return pd.DataFrame(
        data={
            'x': np.array([18, np.nan, 27, 22]),
            'y': np.array([np.nan, 1, 5, -3.0]),
            'z': np.array([9, 4, 2, 7])
        },
        index=list([x for x in range(1, 5)])
    )


def generate_example_df_divcols():
    """
    Example data frame with 10 rows for 8 columns. Has diverse columns.

    By columns:
    3 columns (a, b and d) contain only non-NA values.
    1 column (e) contains 1 NA value.
    2 columns (f and g) contain 2 NA values.
    1 column (h) contains 3 NA values.
    1 column (c) contains only NA values.

    By rows:
    5 rows (5 - 9) contain 1 NA value.
    3 rows (2, 4 and 10) contain 2 NA values.
    1 row (3) contains 3 NA values.
    1 row (1) contains 4 NA values.

    Representation:

         a  b   c     d     e     f    g    h
    1    1  0 NaN   7.4   NaN   NaN  NaN  5.0
    2    2  0 NaN   5.2  -6.2  -3.0  2.0  NaN
    3    3  0 NaN   7.0  34.5   NaN  2.0  NaN
    4    4  0 NaN   8.0   8.0   7.0  0.0  NaN
    5    5  0 NaN   8.0   5.0   4.3  9.0 -5.5
    6    6  0 NaN   6.0   3.0   1.3  0.5 -0.1
    7    7  0 NaN   2.0   2.0   8.0  7.0  2.0
    8    8  0 NaN  15.3   5.0  12.0  5.0  3.0
    9    9  0 NaN   2.0   6.0  -3.0  4.3  4.0
    10  10  0 NaN   4.0   6.0   5.0  NaN  5.0
    """
    return pd.DataFrame(
        data={
            'a': np.array([
                1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]),
            'b': np.array([
                0, 0, 0, 0, 0,
                0, 0, 0, 0, 0]),
            'c': np.array([
                np.nan, np.nan, np.nan, np.nan, np.nan,
                np.nan, np.nan, np.nan, np.nan, np.nan]),
            'd': np.array([
                7.4, 5.2, 7, 8, 8,
                6, 2, 15.3, 2, 4]),
            'e': np.array([
                np.nan, -6.2, 34.5, 8, 5,
                3, 2, 5, 6, 6]),
            'f': np.array([
                np.nan, -3.0, np.nan, 7, 4.3,
                1.3, 8, 12, -3, 5]),
            'g': np.array([
                np.nan, 2, 2, 0, 9,
                0.5, 7, 5, 4.3, np.nan]),
            'h': np.array([
                5, np.nan, np.nan, np.nan, -5.5,
                -0.1, 2, 3, 4, 5])
        },
        index=list([x for x in range(1, 11)])
    )


def generate_example_df_hotdeck():
    """
    Example data frame with 6 rows for 4 columns. Prepared specifically for
    testing random hot deck imputation.

    Representation:

         a  b     c  d
    1  3.1  x  None  i
    2  NaN  x     a  j
    3  NaN  y     b  k
    4  5.7  y     c  l
    5  8.0  x     d  m
    6  1.2  y     e  n
    """
    return pd.DataFrame(
        data={
            'a': np.array([
                3.1, np.nan, np.nan, 5.7, 8.0, 1.2]),
            'b': np.array([
                'x', 'x', 'y', 'y', 'x', 'y']),
            'c': np.array([
                None, 'a', 'b', 'c', 'd', 'e']),
            'd': np.array([
                'i', 'j', 'k', 'l', 'm', 'n']),

        },
        index=list([x for x in range(1, 7)])
    )


def generate_example_series():
    return pd.Series(
        data=np.array([np.nan, 4, -3, np.nan, 24, np.nan]),
        index=list([x for x in range(1, 7)])
    )


def generate_ts_airgap():
    """
    Timeseries describing monthly totals of international airline passengers
    (presumably in millions) and containing 13 missing values. This series
    has a strong multiplicative seasonal component.


    Adapted from the imputeTS R package, with data originating from:
    George E. P. Box, Gwilym M. Jenkins, Gregory C. Reinsel, Greta M. Ljung
        (2015). Time Series Analysis: Forecasting and Control. Fifth Edition.
        (John Wiley & Sons)
    """
    return pd.Series(
        np.array([
            112, 118, 132, 129, np.nan, 135, 148, 148, np.nan, 119, 104, 118,
            115, 126, 141, 135, 125, 149, 170, 170, np.nan, 133, np.nan, 140,
            145, 150, 178, 163, 172, 178, 199, 199, 184, 162, 146, 166,
            171, 180, 193, 181, 183, 218, 230, 242, 209, 191, 172, 194,
            196, 196, 236, 235, 229, 243, 264, 272, 237, 211, 180, 201,
            204, 188, 235, 227, 234, np.nan, 302, 293, 259, 229, 203, 229,
            242, 233, 267, 269, 270, 315, 364, 347, 312, 274, 237, 278,
            284, 277, np.nan, np.nan, np.nan, 374, 413, 405, 355, 306, 271,
            306,
            315, 301, 356, 348, 355, np.nan, 465, 467, 404, 347, np.nan, 336,
            340, 318, np.nan, 348, 363, 435, 491, 505, 404, 359, 310, 337,
            360, 342, 406, 396, 420, 472, 548, 559, 463, 407, 362, np.nan,
            417, 391, 419, 461, np.nan, 535, 622, 606, 508, 461, 390, 432
        ]),
        index=pd.date_range(start='1949', end='1961', freq='M')
    )


def generate_ts_ausbeer():
    """
    Timeseries describing total quarterly beer production in Australia (in
    megaliters) from 1956:Q1 to 1967:Q3 and containing 9 NA values. This
    series has a strong additive seasonal component.

    Adapted from the fpp R package (Rob J Hyndman), with data originating from
    the Australian Bureau of Statistics.
    """
    return pd.Series(
        np.array([
            284, 213, 227, 308,
            np.nan, 228, 236, 320,
            272, np.nan, np.nan, 313,
            261, 227, 250, 314,
            286, np.nan, 260, 311,
            np.nan, 233, 257, 339,
            279, 250, np.nan, 346,
            294, np.nan, 278, np.nan,
            313, np.nan, 300, 370,
            331, 288, 306, 386,
            335, 288, 308, 402,
            353, 316, 325, 405
        ]),
        index=pd.date_range(start='1956', end='1968', freq='3M')
    )


def generate_example_df_ts():
    """
    Example data frame containing two columns:
    airgap: 131 integers, 13 NA values
    empty: 144 NA values
    """
    ts_airgap = generate_ts_airgap()
    return pd.DataFrame(
        data={
            'airgap': ts_airgap,
            'empty': np.nan
        }
    )


def generate_df_sales():
    """
    Example dataframe.

    In the complete dataset, the relationship between year, advertising and
    sales is roughly described by the following regression equation:
    'sales' = -91945.21814713 + 13.98961204*'advertising' + 46.6003816*'year'

    The dataframe contains 8 NA values.

    Representation:

          year  advertising   sales
    1      NaN          NaN     NaN
    2   1981.0         23.0   651.0
    3   1982.0         26.0   762.0
    4      NaN         30.0     NaN
    5   1984.0         34.0  1063.0
    6   1985.0          NaN     NaN
    7   1986.0         48.0  1298.0
    8   1987.0         52.0  1421.0
    9   1988.0         57.0  1440.0
    10  1989.0         58.0     NaN
    """
    return pd.DataFrame({
        'year': np.array(
            [np.nan, 1981, 1982, np.nan, 1984, 1985, 1986, 1987, 1988, 1989]),
        'advertising': np.array(
            [np.nan, 23, 26, 30, 34, np.nan, 48, 52, 57, 58]),
        'sales': np.array(
            [np.nan, 651, 762, np.nan, 1063, np.nan, 1298, 1421, 1440, np.nan])
    }, index=list([x for x in range(1, 11)]))


def generate_df_breast_cancer():
    """
    Example dataframe used to test logistic regression.

    Adapted from: Breast Cancer Wisconsin (Diagnostic) Data Set (UCI Machine
    Learning Repository)

    Contains 15 missing values.

        thickness  uniformity  adhesion  size  nucleoli  mitoses class
    0         1.0         1.0         1   1.0        1        1     B
    1         1.0         1.0         1   2.0        1        1     B
    2         8.0         4.0         3   3.0        3        1     B
    3         4.0         1.0         1   2.0        6        1     B
    4        10.0         8.0         4   4.0       10        4  None
    5         5.0         1.0         1   2.0        2        1     B
    6         NaN        10.0        10   3.0        6        1  None
    7         3.0         3.0         1   2.0        1        1     B
    8         3.0         NaN         1   2.0        1        1  None
    9         2.0         3.0         1   5.0        1        1     B
    10        NaN         1.0         1   NaN        1        1  None
    11        5.0         2.0         2   1.0        1        1     B
    12       10.0         NaN         2   NaN        7        1  None
    13        7.0         8.0         2   4.0        8        2     M
    14        8.0         4.0         1   3.0        9        2  None
    15        1.0         1.0         1   2.0        1        1     B
    16        4.0         1.0         1   2.0        1        1  None
    17        1.0         2.0         1   2.0        1        1     B
    18       10.0         NaN         4   NaN       10        1     M
    19        1.0         1.0         1   2.0        1        1     B
    20        3.0         1.0         1   2.0        1        1     B
    21        5.0         1.0         1   2.0        1        1     B
    22        4.0         1.0         1   2.0        1        1     B
    23        8.0         4.0         1   2.0        3        1     M
    24        8.0         7.0         4   5.0       10        1     M
    25       10.0         4.0        10   4.0        1        1     M
    26        8.0         3.0         9   3.0        3        1     M
    27        8.0        10.0         8   7.0        7        1     M
    28        6.0         1.0         1   2.0        1        1     B
    29        4.0         1.0         1   2.0        1        1     B
    """
    return pd.DataFrame({
        'thickness': np.array(
            [1.0, 1.0, 8.0, 4.0, 10.0, 5.0, np.nan, 3.0, 3.0, 2.0, np.nan, 5.0,
             10.0, 7.0, 8.0, 1.0, 4.0, 1.0, 10.0, 1.0, 3.0, 5.0, 4.0, 8.0, 8.0,
             10.0, 8.0, 8.0, 6.0, 4.0]),
        'uniformity': np.array(
            [1.0, 1.0, 4.0, 1.0, 8.0, 1.0, 10.0, 3.0, np.nan, 3.0, 1.0, 2.0,
             np.nan, 8.0, 4.0, 1.0, 1.0, 2.0, np.nan, 1.0, 1.0, 1.0, 1.0, 4.0,
             7.0, 4.0, 3.0, 10.0, 1.0, 1.0]),
        'adhesion': np.array(
            [1, 1, 3, 1, 4, 1, 10, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 4, 1, 1, 1,
             1, 1, 4, 10, 9, 8, 1, 1]),
        'size': np.array(
            [1.0, 2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 2.0, 5.0, np.nan, 1.0,
             np.nan, 4.0, 3.0, 2.0, 2.0, 2.0, np. nan, 2.0, 2.0, 2.0, 2.0, 2.0,
             5.0, 4.0, 3.0, 7.0, 2.0, 2.0]),
        'nucleoli': np.array(
            [1, 1, 3, 6, 10, 2, 6, 1, 1, 1, 1, 1, 7, 8, 9, 1, 1, 1, 10, 1, 1,
             1, 1, 3, 10, 1, 3, 7, 1, 1]),
        'mitoses': np.array(
            [1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1]),
        'class': ['B', 'B', 'B', 'B', None, 'B', None, 'B', None, 'B', None,
                  'B', None, 'M', None, 'B', None, 'B', 'M', 'B', 'B', 'B',
                  'B', 'M', 'M', 'M', 'M', 'M', 'B', 'B']
    })


def generate_ts_cat():
    """
    Example timeseries with categorical values.
    """
    return pd.Series(
        data=['A', None, 'B', None, None, 'A', 'C', 'A', None, 'B'],
        index=pd.date_range(start='2000', end='2010', freq='Y')
    )


def generate_example_df_ts_cat():
    """
    Example data frame containing two columns:
    grades: 6 strings, 4 None values
    empty: 10 None values
    """
    grades = generate_ts_cat()
    return pd.DataFrame(
        data={
            'grades': grades,
            'empty': None
        }
    )


def generate_example_df_ts_cat_and_num():
    """
    Example data frame containing three columns:
    grades: 6 strings, 4 None values
    points: 8 integers, 2 NA values
    empty: 10 None values
    """
    grades = generate_ts_cat()
    return pd.DataFrame(
        data={
            'grades': grades,
            'points': np.array([5, 3, np.nan, np.nan, 0, 1, 3, 5, 8, 7]),
            'empty': None
        }
    )


def generate_example_df_high_corr():
    """
    Example data frame with high correlation between columns.
    """
    return pd.DataFrame(
        data={
            'a': np.array([
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            'b': np.array([
                2, 4, 6, 8, 10, 12, 14, 16, 18, np.nan]),

        },
        index=list([x for x in range(1, 11)])
    )
