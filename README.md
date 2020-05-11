# Usage:
1. Activate virtual environment
> For Ubuntu
``` 
python -m venv env
source env/bin/activate
```
> For Windows
```
python -m venv env
env/Scripts/activate
```
2. Install requirements
```pip install -r requirements.txt```

3. Update .env file

> Go through all variables in .env file and update them if necessary

4. Run server

```
python template.py
```

or

```
flask run
```

# Development instructions

* 'mini_app1' is template for mini apps inside project
* After creating a new app inside project update __init__.py file in root folder
* Its better to go through services and tests 
