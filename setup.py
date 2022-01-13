from setuptools import setup

readme = ''
with open('README.md') as f:
    readme = f.read()   

setup(name='pscontroll',
      author='iFanpS',   
      url='https://github.com/iFanpSGTS/PSController_Module',
      project_urls={
        "Issue tracker": "https://github.com/iFanpSGTS/PSController_Module",
      },
      version=2.0,
      packages=['pscontroll'],
      license='MIT',
      description='GTPS Controller via Module',
      long_description=readme,
      long_description_content_type="text/plain",
      include_package_data=True,
      install_requires=['psutil', 'regex'],
      python_requires='>=3.5.3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
      ]
)