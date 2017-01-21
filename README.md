# SGI_Coding_Challenge
Github repostitory for SGI Coding Challenge #1

Built with Python 2.7.1
No special packages are required, everything is done with base python

Tested and verified using:
Python 2.7.1

Stats:
1000000 rows of data
Birth dates and death dates are randomly generated

High-level:
Create a dictionary using dates as the key values. If a person is born in a given year, increment the value associated with that key. If a person dies during a given year, decrement the value associated with that key. Then loop through the final list and add the values for each given year. <br />
<br />
EXAMPLE:<br />
1970,2<br />
1972,-1<br />
1980,5<br />
1991,-2<br />
<br />
1970 nets 2 people alive (more people born this year than died)<br />
1972 nets 1 person dead (more people died this year than born)<br />
1980 nets 5 people alive<br />
1991 nets 2 people dead<br />
<br />
1970 1972 1980 1991<br />
+2   -1   +5   -2<br />
 2    1    6    3 <br />
<br />
1980 saw the most people alive
