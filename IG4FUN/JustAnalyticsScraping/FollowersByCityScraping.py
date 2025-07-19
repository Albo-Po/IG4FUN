import pandas as pd

filepath = "SampleData.txt"
with open(filepath) as f:
    text_data = f.read()
    print(text_data)
    citiesData = text_data.split("%")
    print(citiesData)
    citiesData = [x.strip() for x in citiesData]
    citiesData = [x.split("\n") for x in citiesData if len(x) > 0]
    print(citiesData)
    df = pd.DataFrame()
    df["City"] = [x[0].split(",")[0] for x in citiesData if len(x[0].split(",")) > 0]
    print(df["City"])
    df["Region"] = [x[0].split(",")[1].strip() for x in citiesData if len(x[0].split(",")) > 1]
    print(df["Region"])
    df["Followers"] = [int(x[1]) for x in citiesData]
    print(df["Followers"])
    df["% Followers"] = [float(x[2].replace(",", ".")) for x in citiesData]
    print(df["% Followers"])
    df.to_excel("FollowersByCity.xlsx", index=False)

