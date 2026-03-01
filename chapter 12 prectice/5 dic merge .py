#New operators | and |= allow for merging and updating dictionaries.
dict1={'a':45,'b':12,"c":45}
dict2={"d":78,"e":19}
#merging the both dictionaries 
dict3=dict1|dict2
print(dict3)