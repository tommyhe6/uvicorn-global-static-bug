# Running uvicorn from python with class attribute in *different* file (*with* reload / workers)
Commands ran:
```
uvicorn main:app --host 127.0.0.1 --port 8000
```
```
uvicorn main:app --host 127.0.0.1 --port 8000 --workers 4
```
```
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
Result:
```
changed
INFO:     Started server process [77605]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
changed
INFO:     127.0.0.1:61926 - "GET /test HTTP/1.1" 200 OK
changed
INFO:     127.0.0.1:61929 - "GET /test HTTP/1.1" 200 OK
```
