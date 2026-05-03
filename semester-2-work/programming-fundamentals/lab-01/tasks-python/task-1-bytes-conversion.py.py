# To Convert Bytes into MB and GB

# To take num of bytes from the user
bytes = float(input("Enter the number of bytes: "))

#Conversion
MB = bytes/(1024**2)                 # 1kB= 1024 bytes
GB = bytes/(1024**3)

# Output
print(" MegaBytes (MB): ",MB)
print(" GigaBytes (GB): ",GB)

















