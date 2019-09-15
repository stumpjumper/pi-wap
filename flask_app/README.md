cd <dir flask_hello.py is in>
export FLASK_ENV=development
export FLASK_APP=flask_hello.py
# --host='0.0.0.0' makes it available to all computers on the network
flask run --host='0.0.0.0'
