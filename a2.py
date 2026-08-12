from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


def one_hot_encode(df, column):
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    
    encoded = encoder.fit_transform(df[[column]])
    
    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out([column])
    )
    
    df = df.drop(column, axis=1)
    df = pd.concat([df.reset_index(drop=True),
                    encoded_df.reset_index(drop=True)], axis=1)
    
    return df



def label_encode(df, column):
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column])
    return df