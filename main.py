def berechne_leistung(spannung, strom):
    return spannung * strom


spannung = 230
strom = 5

leistung = berechne_leistung(spannung, strom)

print(f"Spannung: {spannung} V")
print(f"Strom: {strom} A")
print(f"Leistung: {leistung} W")