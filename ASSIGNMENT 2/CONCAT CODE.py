#OPTION 1
dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
dfML = pd.concat([df1ML, df2ML], ignore_index=True)

df = pd.concat([dfML, dfSE], axis=1)
print(df)
print("#########################################\n")
print("###############LINE BREAK################  ")
print("#########################################\n")
 

#OPTION 2
dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
dfML = pd.concat([df1ML, df2ML], ignore_index=True)

df1 = dfSE.merge(dfML, how='inner')
print(df1)
print("#########################################\n")
print("###############LINE BREAK################  ")
print("#########################################\n")

#OPTION 3
dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
dfML = pd.concat([df1ML, df2ML], ignore_index=True)

df2 = dfSE.merge(dfML, how='left')
print(df2)
print("#########################################\n")
print("###############LINE BREAK################  ")
print("#########################################\n")


#OPTION 4
dfSE = pd.concat([df1SE, df2SE], ignore_index=True)
dfML = pd.concat([df1ML, df2ML], ignore_index=True)

df3 = dfSE.merge(dfML, how='right')
print(df3)
