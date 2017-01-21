# SGI_Coding_Challenge
Github repostitory for SGI Coding Challenge #1<br />
<br />

Built with Python 2.7.1<br />
No special packages are required, everything is done with base python<br />

<br />
Tested and verified using:<br />
Python 2.7.1<br />
<br />

<strong>How it was set up: </strong><br />
1) names.txt contain 800 random names obtained from the social security administration page (top 200 for 2 decades male and female) <br />
2) generate_data.py generates 1 million rows using random first and last names, and random birth and death year (death year must be after birth year)<br />
3) coding_challenge.py will read in the datafile containing 1 million rows and calculate which year saw the most people alive<br />
<br />

<strong>Assumptions:</strong><br />
1000000 rows of data<br />
Birth dates and death dates are randomly generated<br />
The data only contains people who were born and died between 1900 and 2000<br />
    -"Given a list of people with their birth and end years (all between 1900 and 2000)"<br />
<br />

<strong>High-level:</strong><br />
Create a dictionary using dates as the key values. If a person is born in a given year, increment the value associated with that key. If a person dies during a given year, decrement the value associated with that key. Then loop through the final list and add the values for each given year. <br />
<br />

<strong>Low-level Example:</strong><br />
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
1970 nets 0 people alive or dead (same amount of people born and died this year) <br />
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
  <td>0</td>
  <td>-2</td>
  <td>-1</td>
 </tr>
 <tr>
  <td>1</td>
  <td>3</td>
  <td>4</td>
  <td>3</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
 </tr>
</table>
1945 saw the most people alive<br />
<br />

<strong>RESULTS FROM COMMAND LINE EXECUTION:</strong><br />
eric@super-machine ~/git $ python generateData.py <br />
Please input how many rows of data you would like: 1000000<br />
Data file has been created successfully! datafile.csv<br />
<br />
eric@super-machine ~/git $ python coding_challenge.py<br /> 
There were the most people alive in the year 1962 at 364155<br />
