# Date Calculator

## **Description**

>***This application requires Python 3.9.6 to run properly and also assume the user is using Ubuntu***

This is a CLI application implemented in Python using only primitives, built-in language functions and no external pip dependencies. The application accepts input from stdin. User can also execute "userInput.py" to enter date in a cli prompt, this application also validate input.

This application calculate the distance in whole days between two dates, counting only the days in between those dates, i.e. 01/01/2001 to 03/01/2001 yields “1”. The valid date range is between 01/01/1900 and 31/12/2999, all other dates should be rejected.

Testing data sets are followed:

- 2/6/1983 to 22/6/1983&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;19 days
- 4/7/1984 to 25/12/1984&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;173 days
- 1/3/1989 to 3/8/1983&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2036 days

***

## **File Structure**

| File           | Description                                             |
| -------------- | ------------------------------------------------------- |
| datediff.py    | function module                                         |
| test.py        | test file                                               |
| userInput.py   | interation cli prompt with error handling               |
| datetimelib.py | another sample using python's built-in datetime library |

## **Calculation Logic**

The application will calculate each date entry against the most initial date which is 00/00/000, convert two date entry as days and then return differenciate value by substracting the two. while also put leap years into consideration. 

>e.g. if a year is leap year, add 1 day to total days 

The application will always using the bigger number (later in the timeline) minus the smaller number (ealier in the timeline) to output the final days between the two dates. 

## **Instruction**
### Step one: install Python 3.6.9
- Update apt: `sudo apt update`

- Enter the following to install the required packages for Python:
```
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```
- Download Python 3.9.6, optimise installation

```
cd /tmp
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
tar –xf Python-3.9.6.tgz
cd python-3.9.6
./configure ––enable–optimizations
```
- Install Python 3.9.6 recommend using `altinstall` rather than `install`

```
sudo make altinstall or sudo make install
```

### Step two: clone the repo
clone the repo to your prefered location
```
git clone https://github.com/Lutecial/datecalculator.git
```
### Step three: using the application

>you might want to `chmod +x` on datediff.py, datetimelib.py, test.py and userInput.py just for convience sake

- run `./test.py` to see the data sets test against the application
- run `./userInput.py` for interactive cli prompt to type in two dates for calculation(the application will close automatically after display the result.)
- open datediff.py to see the source code for calculation
- run `./datetimelib.py` to validate the result if you are interested (no error validation on this one)




