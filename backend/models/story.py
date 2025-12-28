from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
#sqlalchemy itu library buat database, temasuk ORM (Object Relational Mapping)
#mirip gimana kita map settings dari variabel env ke dalam class
#FastAPI punya module kek sqlalchemy yang bisa map data ke dalam class
# jadi gk perlu nulis SQL code lagi
# SQL itu bahasa query database, buat interaksi ke database
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    #Column itu cuma bagian dari data yang akan di simpan di database untuk setiap individual story
    #primary key itu unik buat setiap row, jadi setiap story punya indentifier unik
    #index itu untuk optimize query, jadi kalo query by id, bisa cepet, buat nyari stories cepet

    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")