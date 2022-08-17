import requests

class BitioConnector(object):
    
    def __init__(self):
        self.string = "v2_3tRkM_JwL4zBbvrRxaunZnkN4bHJ8"
        self.database = "sumir40/project_3001"

    def engine(self, query):
        headers = {"Authorization": "Bearer {}".format(self.string),
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    }
        url = "https://api.bit.io/v2beta/query"

        data = {"query_string":"{}".format(query), "database_name":"{}".format(self.database)}

        response = requests.post(url, json=data, headers=headers)
        return response.json() 


        

    def get_main_data(self):
        query_anxiety = "SELECT * FROM api_main_data WHERE heading = 'Anxiety Disorders' LIMIT 2000;"
        query_depression = "SELECT * FROM api_main_data WHERE heading = 'Depression' LIMIT 2000;"
        anxiety_data = self.engine(query_anxiety)
        depression_data = self.engine(query_depression)
        return anxiety_data, depression_data

    # get_data_between 

    def convert_to_dict(self):
        final_dict = []
        anxiety_object, depression_object = self.get_main_data()
        column = ["id", "heading", "sub_heading", "main_problem", "author_name"]
        for point in anxiety_object["data"]:
            temp = {}
            for d in range(len(point)):
                temp[column[d]] = point[d]
            final_dict.append(temp)

        for row in depression_object["data"]:
            temp2 = {}
            for d in range(len(row)):
                temp2[column[d]] = row[d]
            final_dict.append(temp2)
        
        return final_dict
        


connects = BitioConnector()
data = connects.convert_to_dict()
 

