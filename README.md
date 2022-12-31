# Restaurant System

Patterns and Concepts used:
- [x] Unit Test;
- [x] Integration Test;
- [x] Domain Driven Design;
- [x] Clean Architecture;
- [x] Microservice;
- [ ] Notification Pattern;
- [ ] Event Sourcing;


## Basic Diagram:
![image](https://user-images.githubusercontent.com/55208546/204069761-6afa11f4-5a31-42ad-a16a-08372406a4df.png)

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
pdm istall
```

### Start the local server (will be available at http://127.0.0.1:8000 or localhost:8000)
```
cp .env.example .env
pdm run python main.py
```

### Run tests
```
pdm run pytest -vv -s
```

### Access docs at http://localhost:8000/docs or http://localhost:8000/redoc

