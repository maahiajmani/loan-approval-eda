 # Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Loading the dataset
df=pd.read_csv("C:\\Users\\MAAHI\\Downloads\\loan_approval_dataset.csv")
# Previewing the top rows
print(df.head())
 # Printing the column names
print(df.columns)
 #Removing the spaces from the column names
df.columns=df.columns.str.strip()
# Checking
print(df.columns)
 # Keeping only rows where cibil_score is between 300 and 900
df=df[df['cibil_score'].between(300,900)]
# Previewing again
print(df[['cibil_score','loan_status']].head())
 #Grouping the score range and loan status
approval_rate_cibil=df.groupby('cibil_score_range')['loan_status'].value_counts(normalize=True).unstack()
 # Only picking the approved column
approval=approval_rate_cibil[' Approved']
approval.plot(kind='bar',color='mediumseagreen',edgecolor='black')
plt.title('Loan Approval by CIBIL Score')
plt.xlabel('CIBIL Score Range')
plt.ylabel('Approval Rate')
plt.ylim(0,1)
plt.tight_layout()
plt.show()
# Approval rate by education level
approval_rate_edu=df.groupby('education')['loan_status'].value_counts(normalize=True).unstack()
approval_rate_edu.columns=approval_rate_edu.columns.str.strip()
print(approval_rate_edu)
# Plotting the bar graph
approval_edu=approval_rate_edu['Approved']
approval_edu.plot(kind='bar',color='teal',edgecolor='black')
plt.title('Loan Approval Rate by Education')
plt.xlabel('Education')
plt.ylabel('Approval Rate')
plt.ylim(0,1)
plt.tight_layout()
plt.show()
# Approval rate by Self-Employed Status
df['self_employed']=df['self_employed'].str.strip()
# Grouping and calculating approval rates
approval_rate_self=df.groupby('self_employed')['loan_status'].value_counts(normalize=True).unstack()
approval_rate_self.columns=approval_rate_self.columns.str.strip()
print(approval_rate_self)
approval_self=approval_rate_self[' Approved']
approval_self.plot(kind='bar',color='orange',edgecolor='black')
plt.title('Loan Approval Rate by Self Employment Status')
plt.xlabel('Self-Employed')
plt.ylabel('Approval Rate')
plt.ylim(0,1)
plt.tight_layout()
plt.show()