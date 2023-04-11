import pickle
import pandas as pd
import numpy as np
import math
import datetime
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


class Rossmann(object):

    def __init__(self):
        self.home_path = 'C:/Users/Lidiane/Documents/projects_portfolio/rossmann'
        self.transformations = pickle.load(
            open(self.home_path + '/models/transformations.pkl'))

    def data_cleaning(self, df):

        # DataTime
    df['date'] = pd.to_datetime(df['date'])

    # Filtragem
    df = df[df['Open'] != 0]

    # Preenchendo missing values
    # Imputação para a coluna 'CompetitionOpenSinceMonth' com a estratégia de moda
    imputer = SimpleImputer(strategy='most_frequent')
    df.loc[:, 'CompetitionOpenSinceMonth'] = imputer.fit_transform(
        df[['CompetitionOpenSinceMonth']])

    # Imputação para a coluna 'CompetitionOpenSinceYear' com a estratégia de moda
    imputer = SimpleImputer(strategy='most_frequent')
    df.loc[:, 'CompetitionOpenSinceYear'] = imputer.fit_transform(
        df[['CompetitionOpenSinceYear']])

    # Imputação para a coluna 'CompetitionDistance' com a estratégia de mediana
    imputer = SimpleImputer(strategy='median')
    df.loc[:, 'CompetitionDistance'] = imputer.fit_transform(
        df[['CompetitionDistance']])

    # Substituição de valores ausentes por zero
    df['Promo2SinceWeek'].fillna(0, inplace=True)
    df['Promo2SinceYear'].fillna(0, inplace=True)
    df['PromoInterval'].fillna(0, inplace=True)

    # Convertendo tipos de dados em df
    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].astype(
        int)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].astype(int)
    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].astype(int)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].astype(int)

    return df

    def feature_engineering(self, df):

        # Adicionando features de data
        # Year
    df['Year'] = df['Date'].dt.year
    # Month
    df['Month'] = df['Date'].dt.month
    # Day
    df['Day'] = df['Date'].dt.day
    # Week of year
    df['WeekOfYear'] = df['Date'].dt.isocalendar().week
    # Year Week
    df['YearWeek'] = df['Date'].dt.strftime('%Y-%W')

    # Competition
    df['CompetitionSince'] = pd.to_datetime(
        df['CompetitionOpenSinceYear'].astype(
            str) + '-' + df['CompetitionOpenSinceMonth'].astype(str) + '-01'
    )

    df['CompetitionTimeMonth'] = (
        (df['Date'] - df['CompetitionSince']) / np.timedelta64(1, 'M')).astype(int)

    # Promo2 Since
    promo2since = ((df['Year'] - df['Promo2SinceYear']) * 12 +
                   (df['WeekOfYear'] - df['Promo2SinceWeek']) * 0.230137)
    df['Promo2Since'] = promo2since.clip(lower=0) * df['Promo2']

    return df

    def data_preparation(self, df):

        # Verifica se as colunas necessárias estão presentes no DataFrame
    required_cols = ['DayOfWeek', 'Month', 'Day', 'WeekOfYear']
    missing_cols = set(required_cols) - set(df.columns)
    if missing_cols:
    raise ValueError(f"Missing columns in DataFrame: {missing_cols}")

    # Transforma o dia da semana em coordenadas polares para preservar a ordem circular
    df['DayOfWeek_sin'] = df['DayOfWeek'].apply(
        lambda x: np.sin(x * (2 * np.pi / 7)))
    df['DayOfWeek_cos'] = df['DayOfWeek'].apply(
        lambda x: np.cos(x * (2 * np.pi / 7)))

    # Transforma o mês em coordenadas polares para preservar a ordem circular
    df['Month_sin'] = df['Month'].apply(
        lambda x: np.sin(x * (2 * np.pi / 12)))
    df['Month_cos'] = df['Month'].apply(
        lambda x: np.cos(x * (2 * np.pi / 12)))

    # Transforma o dia do mês em coordenadas polares para preservar a ordem circular
    df['Day_sin'] = df['Day'].apply(
        lambda x: np.sin(x * (2 * np.pi / 30)))
    df['Day_cos'] = df['Day'].apply(
        lambda x: np.cos(x * (2 * np.pi / 30)))
    # Transforma a semana do ano em coordenadas polares para preservar a ordem circular
    df['WeekOfYear_sin'] = df['WeekOfYear'].apply(
        lambda x: np.sin(x * (2 * np.pi / 52)))
    df['WeekOfYear_cos'] = df['WeekOfYear'].apply(
        lambda x: np.cos(x * (2 * np.pi / 52)))

    cols_selected = ['Store', 'StoreType', 'CompetitionDistance', 'CompetitionTimeMonth', 'DayOfWeek_sin', 'DayOfWeek_cos',
                     'Assortment', 'Promo2', 'Promo2Since', 'Month_sin', 'Month_cos', 'Day_sin', 'Day_cos', 'WeekOfYear_sin',
                     'WeekOfYear_cos']

    return df[cols_selected]

    def get_prediction(self, model, original_data, test_data):
        # prediction
    pred = model.predict(test_data)

    # join pred into the original data
    original_data['Prediction'] = np.expm1(pred)

    return original_data.to_json(orient='records', date_format='iso')