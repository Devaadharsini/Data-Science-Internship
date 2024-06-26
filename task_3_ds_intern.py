# -*- coding: utf-8 -*-
"""task_3_ds_intern.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vnk5ywSuiY0isOOdUBfXDS4qtpc-gdiF

*TASK 3*

*Build a decision tree classifier to predict whether a customer will purchase a product or service based on their demographic and behavioral data. Use a dataset such as the Bank Marketing dataset from the UCI Machine Learning Repository.*
"""

!pip install scikit-learn
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""**LOADED THE BANK MARKETING DATASET**"""

data=pd.read_csv('bank-full.csv')

data

"""**EXPLORATORY DATA ANALYSIS**"""

plt.figure(figsize=[15,8])
sns.barplot(data=data,x=data['job'], y=data['age'],hue=data['marital'],palette='gist_earth_r')
plt.title('Age Analysis based on Job and Marital status')
plt.show()

sns.barplot(x=data['contact'],y=data['previous'],hue=data['poutcome'],palette='twilight_shifted_r')
plt.title('Number of Previous Contacts by Communication Type and Campaign Outcome')
plt.show()

plt.figure(figsize=[14,5])
sns.barplot(x=data['contact'],y=data['campaign'],hue=data['poutcome'],palette='terrain')
plt.title('Frequency of Contacts performed during Campaign by Communication Type and Campaign Outcome')
plt.ylim(0.0,4.0)
plt.show()

plt.figure(figsize=[15,8])
sns.barplot(x=data['education'],y=data['balance'],hue=data['poutcome'],order=['primary','secondary','tertiary'],palette='summer')
plt.ylim(0,3000)
plt.title('Average of Yearly Bank Balance distribution by Education and Campaign Outcome')
plt.legend(loc='upper right')
plt.ylabel('balance in Euros ')
plt.plot()

"""**REQUIRED ATTRIBUTES**"""

data=data.drop(columns=['day','month','pdays'],axis=1)

data.head()

"""**SHAPE OF DATASET**"""

print('Shape of data:','\n')
data.shape

"""**INFO ABOUT DATASET**"""

print('Info of data:','\n')

data.info()

"""**DESCRIPTION OF DATASET**"""

print('description of data','\n')

data.describe()

"""**CONVERTING DATASET INTO DATAFRAME**"""

df=pd.DataFrame(data)

df.tail()

"""**SPLITTING INPUT VARIABLES AND TARGET VARIABLE**"""

x=df.drop('y',axis=1)

y=df['y']

x.head()

y.head()

"""**FINDING UNIQUE VALUES IN EACH CATEGORICAL VARIABLES**"""

print('JOB: ',x['job'].unique())

print('\n','marital status: ',x['marital'].unique())

print('\n','education: ',x['education'].unique())

print('\n','default: ',x['default'].unique())

print('\n','housing loan: ',x['housing'].unique())

print('\n','loan: ',x['loan'].unique())

print('\n','contact:',x['contact'].unique())

print('\n','campaign outcome: ',x['poutcome'].unique())

"""**MAPPING TEXT INTO NUMERIC**"""

job={'student':0,'services':1,'admin.':2,'technician':3,'blue-collar':4,'management':5,'entrepreneur':6,'unemployed':7,'retired':8,'self-employed':9,'housemaid':10,'unknown':11}
marital_status={'single':0,'married':1,'divorced':2}
education={'unknown':0,'primary':1,'secondary':2,'tertiary':3}
credit_in_default={'yes':1,'no':0}
housing_loan={'yes':1,'no':0}
personal_loan={'yes':1,'no':0}
contact_type={'unknown':0,'telephone':1,'cellular':2}
prev_campaign_result={'unknown':0,'success':1,'failure':2,'other':3}

x['job']=x['job'].map(job)

x['marital']=x['marital'].map(marital_status)

x['education']=x['education'].map(education)

x['default']=x['default'].map(credit_in_default)
x['housing']=x['housing'].map(housing_loan)
x['loan']=x['loan'].map(personal_loan)
x['contact']=x['contact'].map(contact_type)
x['poutcome']=x['poutcome'].map(prev_campaign_result)

"""**DATASET AFTER MAPPING**"""

x.tail()

y.map({'yes':1,'no':0})

"""**CORRELATION MATRIX**"""

correlation_matrix=x.corr()
correlation_matrix

"""**HEATMAP FOR CORRELATION MATRIX**"""

plt.figure(figsize=[12,7])

sns.heatmap(correlation_matrix,annot=True,cmap='Accent',linewidths=0.5)
plt.title('CORRELATION MATRIX of Input variables')
plt.show()

"""**FITTING DecisionTreeClassifier WITH MAX_DEPTH 16**"""

dt=DecisionTreeClassifier(max_depth=16,random_state=42)
dt.fit(x,y)

"""**ACCURACY : 0.96**"""

pred_x=dt.predict(x)

accuracy=accuracy_score(pred_x,y)
print(accuracy)

def mapping_data(age_d,job_map,ms_map,edu_map,credit_map,bank_balance,housing_map,loan_map,_contact_,duration_of_call,before_campaign,during_campaign,poutcome_map):
  return [
  x.age[age_d],
  job[job_map],
  marital_status[ms_map],
  education[edu_map],
  credit_in_default[credit_map],
  x.balance[bank_balance],
  housing_loan[housing_map],
  personal_loan[loan_map],
  contact_type[_contact_],
  x.duration[duration_of_call],
  x.previous[before_campaign],
  x.campaign[during_campaign],
  prev_campaign_result[poutcome_map]]

"""**PREDICTING WHETHER A CUSTOMER WILL PURCHASE A PRODUCT OR SERVICE USING UNSEEN DATA**"""

unseen_data=[mapping_data(79,'retired','divorced','secondary','yes',2500,'no','no','telephone',350,5,10,'success'),
mapping_data(28,'blue-collar','married','secondary','yes',900,'yes','yes','cellular',50,3,7,'failure')]

unseen_data_pred=dt.predict(unseen_data)
print(unseen_data_pred)

"""**EVALUATING MODEL PERFORMANCE USING METRICS**



"""

# Evaluate model performance

from sklearn.metrics import classification_report

y_pred = dt.predict(x)
cr=classification_report(y, y_pred,output_dict=True)
print(cr)

"""**CLASSIFICATION REPORT**"""

df_cr=pd.DataFrame(cr).transpose()
print(df_cr)

"""**HEATMAP FOR CLASSIFICATION REPORT**"""

plt.figure(figsize=(10, 6))
sns.heatmap(df_cr.iloc[:-1, :-1], annot=True, cmap='cubehelix', fmt='.2f')
plt.title('Heatmap for Classification Report')
plt.show()