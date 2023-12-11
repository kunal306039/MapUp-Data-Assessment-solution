import pandas as pd
import numpy as np


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    df = pd.crosstab(df.id_1, df.id_2, values=df.car, aggfunc='sum').fillna(0)

    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    def get_type_counts(x):
        if x >= 25:
            return 'high'
        elif x > 15 and x < 25:
            return 'medium'
        else:
            return 'low'

    df['car_type'] = df['car'].apply(get_type_counts)
    df = df.car_type.value_counts()

    return df.to_dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here

    bus_mean = df['bus'].mean()

    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    bus_indexes.sort()

    return list(bus_indexes)




def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    l = []
    for i in range((df.shape)[0]):
        if df.car[i] > 7:
            l.append(df.route[i])
        else:
            pass
    route = np.array(sorted(l))

    return list(route)


def multiply_matrix(df)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    def matrix(x):
        if x > 20:
            return round((x * 0.75), 1)
        else:
            return round((x * 1.25), 1)

    mul_matrix = pd.crosstab(df.id_1, df.id_2, values=df['car'].apply(matrix), aggfunc='sum').fillna(0)

    return mul_matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
