[[GUI Version](https://github.com/sorzkode/spassgui)]
[[MIT Licence](https://en.wikipedia.org/wiki/MIT_License)]


![alt text](https://raw.githubusercontent.com/sorzkode/spasscli/master/assets/splogo.png)

# Snazzy Pass CLI

A random password generator with a CLI.

![alt text](https://raw.githubusercontent.com/sorzkode/spasscli/master/assets/help.png)

## Example

![alt text](https://raw.githubusercontent.com/sorzkode/spasscli/master/assets/example.png)

## Installation

You can download from Github, changedir (cd) to the script directory and run the following:
```
pip install -e .
```
*This will install the snazzy pass package locally 

Installation isn't required to run the script but you will need to ensure the requirements below are met.

## Requirements

  [[Python 3](https://www.python.org/downloads/)]

  [[pyfiglet module](https://pypi.org/project/pyfiglet/)] 

  [[click module](https://pypi.org/project/click/)]

## Usage

```
Usage: spasscli.py [OPTIONS]

Options:
  -l, --length INTEGER   Set your overall password length.
  -s, --special INTEGER  Set the number of special characters.
  -n, --numbers INTEGER  How many numbers to include.

  --help                 Show this message and exit.
```
If snazzy pass is installed you can use the following command syntax:
```
python -m spasscli --help

python -m spasscli -l 15 -s 3 -n 2
python -m spasscli --length 15 --special 3 --numbers 2
```
Otherwise you can run the script directly by changing directory (cd) in a terminal of your choice to the spasscli directory and using the following syntax:
```
python spasscli.py --help

python spasscli.py -l 15 -s 3 -n 2
python spasscli.py --length 15 --special 3 --numbers 2
```




