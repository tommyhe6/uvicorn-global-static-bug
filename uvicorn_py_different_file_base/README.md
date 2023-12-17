# Running uvicorn from python with class attribute in *different* file (*no* reload / workers)
Command ran:
```
python main.py
```
Result:
```
changed
INFO:     Started server process [76930]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
changed
INFO:     127.0.0.1:61672 - "GET /test HTTP/1.1" 200 OK
changed
INFO:     127.0.0.1:61675 - "GET /test HTTP/1.1" 200 OK
```
