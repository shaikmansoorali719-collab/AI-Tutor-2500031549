from fastapi import FastAPI

klu = FastAPI(title = "AI Tutor",
              description = "AI Tutor Pbl Project",
              version = "1.0.0")

@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor Project!"}

@klu.get("/demo")
def demo():
    return {"message" : "KL University"}

@klu.get("/askquestion")
def ask():
    return {"message" :"What is Llm", "Answer": "Large Language Model"}

@klu.get("/emp")
def emp():
    return {"id" : 1, "name" : "Ram" , "gender" : "Male", "course" : "DSA"}

@klu.get("/students")
def students():
    return [{"id" : 1, "name" : "Ram" , "gender" : "Male", "course" : "DSA"},
            {"id" : 2, "name" : "Shyam" , "gender" : "Male", "course" : "DSA"},
            {"id" : 3, "name" : "Sita" , "gender" : "Female", "course" : "DSA"}
    ]
