### installation steps:

1. python 3.11.8 or newer installed

2. create a virtual envoriment: `python -m venv venv`

3. activate env then install required packages:
   `pip install -r requirements`

4. run via either:

- default python testing/development `python -m main.py`

- uwsgi for production puropses:
  `uwsgi --http 127.0.0.1:5000 --wsgi-file main.py --callable app`

access via 127.0.0.1:5000
