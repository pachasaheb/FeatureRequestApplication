# from sqlalchemy package we can import Column, String, Integer, Date, Sequence
from sqlalchemy import Column, String, Integer, Date, Sequence
# imports Config class from config module
from config import Config
#exception handling using try except for FeatureRequestAppClass.
try:
    # A class FeatureRequestApp will be the class to which we map 'FeatureRequestApp' table and contains requeired columns from table as variable in class.
    class FeatureRequestApp(Config.base):
        """Simple database model with required columns and table name."""    
        # A class using Declarative  needs a __tablename__ attribute, and one Column which is a primary key 
        __tablename__ = 'FeatureRequestApp'
        featureId = Column('featureId', Integer, Sequence('feature_id_seq'),unique=True,primary_key=True)
        title = Column(String(250),unique=True)
        description = Column(String(1000))
        client = Column(String(100)) 
        clientPriority = Column(Integer())
        targetDate = Column(Date())
        productArea = Column(String(100))
        # __init__ is a special method in Python classes, it is the constructor method for a class
        # __init__ is called when ever an object of the class is constructed.
        def __init__(self, title, description, client, clientpriority, targetdate, productarea):
            self.title = title
            self.description = description
            self.client = client
            self.clientPriority = clientpriority
            self.targetDate = targetdate
            self.productArea = productarea
    # The declarative_base() base class contains a MetaData object where newly defined Table objects are collected.  
    # This object is to be accessed  for MetaData-specific operations.Such as, to issue CREATE statements for all tables.
    Config.base.metadata.create_all(Config.db)
except ArgumentError as argexp:
    print('Missing connection string or primary key', argexp)

except UnboundExecutionError as unexp:
    print('SQL was attempted without a database connection to execute it on', unexp)

except IndexError as indexerror:
    print('Missing Table Name', indexerror)

except TypeError as typeerror:
    print('Check Params', typeerror)

except TimeoutError as timeout:
    print('Connection TimedOut', timeout)