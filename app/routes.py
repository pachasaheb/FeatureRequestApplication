# routes.py acts as view for the project which renders html pages on routing to 'http://127.0.0.1:5000/' and 'http://127.0.0.1:5000/FeatureRequestDetails'

# from flask import render_template() To render a template.
from flask import render_template
# from app folder importing flask variable APP
from app import APP

# On Flask app run whenever user navigates to url 'http://127.0.0.1:5000/FeatureRequestDetails' FeatureRequestDetails function renders featureRequestDetails.html

@APP.route('/FeatureRequestDetails')
def featureRequestDetails():
    """ featureRequestDetails function is used to display featureRequestDetails html page"""
    return render_template('featureRequestDetails.html')

# On Flask app run when user navigates to url 'http://127.0.0.1:5000/' FeatureRequestForm function renders featureRequestForm.html

@APP.route('/')
def featureRequestForm():
    """ featureRequestForm function is used to display featureRequestForm html page"""
    return render_template('featureRequestForm.html')