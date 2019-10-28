# 数据库模型
from traceback import format_exc
from datetime import datetime

from sqlalchemy import Column, String, DateTime

from utils.sqlopt import Base, SessionPool


class TravelLocation(Base):
    """旅行日记 - 地图标注页"""
    __tablename__ = 'travel_location'
    province = Column(String(10), primary_key=True)
    note = Column(String(128), nullable=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=None, nullable=True)
    # is_deleted = Column(Boolean, default=0)

    @classmethod
    def get_all(cls):
        session = SessionPool()
        return session.query(cls).all()

    @classmethod
    def get_by_province(cls, province):
        session = SessionPool()
        return session.query(cls).filter_by(province=province).all()


def create_note(provice, note):
    """增"""
    session = SessionPool()
    try:
        session.add(TravelLocation(province=provice, note=note))
        session.commit()
    except:
        print(format_exc())
        session.rollback()
    finally:
        session.close()


def delete_note(province):
    """删"""
    session = SessionPool()
    try:
        row = session.query(TravelLocation).filter_by(province=province)
        if row:
            row = row[0]
            print('Deleting Row From TravelLocation: %s' % str(row))
            session.delete(row)
            session.commit()
        else:
            print('Province: %s does not exist, Affected 0 Row(s)' % province)
    except:
        print(format_exc())
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    Base.metadata.create_all()
