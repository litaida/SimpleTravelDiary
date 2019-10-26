# 数据库模型
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

from utils.sqlopt import Base


class TravelLocation(Base):
    """旅行日记 - 地图标注页"""
    __tablename__ = 'travel_location'
    province = Column(String(10), primary_key=True)
    longitude = Column(Float())
    latitude = Column(Float())
    note = Column(String(30), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=None, nullable=True)
    # is_deleted = Column(Boolean, default=0)


if __name__ == '__main__':
    Base.metadata.create_all()
