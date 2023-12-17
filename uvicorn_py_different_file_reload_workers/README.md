# Running uvicorn from python with class attribute in *different* file (*with* reload / workers)
Command ran:
```
python main.py
```
Result:
```
changed
INFO:     Will watch for changes in these directories: ['/Users/tommyhe/computer_science/bugs/uvicorn_global_static/C']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [77202] using WatchFiles
INFO:     Started server process [77204]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
original
INFO:     127.0.0.1:61761 - "GET /test HTTP/1.1" 200 OK
original
INFO:     127.0.0.1:61765 - "GET /test HTTP/1.1" 200 OK
```
