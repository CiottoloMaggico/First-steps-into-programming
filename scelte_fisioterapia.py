from json import load
import openpyxl

# Corso B: 29856
# Corso C: 29970
# Corso A: 29969
# Corso X: 29869
# Corso J: 29859
# Corso A F: 29981


scelte = {"29856": 0, "29970": 0, "29969": 0,
          "29859": 0, "29981": 0, "29869": 0}
document = openpyxl.load_workbook(
    "D:\\Documenti\\python testing\\algo\\graduatoria.xlsx")
sheet = document["Table 1"]
accoppiata = 0


for rows in range(2, 2658):
    cella = str(sheet.cell(row=rows, column=10).value)
    if len(cella) != 1:
        cella = cella.split(" ")[1:2]
        accoppiata += cella.count("29857")
    # scelte["29970"] += cella.count("29970")
    # scelte["29969"] += cella.count("29969")
    # scelte["29859"] += cella.count("29859")
    # scelte["29981"] += cella.count("29981")
    # scelte["29869"] += cella.count("29869")

print(accoppiata)
# print(f"Corso B: {scelte['29856']}\nCorso C: {scelte['29970']}\nCorso A: {scelte['29969']}\nCorso X: {scelte['29869']}\nCorso J: {scelte['29859']}\nCorso AF: {scelte['29981']}")
