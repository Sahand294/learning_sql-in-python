from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

varieble = create_engine("postgresql://postgres:sahand91@127.0.0.1/archemy")
# engine = create_engine("sqlite:///example.db")
baseclass = declarative_base()
session = sessionmaker(bind=varieble)
session2 = session()
from idk import User
new_user = User(name='sahand',email='examples.com',age=12,mobile='iphone')
session2.add(new_user)
session2.commit()