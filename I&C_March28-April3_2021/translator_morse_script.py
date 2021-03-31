translator = {"A":"·-", "J":"·---", "S":"···", "B":"-···", "K":"-·-", "T":"-", "C":"-·-·", "L":"·-··",
"U":"··-", "D":"-··", "M":"--", "V":"···-", "E":"·", "N":"-·", "W":"·--", "F":"··-·", "O":"---", "X":"-··-", "G":"--·",
"P":"·--·", "Y":"-·--", "H":"····", "Q":"--·-",
"Z":"--··", "I":"··", "R":"·-·"}

message = input("Please enter the message to convert to Morse: ")

for i in message:
    if i in translator:
        print(translator[i],end= " ")
    else:
        print(i,end= " ")
