test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}
new={i:j for i,j in test_dict.items() if i!="Mani"}
print(new)