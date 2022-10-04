# py_ftn.py
  
import pandas as pd
def py_read_flights(file):
  flights = pd.read_csv(file)
  flights = flights[flights['dest'] == "LAX"]
  flights = flights[['carrier', 'dep_delay', 'arr_delay']]
  flights = flights.dropna()
  return flights

def py_read_iris(file):
  data = pd.read_csv(file)
  data = data[data['SP'] == "vc"]
  return data


def  py_desc(data) :
     data = pd.DataFrame(data)
     desc = data.describe()
     return desc

from sklearn.linear_model import LinearRegression
py_reg = LinearRegression()


