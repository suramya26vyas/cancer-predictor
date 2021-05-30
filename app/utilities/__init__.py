from ..config.config import basedir
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import os
import pandas as pd

cancer_dataset = os.path.join(basedir,'data','cancer_classification.csv')

class LibraryUtilities:
    """
    This class contains all the standard functions
    that can be used as library utilities and common
    functionalities
    """
    @staticmethod
    def get_trained_model_and_scalar():
        try:
            cancer_df = pd.read_csv(cancer_dataset)
            X = cancer_df.drop('benign_0__mal_1', axis=1).values
            y = cancer_df['benign_0__mal_1'].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
            scalar = MinMaxScaler()
            X_train = scalar.fit_transform(X_train)
            X_test = scalar.transform(X_test)
            early_stop = EarlyStopping(monitor='val_loss', mode='min', patience=10, verbose=1)

            model = Sequential()
            model.add(Dense(30, activation='relu'))
            model.add(Dropout(0.6))
            model.add(Dense(15, activation='relu'))
            model.add(Dropout(0.6))
            model.add(Dense(1, activation='sigmoid'))
            model.compile(loss='binary_crossentropy', optimizer='adam')

            model.fit(X_train, y_train, epochs=600, verbose=1, validation_data=(X_test, y_test), callbacks=[early_stop])
            return scalar, model
        except Exception:
            raise
