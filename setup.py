from setuptools import setup

setup(name='pylist',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.7.2', 'MarkupSafe','Flask-SQLAlchemy==0.16']
     )

BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
STATIC_PATH = os.path.join(BASE_DIR, 'static')
DATABASE_PATH = os.path.join(BASE_DIR, 'magedb.db')

DATABASES = {
    'default': {
        'NAME': DATABASE_PATH
    }
}