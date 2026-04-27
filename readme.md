# Task API (Flask)

Simple REST API to manage tasks using in-memory storage.

---

## 🚀 Run the project

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### 1. Get all tasks
**GET /tasks**

```bash
curl http://127.0.0.1:5000/tasks
```

---

### 2. Get task by ID
**GET /tasks/{id}**

```bash
curl http://127.0.0.1:5000/tasks/1
```

---

### 3. Create task
**POST /tasks**

```bash
curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"New Task","description":"Details"}'
```

---

### 4. Update task
**PUT /tasks/{id}**

```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \
-H "Content-Type: application/json" \
-d '{"title":"Updated Task","description":"Updated details"}'
```

---

### 5. Delete task
**DELETE /tasks/{id}**

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## Notes

- Requests must use:
  `Content-Type: application/json`
 
- Data is stored in memory (will reset when server restarts)
- API Will  return  standard HTTP status codes:
  - 200 OK
  - 201 Created
  - 204 No Content
  - 400 Bad Request
  - 404 Not Found