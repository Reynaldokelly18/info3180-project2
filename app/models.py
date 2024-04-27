# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash

class Posts(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    caption = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    user_id = db.Column(db.Integer, unique=True)
    created_on = db.Column(db.DateTime)


    def __init__(self,caption,photo,user_id,created_on):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_on= created_on

class Likes(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, unique=True)
    
    def __init__(self,post_id,user_id):
        self.post_id = post_id
        self.user_id = user_id

class Follows(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    follower_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, unique=True)
    
    def __init__(self,follower_id,user_id):
        self.follower_id = follower_id
        self.user_id = user_id\

class Users(db.Model):
 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80), unique=True)
    biography = db.Column(db.String(80), unique=True)
    profile_photo = db.Column(db.String(80), unique=True)
    joined_on = db.Column(db.DateTime)


    def __init__(self,first_name,last_name,username,password,email,location,biography,profile_photo,joined_on):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password,method='pbkdf2:sha256')
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)