import os
# from sqlalchemy package we can import create_engine
from sqlalchemy import create_engine
# from sqlalchemy package we can import declarativ_base
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy package we can import sessionmaker
from sqlalchemy.orm import sessionmaker

class Config(object): 
    """ Config class is used to set configurations required for the project."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # SET database connection string
    #db_string = "postgres://postgres:Password0@localhost:5432/featureapp"
    #Need to uncomment when using cloud database
    db_string = "postgres://featureappadmin@featureapp-tm-inslab:Feature123$@featureapp-tm-inslab.postgres.database.azure.com:5432/featureapp"
    # an Engine, which the Session will use for connection
    db = create_engine(db_string)
    # Declarative, which allows us to create classes that include directives to describe the actual database table 
    # they will be mapped to.
    # We create the base class using the declarative_base().“base”, we can define any number of mapped classes.
    base = declarative_base()
    # Specifying tablename for models.py to persist in database.
    table= 'FeatureRequestApp'
    # create a configured "Session" class
    Session= sessionmaker(db)
    #Setting Urls for feature request form page and details page which will be used in testcases
    featureHomePageURL= 'http://127.0.0.1:5000/'
    featureListPageURL= 'http://127.0.0.1:5000/FeatureRequestDetails'


