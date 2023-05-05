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
        self.home_path = '/Users/Lidiane/Documents/projects_portfolio/rossmann'
        self.model_pipeline = pickle.load(
            open(self.home_path + '/models/pipe.pkl', 'rb'))
        return None

    def data_cleaning(self, df1):

        # Cria uma cópia do dataframe original
        df_clean = df1.copy()

        # Converter 'Date' para datetime
        df_clean['Date'] = pd.to_datetime(df_clean['Date'], format='%Y.%m.%d') #errors='coerce')
        
        # Filtragem dos dados
        df_clean = df_clean[df_clean['Open'] != 0]

        # Imputação para a coluna 'CompetitionOpenSinceMonth' com a estratégia de moda
        imputer = SimpleImputer(strategy='most_frequent')
        df_clean.loc[:, ['CompetitionOpenSinceMonth']] = imputer.fit_transform(
            df_clean[['CompetitionOpenSinceMonth']])

        # Imputação para a coluna 'CompetitionOpenSinceYear' com a estratégia de moda
        imputer = SimpleImputer(strategy='most_frequent')
        df_clean.loc[:, ['CompetitionOpenSinceYear']] = imputer.fit_transform(
            df_clean[['CompetitionOpenSinceYear']])

        # Imputação para a coluna 'CompetitionDistance' com a estratégia de mediana
        imputer = SimpleImputer(strategy='median')
        df_clean.loc[:, ['CompetitionDistance']] = imputer.fit_transform(
            df_clean[['CompetitionDistance']])

        # Substituição de valores ausentes por zero
        df_clean.loc[:, ['Promo2SinceWeek']] = df_clean['Promo2SinceWeek'].fillna(0)
        df_clean.loc[:, ['Promo2SinceYear']] = df_clean['Promo2SinceYear'].fillna(0)
        df_clean.loc[:, ['PromoInterval']] = df_clean['PromoInterval'].fillna(0)
        
        # Converter tipos
        df_clean['CompetitionOpenSinceYear'] = df_clean['CompetitionOpenSinceYear'].astype(float).astype(int)
        df_clean['CompetitionOpenSinceMonth'] = df_clean['CompetitionOpenSinceMonth'].astype(int)

        return df_clean

    def feature_engineering(self, df2):

        # Year
        df2['Year'] = df2['Date'].dt.year

        # Month
        df2['Month'] = df2['Date'].dt.month

        # Day
        df2['Day'] = df2['Date'].dt.day

        # Week of year
        df2['WeekOfYear'] = df2['Date'].dt.isocalendar().week

        # Year Week
        df2['YearWeek'] = df2['Date'].dt.strftime('%Y-%W')

        # Competition
        df2['CompetitionSince'] = pd.to_datetime(
            df2['CompetitionOpenSinceYear'].astype(str) + '-' +
            df2['CompetitionOpenSinceMonth'].astype(str).str.zfill(2) + '-01')

        df2['CompetitionTimeMonth'] = (
            (df2['Date'] - df2['CompetitionSince']) / np.timedelta64(1, 'M')).astype(int)

        # Promo Since
        promo2since = ((df2['Year'] - df2['Promo2SinceYear']) * 12 +
                       (df2['WeekOfYear'] - df2['Promo2SinceWeek']) * 0.230137)
        df2['Promo2Since'] = promo2since.clip(lower=0) * df2['Promo2']

        # Convertendo tipos de dados
        df2['CompetitionOpenSinceMonth'] = df2['CompetitionOpenSinceMonth'].astype(
            int)
        df2['CompetitionOpenSinceYear'] = df2['CompetitionOpenSinceYear'].astype(
            int)
        df2['Promo2SinceWeek'] = df2['Promo2SinceWeek'].astype(int)
        df2['Promo2SinceYear'] = df2['Promo2SinceYear'].astype(int)

        return df2

    def data_prep(self, df3):
        # Verifica se as colunas necessárias estão presentes no DataFrame
        required_cols = ['DayOfWeek', 'Month', 'Day', 'WeekOfYear']
        missing_cols = set(required_cols) - set(df3.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in DataFrame: {missing_cols}")

        # Transforma o dia da semana em coordenadas polares para preservar a ordem circular
        df3['DayOfWeek_sin'] = df3['DayOfWeek'].apply(
            lambda x: np.sin(x * (2 * np.pi / 7)))
        df3['DayOfWeek_cos'] = df3['DayOfWeek'].apply(
            lambda x: np.cos(x * (2 * np.pi / 7)))

        # Transforma o mês em coordenadas polares para preservar a ordem circular
        df3['Month_sin'] = df3['Month'].apply(
            lambda x: np.sin(x * (2 * np.pi / 12)))
        df3['Month_cos'] = df3['Month'].apply(
            lambda x: np.cos(x * (2 * np.pi / 12)))

        # Transforma o dia do mês em coordenadas polares para preservar a ordem circular
        df3['Day_sin'] = df3['Day'].apply(
            lambda x: np.sin(x * (2 * np.pi / 30)))
        df3['Day_cos'] = df3['Day'].apply(
            lambda x: np.cos(x * (2 * np.pi / 30)))
        # Transforma a semana do ano em coordenadas polares para preservar a ordem circular
        df3['WeekOfYear_sin'] = df3['WeekOfYear'].apply(
            lambda x: np.sin(x * (2 * np.pi / 52)))
        df3['WeekOfYear_cos'] = df3['WeekOfYear'].apply(
            lambda x: np.cos(x * (2 * np.pi / 52)))

        cols_selected = ['Store', 'StoreType', 'CompetitionDistance', 'CompetitionTimeMonth', 'DayOfWeek_sin', 'DayOfWeek_cos',
                         'Assortment', 'Promo2', 'Promo2Since', 'Month_sin', 'Month_cos', 'Day_sin', 'Day_cos', 'WeekOfYear_sin',
                         'WeekOfYear_cos']

        return df3[cols_selected]

     # pipeline e fit
    def get_prediction(self, model, original_data, test_data):

        pred = model.predict(test_data)
        # join pred into original data
        original_data['prediction'] = np.expm1(pred)

        return original_data.to_json(orient='records', date_format='iso')