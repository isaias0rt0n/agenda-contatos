try:
    with open("emails.txt", "a") as arq:
        arq.write("dois@hotmail.com\n")
except Exception as error:
    print("Algum error ocorreu")
    print(error)