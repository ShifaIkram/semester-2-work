# E-cat Aggregate Calculator

# Taking Information from the user
matric_OM = int(input("Enter marks obtained in Matric:"))
matric_TM = int(input("Enter total marks in matric:"))

fsc_OM = int(input("Enter marks obtained in FS-c(I):"))
fsc_TM = int(input("Enter total marks in FS-c(I):"))

ecat_OM = int(input("Enter marks obtained in E-cat:"))
ecat_TM = int(input("Enter total marks in E-cat:"))

# Percentages Calculation
matric = (matric_OM / matric_TM)*100
fsc = (fsc_OM / fsc_TM)*100
ecat = (ecat_OM / ecat_TM)*100

# Aggregate Calculation
aggregate = (matric*0.17) + (fsc*0.50) + (ecat*0.33)

# OUTPUT
print("-------- E-cat Aggregate--------")
print(aggregate)
