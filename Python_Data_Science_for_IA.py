import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook

output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
    
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

csv_path = links["GDP"]
data_frame_GDP = pd.read_csv(csv_path)

data_frame_GDP.head()

x = data_frame_GDP["date"].unique()
gdp_change = data_frame_GDP["change-current"].unique()

print("\n")
print(data_frame_GDP.head())

csv_path = links["unemployment"]
data_frame_unemployment = pd.read_csv(csv_path)

data_frame_unemployment.head()
unemployment = data_frame_unemployment ["unemployment"].unique()

print("\n")
print(data_frame_unemployment.head())

y = data_frame_unemployment[data_frame_unemployment["unemployment"]>8.5]

print("\n")
print(y)


title = "Análisis de datos económicos de EE. UU"
file_name = "index.html"
print("\n")
make_dashboard(x,gdp_change,unemployment,title,file_name)
