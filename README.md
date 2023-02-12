 [![Python 3.10.6](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3106/)

# RNG Scrapper 

Cryptographically secure random number scrapper built utilizing Selenium library.

# Requirements

- [Selenium](https://www.selenium.dev/pt-br/documentation/) library

    pip install selenium
      
- [Random User Agents](https://pypi.org/project/random-user-agent/) library
 
    pip install random_user_agent
       
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) library
 
    pip install pycryptodomex
       
- To install all dependencies:

    ./install_dependencies.sh
       

# Execution

    python3 scrapper.py


# Notes

- The Selenium library requires the setup of environment variables, as also the download of a driver accordingly to version and browser utilized.
- That driver must be put in the directory setted by the environment variable before running the script, as well as changing it's value if necessary.
