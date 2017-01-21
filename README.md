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

<strong>High-level:</strong><br />
Create a dictionary using dates as the key values. If a person is born in a given year, increment the value associated with that key. If a person dies during a given year, decrement the value associated with that key. Then loop through the final list and add the values for each given year. <br />
<br />
EXAMPLE:<br />
sample_data.csv<br />
Smith,Joe,             1920,1991<br />
Jefferson,Karen,       1920,1950<br />
Man,Hugh,              1945,1998<br />
Coholic,Al,            1970,1991<br />
Smithers,Waylon,       1903,1970<br />

<br />
1903 nets 1 person alive (more people born this year than died)<br />
1920 nets 2 people alive<br />
1945 nets 1 person alive<br />
1950 nets 1 person dead(more people died this year than born)<br />
1970 nets 1 person dead<br />
1991 nets 2 people dead<br />
1998 nets 1 person dead<br />
<br />
<table>
 <tr>
  <th>1903</th>
  <th>1920</th>
  <th>1945</th>
  <th>1950</th>
  <th>1970</th>
  <th>1991</th>
  <th>1998</th>
 </tr>
 <tr>
  <td>+1</td>
  <td>+2</td>
  <td>+1</td>
  <td>-1</td>
  <td>-2</td>
  <td>-1</td>
 </tr>
 <tr>
  <td>1</td>
  <td>3</td>
  <td>4</td>
  <td>3</td>
  <td>1</td>
  <td>0</td>
 </tr>
</table>
1945 saw the most people alive
