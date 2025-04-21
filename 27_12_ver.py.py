from tkinter import *
from tkinter import ttk
from tkinter import font
from random import *
import json

try:
    with open("viselica/words.json", "r", encoding="utf-8") as f:
        word_list = json.load(f)["word_list"]
except Exception as e:
    raise e
print(word_list)


def image(a):
    if a == 0:
        img["image"] = img_0
    elif a == 1:
        img["image"] = img_1
    elif a == 2:
        img["image"] = img_2
    elif a == 3:
        img["image"] = img_3
    elif a == 4:
        img["image"] = img_4
    elif a == 5:
        img["image"] = img_5
    elif a == 6:
        img["image"] = img_6
    else:
        img["image"] = img_7


def word_create():
    global word, wordlist, count, ugadalka
    word = choice(word_list)
    wordlist = list(word)
    ugadalka = ["_"] * len(wordlist)
    # новое слово в тексте
    wordtk["text"] = ugadalka
    # сброс фотки
    count = 0
    image(count)
    # print(word)


# count 10 -> win
# coun 7 -> lose
def knopka_do(bukva):
    global word, wordlist, count, ugadalka
    if len(wordlist) != 0:
        if len(bukva) == 1:
            if bukva.lower() in wordlist:
                for i in range(len(word)):
                    if wordlist[i] == bukva.lower():
                        ugadalka[i] = bukva.lower()
            else:
                count += 1
            wordtk["text"] = ugadalka
            if ugadalka == wordlist:
                count = 10
        else:
            count += 1
        if count == 7:
            game_status["text"] = "ПРОИГРЫШ"
        elif count == 10:
            game_status["text"] = "ПОБЕДА"
        else:
            game_status["text"] = ""
        # изображение
        if count < 7:
            image(count)
            game_status["text"] = ""
        elif count == 7:
            image(count)
            game_status["text"] = "СМЭРТЬ"
            wordtk["text"] = wordlist
        entry.delete(0, END)
        name_prov_button_and_start_new_game(count)
        # print(count)


def bukva_vvod_slovo():
    global word, wordlist, count, ugadalka
    if count == -1:
        word_create()
        prov_button["text"] = "Проверка"
    elif count == 10:
        count = 11
    else:
        bukva = entry.get()
        if bukva == word:
            ugadalka = wordlist
            wordtk["text"] = ugadalka
            count = 10
        else:
            count += 1
        if count == 7:
            game_status["text"] = "ПРОИГРЫШ"
        elif count == 10:
            game_status["text"] = "ПОБЕДА"
        else:
            game_status["text"] = ""
        # изображение
        if count < 7:
            image(count)
            game_status["text"] = ""
        elif count == 7:
            image(count)
            game_status["text"] = "СМЭРТЬ"
            wordtk["text"] = wordlist
        entry.delete(0, END)
    name_prov_button_and_start_new_game(count)
    # print(count)


# сдаться
def surrender():
    global word, wordlist, count, ugadalka
    if count != 10:
        count = 6
        knopka_do("")


def name_prov_button_and_start_new_game(a):
    if a == 7 or a == 10:
        prov_button["text"] = "Начать заново"
    elif a == 8 or a == 11:
        prov_button["text"] = "Проверка"
        word_create()
        game_status["text"] = ""


# создание буков
def button_maker(first_letter, row_1, column_1, colvo):
    for i in range(colvo):

        but = ttk.Button(
            text=f"{chr(ord(first_letter)+i)}",
            command=lambda x=chr(ord(first_letter) + i): knopka_do(f"{x}"),
        )
        but.place(y=i // 11 * 60, x=i % 11 * 50, width=50)


root = Tk()
root.title("Виселица")
root.geometry("1000x360+320+180")
# начальные парамаетры
count = -1
word = ""
wordlist = []
ugadalka = []
# фон
img_0 = PhotoImage(file="viselica/images/0.png")
img_1 = PhotoImage(file="viselica/images/1.png")
img_2 = PhotoImage(file="viselica/images/2.png")
img_3 = PhotoImage(file="viselica/images/3.png")
img_4 = PhotoImage(file="viselica/images/4.png")
img_5 = PhotoImage(file="viselica/images/5.png")
img_6 = PhotoImage(file="viselica/images/6.png")
img_7 = PhotoImage(file="viselica/images/7.png")

beliy_fon = ttk.Label(background="White")
beliy_fon.place(anchor=NW, x=0, y=0, width=1000, height=1000)
img = ttk.Label(image=img_0)
img.place(anchor=NW, x=650, y=0)

# style
frame = ttk.Frame(root)
style = ttk.Style(root)
font = font.Font(family="TkIconFont", size=25)
style.configure("TButton", font=font)

# слово
wordtk = ttk.Label(text="В И С Е Л И Ц А", font=("Arial", 25), background="White")
wordtk.place(anchor=CENTER, x=830, y=50)

# создание слова
wordlist = []

# Ввод слова
# vvod_text = ttk.Label(text="Ввод слова", style="TButton")
# vvod_text.place(anchor=CENTER, x=150, y=250)
entry = ttk.Entry(font=("Arial", 24))
entry.place(anchor=CENTER, x=150, y=300, width=206)
entry.insert(0, "Ввести слово")
# создание буков
button_maker("а", 1, 1, 32)
# кнопка Сдаться
restart_button = ttk.Button(text="Сдаться", style="TButton", command=surrender)
restart_button.place(anchor=CENTER, x=450, y=300)

# кнопка старта и проверки
prov_button = ttk.Button(text="Начать игру", style="TButton", command=bukva_vvod_slovo)
prov_button.place(anchor=CENTER, x=150, y=250)

# стаус игры
game_status = ttk.Label(text="", font=("Arial", 25), background="White")
game_status.place(anchor=CENTER, x=830, y=330)


root.mainloop()
