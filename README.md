### install Python
https://www.python.org/downloads/

### Check Python version, it should be 3.1x
`python3 --version`

### Create environment
`python3 -m venv [environment_name]

### Activate environment
`source [environment_name]/bin/activate`

### install main dependencies
`pip install fastapi`
`pip install uvicorn`

### Start the app
`uvicorn app.main:app --reload`

### Access the documentation of your web service
[]()

### Project structure
```
WebService/
│
├── app/
│   ├── __init__.py
│   ├── main.py         # Main web service file
│   └── models.py       # Database models for messages and conversation (optional, for the future)
│
├── .gitignore          # Add filenames you do not want to be added to your repository here
├── requirements.txt    # Dependencies
└── README.md           # The file you are reading right now :)
```