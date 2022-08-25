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
        query = "SELECT * FROM api_main_data;"
        data = self.engine(query)
        return data

    # get_data_between 

    def convert_to_dict(self):
        final_dict = []
        objects = self.get_main_data()
        column = ["id", "heading", "sub_heading", "main_problem", "author_name"]
        for point in objects["data"]:
            temp = {}
            for d in range(len(point)):
                temp[column[d]] = point[d]
            final_dict.append(temp)
 
        return final_dict
        


connects = BitioConnector()
data = connects.convert_to_dict()
 

