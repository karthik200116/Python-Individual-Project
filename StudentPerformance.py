import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(r'C:\Users\Aishwarya Iyer\Downloads')
df=pd.DataFrame({'Student_Names':list(data['Math 30 Class Marks']), 'Student_ID': list(data['Unnamed: 1']),'Assignment_1': list(data['Unnamed: 2']),
                 'Assignment_2':list(data['Unnamed: 4']), 'Assignment_3':list(data['Unnamed: 6']), 'Midterm_Exam': list(data['Unnamed: 8']),
                 'Final_Exam': list(data['Unnamed: 10']),'Final_Marks':list(data['Unnamed: 12'])})
df=df.drop([0,1,2,29,30,31])
df=df.fillna('0')
cvt = {'Student_Names':str,'Student_ID':int,'Assignment_1':int,'Assignment_2':int,'Assignment_3':int,'Midterm_Exam': int, 'Final_Exam':int}
df=df.astype(cvt)  #the datatypes are object, so changing it to string and integer
df1=df
df1=df1.sort_values(by='Assignment_1', ascending=True) #sorting
df2=df
df2=df2.sort_values(by='Assignment_2', ascending=True)
df3=df
df3=df3.sort_values(by='Assignment_3', ascending=True)
df1.head(5) #to find students who have scored lowest in first subject
df2.head(5) #to find students who have scored lowest in second subject
df3.head(5) #to find students who have scored lowest in third subject

def first():
	xx = np.arange(26)
	plt.figure(figsize=(15,5))
	plt.bar(xx+0.00,df['Midterm_Exam'],color='r', width=0.2, label="Midterm Exam")
	plt.bar(xx+0.25,df['Final_Exam'],color='b', width=0.2, label="Final Exam")
	plt.xticks(xx,df['Student_ID'])
	plt.xlabel('Student ID',fontsize=20)
	plt.ylabel('Marks scored',fontsize=20)
	plt.title("Comparison of Mid-Term and Final Exam Marks", fontsize=25)
	plt.legend(fontsize=20,loc=(1.01,0.4))
	plt.show()
first()

def second():
	yy=np.arange(26)
	plt.figure(figsize=(17,5))
	plt.bar(yy+0.00,df['Assignment_1'],color='r', width=0.2, label="Marks in Assignment 1")
	plt.bar(yy+0.25,df['Assignment_2'],color='b', width=0.2, label='Marks in Assignment 2')
	plt.bar(yy+0.50,df['Assignment_3'],color='g', width=0.2, label='Marks in Assignment 3')
	plt.xticks(yy,df['Student_ID'])
	plt.xlabel('Student ID', fontsize=20)
	plt.ylabel('Marks Scored', fontsize=20)
	plt.legend(fontsize=20, loc=(1.01,0.4))
	plt.title("Comparison Of Marks Of The Three Assignments", fontsize=25)
	plt.show()
second()
