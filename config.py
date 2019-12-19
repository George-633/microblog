class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/flaskblog?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'lssgeorge633fromdlbj'