from backend.core.db import Base
from sqlalchemy import Column, Integer, String

class TestModel(Base):
    __tablename__ = "test_model"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    description: str = Column(String, nullable=True)
    location: str = Column(String, nullable=True)

    def __repr__(self):
        return f"<TestModel(id={self.id}, name={self.name}, description={self.description})>"