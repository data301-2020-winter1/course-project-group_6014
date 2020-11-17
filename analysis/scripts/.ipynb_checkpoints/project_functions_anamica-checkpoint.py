import pandas as pd
import numpy as np

def load_process_data(path_to_csv):

    # Method Chain 1 (load data and deal with missing data)

    df1 = (
        pd.read_csv(path_to_csv)
        .drop(columns = ['NationalITy', 'StageID','SectionID', 'Semester', 'Relation', 'ParentAnsweringSurvey'])
        .dropna(axis = 0, thresh = 3)
        .rename(columns={"gender":"Gender", "raisedhands":"RaisedHands", "VisITedResources": "VisitedResources"})
    )
    
    df1

    # Method Chain 2 (create new columns)

    df2 = (df1
       .assign(TotalInteraction = lambda row: row.RaisedHands + row.VisitedResources + row.AnnouncementsView + row.Discussion)
          )
    df2
    
    return df2