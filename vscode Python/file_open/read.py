with open("C:/HIdaka ryo/Python/file_open/samplefile.txt","r",encoding="UTF-8")as f:
    data = f.read()
    data1 = f.readline()
    data2 = f.readlines()

print(f"READ DATA is [{data}]")
print(f"READ DATA is [{data1}]")
print(f"READ DATA is [{data2}]")