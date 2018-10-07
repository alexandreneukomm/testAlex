import pandas as pd
df = pd.DataFrame({"a":range(10), "b":range(10,20)})
with open("my_table.tex", "w") as f:
    f.write("\\begin{tabular}{" + " | ".join(["c"] * len(df.columns)) + "}\n")
    for i, row in df.iterrows():
        f.write("\\hline")
        f.write(" & ".join([str(x) for x in row.values]) + " \\\\\n")
        f.write("\\hline")
    f.write("\\end{tabular}")
print(df)