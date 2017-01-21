# SGI_Coding_Challenge
Github repostitory for SGI Coding Challenge #1<br />
<br />

Built with Python 2.7.6<br />
Writtin on Linux Mint 17.3 Rosa<br />
No special packages are required, everything is done with base python<br />

<br />
Tested and verified using:<br />
Python 2.7.6<br />
Python 3.4.3<br />
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
YEAR | NET CHANGE | TOTAL<br />
1900 | 9920 | 9920<br />
1901 | 9601 | 19521<br />
1902 | 9664 | 29185<br />
1903 | 9510 | 38695<br />
1904 | 9584 | 48279<br />
1905 | 9451 | 57730<br />
1906 | 9436 | 67166<br />
1907 | 9138 | 76304<br />
1908 | 9216 | 85520<br />
1909 | 8954 | 94474<br />
1910 | 8840 | 103314<br />
1911 | 8740 | 112054<br />
1912 | 8632 | 120686<br />
1913 | 8492 | 129178<br />
1914 | 8143 | 137321<br />
1915 | 8279 | 145600<br />
1916 | 8215 | 153815<br />
1917 | 8030 | 161845<br />
1918 | 7961 | 169806<br />
1919 | 7659 | 177465<br />
1920 | 7600 | 185065<br />
1921 | 7385 | 192450<br />
1922 | 7263 | 199713<br />
1923 | 7162 | 206875<br />
1924 | 7111 | 213986<br />
1925 | 6990 | 220976<br />
1926 | 6826 | 227802<br />
1927 | 6628 | 234430<br />
1928 | 6588 | 241018<br />
1929 | 6451 | 247469<br />
1930 | 6039 | 253508<br />
1931 | 6362 | 259870<br />
1932 | 6136 | 266006<br />
1933 | 6018 | 272024<br />
1934 | 5477 | 277501<br />
1935 | 5542 | 283043<br />
1936 | 5297 | 288340<br />
1937 | 5175 | 293515<br />
1938 | 5231 | 298746<br />
1939 | 5095 | 303841<br />
1940 | 4786 | 308627<br />
1941 | 4591 | 313218<br />
1942 | 4213 | 317431<br />
1943 | 4140 | 321571<br />
1944 | 4061 | 325632<br />
1945 | 3757 | 329389<br />
1946 | 3556 | 332945<br />
1947 | 3375 | 336320<br />
1948 | 3533 | 339853<br />
1949 | 3071 | 342924<br />
1950 | 3040 | 345964<br />
1951 | 2802 | 348766<br />
1952 | 2491 | 351257<br />
1953 | 2141 | 353398<br />
1954 | 2383 | 355781<br />
1955 | 1874 | 357655<br />
1956 | 1604 | 359259<br />
1957 | 1315 | 360574<br />
1958 | 1173 | 361747<br />
1959 | 1121 | 362868<br />
1960 | 538 | 363406<br />
1961 | 359 | 363765<br />
1962 | 390 | 364155<br />
1963 | -261 | 363894<br />
1964 | -324 | 363570<br />
1965 | -516 | 363054<br />
1966 | -1160 | 361894<br />
1967 | -1323 | 360571<br />
1968 | -1423 | 359148<br />
1969 | -1959 | 357189<br />
1970 | -2262 | 354927<br />
1971 | -2363 | 352564<br />
1972 | -2886 | 349678<br />
1973 | -3325 | 346353<br />
1974 | -3503 | 342850<br />
1975 | -4252 | 338598<br />
1976 | -4226 | 334372<br />
1977 | -4857 | 329515<br />
1978 | -5626 | 323889<br />
1979 | -5782 | 318107<br />
1980 | -6571 | 311536<br />
1981 | -6958 | 304578<br />
1982 | -7509 | 297069<br />
1983 | -8160 | 288909<br />
1984 | -8689 | 280220<br />
1985 | -9302 | 270918<br />
1986 | -10067 | 260851<br />
1987 | -10818 | 250033<br />
1988 | -11846 | 238187<br />
1989 | -12420 | 225767<br />
1990 | -13419 | 212348<br />
1991 | -14824 | 197524<br />
1992 | -15745 | 181779<br />
1993 | -17439 | 164340<br />
1994 | -18996 | 145344<br />
1995 | -20927 | 124417<br />
1996 | -23329 | 101088<br />
1997 | -27238 | 73850<br />
1998 | -31696 | 42154<br />
1999 | -42154 | 0<br />
There were the most people alive in the year 1962 at 364155<br />
