<a><img src="https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width="200" align="center"></a>

<h1>Analyzing US Economic Data and  Building a Dashboard  </h1>
<h2>Description</h2>


Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some essential economic indicators from some data, you will then display these economic indicators in a Dashboard. You can then share the dashboard via an URL.

<p>
<a href="https://en.wikipedia.org/wiki/Gross_domestic_product"> Gross domestic product (GDP)</a> is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this lab, you will examine how changes in GDP impact the unemployment rate. You will take screen shots of every step, you will share the notebook and the URL pointing to the dashboard.</p>


<h2>Table of Contents</h2>
<div class="alert alert-block alert-info" style="margin-top: 20px">
    <ul>
        <li><a href="#Section_1"> Define a Function that Makes a Dashboard </a></li>
    <li><a href="#Section_2">Question 1: Create a dataframe that contains the GDP data and display it</a> </li>
    <li><a href="#Section_3">Question 2: Create a dataframe that contains the unemployment data and display it</a></li>
    <li><a href="#Section_4">Question 3: Display a dataframe where unemployment was greater than 8.5%</a></li>
    <li><a href="#Section_5">Question 4: Use the function make_dashboard to make a dashboard</a></li>
        <li><a href="#Section_6"><b>(Optional not marked)</b> Save the dashboard on IBM cloud and display it</a></li>
    </ul>
<p>
    Estimated Time Needed: <strong>180 min</strong></p>
</div>


<hr>


<h2 id="Section_1"> Define Function that Makes a Dashboard  </h2>

We will import the following libraries.


```python
import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()
```



<div class="bk-root">
    <a href="https://bokeh.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
    <span id="1005">Loading BokehJS ...</span>
</div>





In this section, we define the function <code>make_dashboard</code>. 
You don't have to know how the function works, you should only care about the inputs. The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. If you do not know what an html file is don't worry everything you need to know will be provided in the lab. 


```python
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend_label="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend_label="% unemployed")
    show(p)
```

The dictionary  <code>links</code> contain the CSV files with all the data. The value for the key <code>GDP</code> is the file that contains the GDP data. The value for the key <code>unemployment</code> contains the unemployment data.


```python
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
```

<h3 id="Section_2"> Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.

<b>Hint: <code>links["GDP"]</code> contains the path or name of the file.</b>

Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.


```python
csv_path = links["GDP"]
dataFrame = pd.read_csv(csv_path)
dataFrame.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>level-current</th>
      <th>level-chained</th>
      <th>change-current</th>
      <th>change-chained</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1948</td>
      <td>274.8</td>
      <td>2020.0</td>
      <td>-0.7</td>
      <td>-0.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>272.8</td>
      <td>2008.9</td>
      <td>10.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1950</td>
      <td>300.2</td>
      <td>2184.0</td>
      <td>15.7</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1951</td>
      <td>347.3</td>
      <td>2360.0</td>
      <td>5.9</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1952</td>
      <td>367.7</td>
      <td>2456.1</td>
      <td>6.0</td>
      <td>4.7</td>
    </tr>
  </tbody>
</table>

</div>



<h3 id="Section_2"> Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. </h3>

Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.

Use the method <code>head()</code> to display the first five rows of the GDP data, then take a screen-shot.


```python
csv_path = links["unemployment"]
dataFrame2 = pd.read_csv(csv_path)
dataFrame2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>unemployment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1948</td>
      <td>3.750000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>6.050000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1950</td>
      <td>5.208333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1951</td>
      <td>3.283333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1952</td>
      <td>3.025000</td>
    </tr>
  </tbody>
</table>

</div>



<h3 id="Section_3">Question 3: Display a dataframe where unemployment was greater than 8.5%. Take a screen-shot.</h3>


```python
dataFrameTemp = dataFrame2[dataFrame2["unemployment"]>8.5]

dataFrameTemp.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>unemployment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>1982</td>
      <td>9.708333</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1983</td>
      <td>9.600000</td>
    </tr>
    <tr>
      <th>61</th>
      <td>2009</td>
      <td>9.283333</td>
    </tr>
    <tr>
      <th>62</th>
      <td>2010</td>
      <td>9.608333</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2011</td>
      <td>8.933333</td>
    </tr>
  </tbody>
</table>

</div>



<h3 id="Section_4">Question 4: Use the function make_dashboard to make a dashboard</h3>

In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.

Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.


```python
x =  dataFrame["date"].unique()
```

Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.


```python
gdp_change = dataFrame["change-current"].unique()
```

Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.


```python
unemployment = dataFrame2["unemployment"].unique()
```

Give your dashboard a string title, and assign it to the variable <code>title</code>


```python
title = "US Economic Data Analysis"
```

Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.


```python
file_name = "index.html"
```

Call the function <code>make_dashboard</code> , to produce a dashboard.  Assign the parameter values accordingly take a the <b>, take a screen shot of the dashboard and submit it</b>.


```python
make_dashboard(x, gdp_change, unemployment, title, file_name)
```

    BokehUserWarning: ColumnDataSource's columns must be of the same length. Current lengths: ('x', 69), ('y', 51)
    BokehUserWarning: ColumnDataSource's columns must be of the same length. Current lengths: ('x', 69), ('y', 67)









<div class="bk-root" id="3fed2135-1665-47b0-8df7-84bd7a696703" data-root-id="2467"></div>





<hr>
<p>Copyright &copy; 2019 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>


<h2>About the Authors:</h2> 

<a href="https://www.linkedin.com/in/joseph-s-50398b136/">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

<p>
Other contributors: <a href="https://www.linkedin.com/in/yi-leng-yao-84451275/">Yi leng Yao</a>, <a href="www.linkedin.com/in/jiahui-mavis-zhou-a4537814a">Mavis Zhou</a> 
</p>


<h2>References :</h2> 

<ul>
 <il>
     1) <a href="https://research.stlouisfed.org/">Economic Research at the St. Louis Fed </a>:<a href="https://fred.stlouisfed.org/series/UNRATE/"> Civilian Unemployment Rate</a>
   </il>   
    <p>
     <il>
    2) <a href="https://github.com/datasets">Data Packaged Core Datasets
       </a>
   </il> 
    </p>


</ul>
</div>

### Posted By: Víctor Lavalle

*Project for the Course: *Python for Data Science and AI*
