# Running uvicorn from python with class attribute in *same* file
Command ran:
```
python main.py
```
Result:
```
changed
INFO:     Started server process [75900]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
original
INFO:     127.0.0.1:61318 - "GET /test HTTP/1.1" 200 OK
original
INFO:     127.0.0.1:61337 - "GET /test HTTP/1.1" 200 OK
```
