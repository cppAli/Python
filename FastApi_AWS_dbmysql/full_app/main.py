from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Конфигурация базы данных
DATABASE_URL = "mysql+mysqlconnector://admin:Romanko1488@db-fastapi-aws.cd42w2ayogur.eu-west-3.rds.amazonaws.com/db_demo"

# Создание двигателя SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель данных
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String(255), nullable=True)

# Создание таблицы
Base.metadata.create_all(bind=engine)

# Создание приложения FastAPI
app = FastAPI()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Схемы данных для запросов и ответов
from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    age: int
    position: Optional[str] = None

class EmployeeUpdate(BaseModel):
    age: Optional[int] = None
    position: Optional[str] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    position: Optional[str]

    class Config:
        orm_mode = True

# Создание новых сотрудников
@app.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(name=employee.name, age=employee.age, position=employee.position)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Получение списка сотрудников
@app.get("/employees/", response_model=List[EmployeeResponse])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees

# Получение сотрудника по ID
@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Обновление данных сотрудника
@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    if employee.age is not None:
        db_employee.age = employee.age
    if employee.position is not None:
        db_employee.position = employee.position
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Удаление сотрудника
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"detail": "Employee deleted"}

# Запуск сервера: python -m uvicorn full_app.main:app --reload