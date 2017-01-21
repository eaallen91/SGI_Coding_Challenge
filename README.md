# SGI_Coding_Challenge
Github repostitory for SGI Coding Challenge #1<br />
<br />

Built with Python 2.7.1<br />
No special packages are required, everything is done with base python<br />

<br />
Tested and verified using:<br />
Python 2.7.1<br />
<br />

Stats:<br />
1000000 rows of data<br />
Birth dates and death dates are randomly generated<br />

<strong>High-level:</strong>
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
<table>
 <tr>
  <th>1970</th>
  <th>1972</th>
  <th>1980</th>
  <th>1991</th>
 </tr>
 <tr>
  <td>+2</td>
  <td>-1</td>
  <td>+5</td>
  <td>-2</td>
 </tr>
 <tr>
  <td>2</td>
  <td>1</td>
  <td>6</td>
  <td>4</td>
 </tr>
</table>
1980 saw the most people alive
