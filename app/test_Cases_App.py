# Import Unittest to create test cases, requests to post 
import unittest, requests, json
# unittest.mock is a library for testing in Python
from mock import MagicMock
# form config module imports Config class to required url endpoints
from config import Config
# from models.py imports the model class FeatureRequestApp
from models import FeatureRequestApp
# imports featureRequestManager.py, featureRequestService.py 
import featureRequestManager, featureRequestService

# TestCasesApp class inherits unittest.TestCase class and consists of different testcases.
class TestCasesApp(unittest.TestCase):
    
    # test_app_FeatureRequestFormPage function used for testing routing url 'http://127.0.0.1:5000/' in routes.py.
    def test_app_FeatureRequestFormPage(self):
        """Testing working condition of Feature Requests Form Page."""
        self.assertEqual((requests.get(Config.featureHomePageURL)).status_code,200)   

    # test_app_FeatureRequestDeatailsPage function used for testing routing url 'http://127.0.0.1:5000/FeatureRequestDetails' in routes.py.      
    def test_app_FeatureRequestDeatailsPage(self):
        """Testing working condition of Feature Requests Details Page."""
        self.assertEqual((requests.get(Config.featureListPageURL)).status_code,200) 

    # test_app_featureRequestService_createFeatureRequestService used for testing createFeatureRequestService function present in FeatureRequestService class in featureRequestService module using a mock session.
    def test_app_featureRequestService_createFeatureRequestService(self):
        """Testing successful submission of values in Feature Requests Form Page."""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        # Creating an instance of FeatureRequestService class
        featureRequestServiceClassObject= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        featureRequestServiceClassObject.setSession(mock)
        # Creating an instance of FeatureRequestApp model class with all required values
        featureRequestAppClassObject = FeatureRequestApp('Titl5', 'descr','Client B', 1, 'Billing', '2018-02-01')
        result= featureRequestServiceClassObject.createFeatureRequestService(featureRequestAppClassObject)
        self.assertEqual(result,'success')

    # test_app_featureRequestService_retrieveFeatureRequestService used for testing retrieveFeatureRequestService function present in FeatureRequestService class in featureRequestService module using a mock session.
    def test_app_featureRequestService_retrieveFeatureRequestService(self):
        """Testing successful retrieval of values from database for Feature Request Details."""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        # Creating an instance of FeatureRequestService class
        featureRequestServiceClassObject= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        featureRequestServiceClassObject.setSession(mock)
        # Creating an instance of FeatureRequestApp model class with all required values
        result= featureRequestServiceClassObject.retrieveFeatureRequestService()
        # Checking result of retrieveFeatureRequestService
        self.assertIsNotNone(result)

    # test_app_featureRequestService_reprioritizeFeatureRequestService used for testing reprioritizeFeatureRequestService function present in FeatureRequestService class in featureRequestService module using a mock session.
    def test_app_featureRequestService_reprioritizeFeatureRequestService(self):
        """Testing reprioritize of values in Feature Request Service to get an Error according given test case values(invalid values)."""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        # Creating an instance of FeatureRequestService class
        featureRequestServiceClassObject= featureRequestService.FeatureRequestService()
        # Setting a mock session using setSession function in FeatureRequestService class. 
        featureRequestServiceClassObject.setSession(mock)
        # Creating an instance of FeatureRequestApp model class with all required incorrect values.
        featureRequestAppClassObject = FeatureRequestApp('tileo0092', 'descr','Client B', 'invalid valeue', 'Billing', '2018-02-01')
        result= featureRequestServiceClassObject.reprioritizeFeatureRequestService(featureRequestAppClassObject)
        self.assertEqual(result,'Error Occured')

    

  

    
        
        

