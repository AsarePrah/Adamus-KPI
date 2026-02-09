from typing import Optional, List, Dict, Any
from datetime import date as dt_date
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import JSON, Column

class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    department: str
    role: str = Field(default="User") # User, HOD, Admin
    leaves_used: int = Field(default=0)
    
    leave_requests: List["LeaveRequest"] = Relationship(back_populates="employee")

class LeaveRequest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employee.id")
    start_date: dt_date
    end_date: dt_date
    status: str = Field(default="Pending") # Pending, Approved, Rejected
    
    employee: Optional[Employee] = Relationship(back_populates="leave_requests")

class KPIRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    department: str = Field(index=True)
    subtype: Optional[str] = Field(default=None) # e.g. "ore", "grade"
    date: dt_date = Field(index=True)
    metric_name: str # e.g. "Gold Contained", "Recovery"
    
    # Store flexible numeric data: daily_actual, daily_forecast, var1, mtd_actual, etc.
    data: Dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))
