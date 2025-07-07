backend server to developed using the Python FastAPi
to start the Backend Server 
CMD:  cd BackendServer
CMD:  python -m uvicorn main:app --reload








helper for AWS Functions

to get eh dependencies as folders use this
/> pip install -t dependencies -r requirements.txt

to zip all the dependencies
/> (cd dependencies; zip -r ../dependencies.zip .)
/> (cd dependencies; zip ../aws_lambda_artifacts.zip -r .)


/>zip aws_lambda_artifacts.zip -u app.py 