# featurerequestmanager.py acts as restful webservice which consists of 3 url end points used to create, retrieve and edit Feature requests into/from database.
# Importing FeatureRequestApp model class
from app import APP,FeatureRequestApp
# from sqlalchemy we can import ascending order
from sqlalchemy import asc
# imports jsonify,request from flask package
from flask import jsonify,request 
# imports featureRequestService.py
from featureRequestService import FeatureRequestService

# FeatureRequestManger class is used to handle the url endpoints 'http://127.0.0.1:5000/createFeatureRequest' which is used to create Feature Requests and 'http://127.0.0.1:5000/retrieveFeatureRequest' which is used to retrieve Feature Request records from database
class FeatureRequestManger:
    """FeatureRequestManger Class is used to manage url end points /createFeatureRequest and /retrieveFeatureRequest"""
    try:
        # createFeatureRequest function is used to create New Feature Request in Database
        @APP.route('/createFeatureRequest', methods=['POST'])
        def createFeatureRequestManager():
            # Instance of FeatureRequestService class is created to accesss function createFeatureRequestService
            featureRequestserviceInstance = FeatureRequestService()
            if request.method == 'POST':
                # Assigning FeatureRequestApp class object with title, description, client, clientPriority, targetData and productArea json values as arguments to createFeatureRequestService function
                # Response from createFeatureRequestService is assigned to 'result'       
                result = featureRequestserviceInstance.createFeatureRequestService(FeatureRequestApp(request.json['title'],request.json['description'],request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea']))
                # Returns a String response
                return result

    except Exception as e:
        print("Error Occured in createFeatureRequestManager",e)
        

    try:
        # retrieveFeatureRequest function is used to retrieve the Feaure Request records from Database
        @APP.route('/retrieveFeatureRequest', methods=['GET'])
        def retrieveFeatureRequestManager():
            # Checks request mehtod is GET
            if request.method == 'GET':
                # Instance of FeatureRequestService class is created to accesss function retrieveFeatureRequestService
                featurerequestServiceInstance= FeatureRequestService()
                # Response from retrieveFeatureRequestService is assigned to 'result'       
                output= featurerequestServiceInstance.retrieveFeatureRequestService()
                # Returns a JSON response 
                return jsonify({'details': output})
                
    except Exception as e:
        print("Error Occured in retrieveFeatureRequestManager",e)


    try:
        # editFeatureRequest function is used to edit values of Feature Request in Database
        @APP.route('/editFeatureRequest', methods=['POST'])
        def editFeatureRequestManager():
            # Instance of FeatureRequestService class is created to accesss function editFeatureRequestService
            featurerequestserviceInstance= FeatureRequestService()
            # Checks request mehtod is POST
            if request.method == 'POST':
                # Assigning FeatureRequestApp class object with title, description, client, clientPriority, targetData and productArea json values as arguments to editFeatureRequestService function
                # Response from createFeatureRequestService is assigned to 'result'       
                result =featurerequestserviceInstance.editFeatureRequestService(FeatureRequestApp(request.json['title'],request.json['description'],request.json['client'],request.json['clientPriority'],request.json['targetDate'],request.json['productArea']))
                # Returns a String response
                return result

    except Exception as e:
        print("Error Occured in editFeatureRequestManager",e)