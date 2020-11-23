# FRC2021-Vision
FRC 2473's CV code for 2021

# Project Organization
All Python code shall follow [PEP8 Style](https://www.python.org/dev/peps/pep-0008/)
- One file per Python class
- Import classes like `from depth_data_generator import DepthDataGenerator`

Each team will commit to one development branch. Team branches shall merge to master once a week. This implies that your code should be working and tested by the end of week cut-off time.

# Environment Setup
For this year we will be using Python 3.8.1. Install Python from the [official website](https://www.python.org/downloads/release/python-381/). For Windows, make sure to check the option to add Python to your PATH and increase the PATH length limit.

Once the installer completes, open up a terminal (On Mac, use Terminal.app and on Windows, use CMD or Powershell). Run `python3 --version` to check the installation was succesful.

We will be managing Python dependencies with [pipenv](https://pypi.org/project/pipenv/). You can run `pip3 install --user pipenv` to install pipenv for the first time. Then just run `pipenv install` to fetch all the Python packages for our code. Then use `pipenv run python3` to run code under the pipenv environment.

Current dependency list:
* [Python 3.8.1](https://www.python.org/downloads/release/python-381/)
  * [numpy](https://docs.scipy.org/doc/numpy/reference/)
  * [scipy](https://docs.scipy.org/doc/scipy/reference/)
  * [matplotlib](https://matplotlib.org/api/index.html)
  * [OpenCV](https://docs.opencv.org/master/)
  * [serial](https://pyserial.readthedocs.io/en/latest/shortintro.html)
  * [imageio](https://imageio.github.io/)