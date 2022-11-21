### Project download
```
git clone https://github.com/churros-py/user-microservice-python.git
```

### Access the project directory
```
cd user-microservice-python
```

### Initialization of the virtual environment
```
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Start the local server (will be available at http://127.0.0.1:8000 or localhost:8000)
```
cp .env.example .env
uvicorn main:app --reload
```

### Run tests
```
python -m pytest tests -s
```

### Access docs at http://localhost:8000/docs or http://localhost:8000/redoc
