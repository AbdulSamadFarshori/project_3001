from sqlalchemy import create_engine

class BitIo(object):

    def __init__(self):
        self.eng=create_engine('postgresql://sumir40:v2_3tLey_LBZ8qKULLd8c7uLA8XY3PeH@db.bit.io/sumir40/project_3001', isolation_level="AUTOCOMMIT")


    def get_records(self):
        with self.eng.connect() as conn:
            result = conn.execute("SELECT * FROM main_data;")
            return result

