from sqlalchemy import BigInteger, Column, Date, Numeric, String, UniqueConstraint
from db.base import Base

__all__ = ["Stock"]


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, index=True)
    last = Column(Numeric(precision=10, scale=2), nullable=False)
    high = Column(Numeric(precision=10, scale=2), nullable=False)
    low = Column(Numeric(precision=10, scale=2), nullable=False)
    change = Column(Numeric(precision=10, scale=2), nullable=False)
    change_pct = Column(String(length=10), nullable=False)
    volume = Column(String(length=10), nullable=False)
    country = Column(String(length=50), nullable=False, default="United States", index=True)
    currency = Column(String(length=10), nullable=False, default="USD", index=True)
    date = Column(Date, nullable=False, index=True)
    url = Column(String(length=255), nullable=False)

    __table_args__ = (
        UniqueConstraint('name', 'date', name='_name_time_uc'),
    )

    def __str__(self):
        return "<Stock(name='%s' date='%s' last='%s%s')>" % (
            self.name,
            self.date,
            self.last,
            self.currency,
        )
