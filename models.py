# 数据库模型
from datetime import datetime

from sqlalchemy import Column, String, DateTime

from utils.sqlopt import Base, SessionPool


session = SessionPool()


class TravelLocation(Base):
    """旅行日记 - 地图标注页"""
    __tablename__ = 'travel_location'
    province = Column(String(10), primary_key=True)
    note = Column(String(128), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=None, nullable=True)
    # is_deleted = Column(Boolean, default=0)

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_province(cls, province):
        return session.query(cls).filter_by(province=province).all()


if __name__ == '__main__':
    Base.metadata.create_all()
