n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

students=[[1,"Amit",85],
          [2,"Rahul",90],
          [3,"Sneha",80]]
file=open("students.txt","w")
for student in students:
    file.write(str(student[0])+" "+student[1]+" "+str(student[2])+"\n")
file.close()
print("record stores successfully")  



import pandas as pd
data={"Roll No":[1,2,3,4],
      "Name":["Amit","Rahul",None,"Rohit"],
      "Marks":[80,None,75,90]
      }
df=pd.DataFrame(data)
print("before repeleacing a value:")
print(df)
print("Missing Value:")
print(df.isnull().sum())
df["Name"]=df["Name"].fillna("Unknown")
df["Marks"]=df["Marks"].fillna(0)
df_m=df
print("DataFrame After replacing missing value:")
print(df_m)

