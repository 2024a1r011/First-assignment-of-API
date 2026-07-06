from fastapi import FastAPI
app =FastAPI()

@app.get('/home')
def home():
    return {
        "message": "Welcome to my first FastAPI assignment"
    }
@app.get('/about')
def about():
    return {
        "student_name": "Vishavjeet Singh",
        "course": "FastAPI",
        "topic": "First API Assignment",
        "status": "Learning"
    }
@app.get('/trainer')
def trainer():
    return{
        "name": "Hemanth",
        "role": "Trainer",
        "subject": "FastAPI"
    }
@app.get('/courses')
def courses():
    return [
{
"id": 1,
"name": "Python Basics",
"duration": "1 week"
},
{
"id": 2,
"name": "FastAPI",
"duration": "2 weeks"
},
{
"id": 3,
"name": "SQL Basics",
"duration": "1 week"
    }]

@app.get('/students')
def students():
    return [
{
"id": 1,
"name": "Akhil",
"course": "Python",
"city": "Hyderabad"
},
{
"id": 2,
"name": "Sai",
"course": "FastAPI",
"city": "Vijayawada"
}
    ]
@app.get('/college')
def college():
    return {
"college_name": "Vishavjeet Singh",
"location": "Jammu",
"department": "Computer Science",
"current_module": "FastAPI Basics"}

@app.get("/technology")
def technology():
    return [
"Python",
"FastAPI",
"JSON",
"HTTP",
"REST API"
]

