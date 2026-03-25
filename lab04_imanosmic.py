# Ime: Iman Osmic
# Datum: 25.03.2025
# Lab 4 --- Python za FastAPI

student={"ime":"Amina","godina":3,"email":"ime.prezime@untz.ba"}

# pristup vrijednosti
print(student["ime"])  # "Amina"
print(student.get("gpa",0))  # 0 vraca default ako kljuc ne postoji

# dodavanje / izmjena
student["aktivan"]=True

# provjera postojanja kljuca
print("email" in student)  # True

# iteracija
for kljuc,vrijednost in student.items():
    print(kljuc,vrijednost)

# uklanjanje
del student["aktivan"]

studenti=[
    {"ime":"Amina","godina":3},
    {"ime":"Emir","godina":2},
]

# pristup prvom studentu
print(studenti[0]["ime"])  # "Amina"

# pocetni primjer --- nastavite sami
student={"ime":"Amina","godina":3,"email":"ime.prezime@untz.ba"}
# ... dodajte cetvrto polje, print rjecnika, dodajte novo polje "aktivan",
# napravite listu

# bez type hints radi, ali FastAPI ne moze koristiti
def greeting(name):
    return "Hello "+name

# sa type hints FastAPI moze validirati, dokumentirati, generisati shemu
def greeting_typed(name:str)->str:
    return f"Hello {name}"

# opci oblik potpisa funkcije
def function1(parameter1:type,parameter2:type=None)->type:
    pass

# primjeri type hints
name:str  # tekst
year:int  # cijeli broj
grade:float  # decimalni broj
active:bool  # True ili False
students:list  # lista
data:dict  # rjecnik
optional_year:int|None  # moze biti int ili None (opcionalno)