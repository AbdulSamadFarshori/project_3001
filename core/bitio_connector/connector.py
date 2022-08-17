from sqlalchemy import create_engine
import pandas as pd

class BitioConnector(object):
    
    def __init__(self):
        self.string = "postgresql://sumir40:v2_3tRg3_44jAdLpQamRykebkeyeTwu2@db.bit.io/sumir40/project_3001"

    def engine(self):
        eng=create_engine(self.string, isolation_level="AUTOCOMMIT")
        return eng 

    def callback(self, query):
        with self.engine().connect() as conn:
            result = conn.execute("{}".format(query))
            return result

    def get_main_data(self):
        query_anxiety = "SELECT * FROM api_main_data WHERE heading = 'Anxiety Disorders' LIMIT 2000;"
        query_depression = "SELECT * FROM api_main_data WHERE heading = 'Depression' LIMIT 2000;"
        anxiety_data = self.callback(query_anxiety)
        depression_data = self.callback(query_depression)
        return anxiety_data, depression_data

    # get_data_between 

    def convert_to_dict(self):
        
        anxiety_object, depression_object = self.get_main_data()
        _key = anxiety_object.keys()
        anx_df = pd.DataFrame(anxiety_object.all())
        dep_df = pd.DataFrame(depression_object.all())
        all_join = [anx_df, dep_df]
        final_df = pd.concat(all_join)
        data_dict = final_df.to_dict("records")
        return data_dict


connects = BitioConnector()
data = connects.convert_to_dict() 

