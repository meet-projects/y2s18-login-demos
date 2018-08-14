from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, password):
	"""
	Add a user to the DB.
	"""
	user_object = User(
		username=username,
		password=password)
	session.add(user_object)
	session.commit()

def query_by_name(username):
	"""
	Find the first user in the DB, by their
	username.
	"""
	user = session.query(User).filter_by(
		username=username).first()
	return user