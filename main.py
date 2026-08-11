from fastapi import FastAPI
from routers.student_router import router as student_router
from routers.professor_router import router as professor_router
from routers.course_router import router as course_router
from routers.selection_router import router as selection_router
app = FastAPI()

app.include_router(student_router)
app.include_router(professor_router)
app.include_router(course_router)
app.include_router(selection_router)

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}