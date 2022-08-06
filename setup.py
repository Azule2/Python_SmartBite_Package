from setuptools import setup

def readme():
    with open('README.md') as f:
        return  f.read()


setup(name='mydemo',
      version='0.0.1',
      description = 'Easy Python Demo',
      long_description = readme(),
      url='https://github.com/Azule2/Python_SmartBite_Package',
      author='Azule',
      author_email= 'smartbite0@gmail.com',
      zip_safe=False


      )