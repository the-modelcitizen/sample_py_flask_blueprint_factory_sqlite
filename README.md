#SAMPLE_PY_FLASK_BLUEPRINT_FACTORY_SQLITE 

This is a base Flask app that uses Blueprints to allow multiple apps to be
integrated into one larger Flask app.

to start Flask app:

1. open terminal
2. cd into directory containing app (sample_run.py and sample_test.py should
    be in directory), in this example the directory is
    'sample_py_flask_blueprint_factory_sqlite'
3. check requirements.txt and install required packages into your virtual
    environment
4.a. to run in non-test mode, in terminal run the following command:
    python sample_run.py
    -if you've already run sample_test.py in this terminal session, you will
    need to close the terminal and start a new terminal session to change the
    environment variables from 'test' to 'run'
4.b. to run in test mode, in terminal run the following command:
    python sample_test.py
    -if you've already run sample_run.py in this terminal session, you will
    need to close the terminal and start a new terminal session to change the
    environment variables from 'run' to 'test'
5. open web browser (Chrome preferred)
6. type in url localhost:5000 and hit enter to see results of app2 root
    route call
7. to test routes in app1 or app2 other than root routes, first create
    sample.db or sample_test.db by following the directions in the comments of
    sample_run.py or sample_test.py


I'd like to thank Miguel Grinberg 
(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world),
assorted contributors in the digitalocean.com community and, of course, everyone
that contributes to the best friend of all developers, stackoverflow.com. 

