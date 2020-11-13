import pandas as pd
import numpy as np

def load_process_data(path_to_csv):

    # Method Chain 1 (load data, drop unnecessary columns, and address missing data)

    df2 = (
        pd.read_csv(path_to_csv)
        .drop(columns = ['NationalITy', 'PlaceofBirth', 'GradeID', 'SectionID', 'Topic', 'Semester', 'Relation', 'ParentAnsweringSurvey', 'ParentschoolSatisfaction'])
        .dropna(axis = 0, thresh = 3)
        .rename(columns={"StageID":"grade_level", "raisedhands":"hands", "VisITedResources": "num_resource", "AnnouncementsView" : "announce", "Discussion":"discuss","StudentAbsenceDays":"absent", "Class":"final_grade"})
    )
    df2


    # Method Chain 2 (create new sum column and ??)

    df3 = (df2
       .assign(interaction_sum = lambda row: row.hands + row.num_resource + row.announce + row.discuss)
          )
    df3
    
    return df3