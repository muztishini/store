from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import psycopg2


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost/store"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

class Base(DeclarativeBase): pass


class Product(Base):
	__tablename__ = 'product'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(200), nullable=False)
	racks = relationship("Rack", backref="rack")
	orders = relationship("Order", backref="order")


class Order(Base):
	__tablename__ = 'order'

	id = Column(Integer, primary_key=True, index=True)
	num_order = Column(Integer, nullable=False)
	product_id = Column(Integer, ForeignKey('product.id'))
	quantity = Column(Integer, nullable=False)


class Rack(Base):
	__tablename__ = 'rack'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(100), nullable=False)
	product_id = Column(Integer, ForeignKey('product.id'))
	quantity = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)
print("База данных и таблица созданы")
