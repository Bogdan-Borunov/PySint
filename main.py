import tkinter as tk
from tkinter import ttk
from functions import RunOsint

root = tk.Tk()
root.title("PySint")
root.geometry("620x800")
root.configure(bg="#0b0d0a")
root.resizable(False, False)

Search = tk.BooleanVar(value=False)
Inc = tk.BooleanVar(value=False)
SafeMode = tk.BooleanVar(value=True)

SearchEngine = tk.StringVar(value="Google")
SearchType = tk.StringVar(value="Веб")
TargetType = tk.StringVar(value="Автоопределение")
SourceType = tk.StringVar(value="Все источники")

Language = tk.StringVar(value="Авто")
Region = tk.StringVar(value="Не ограничивать")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Dark.TCombobox",
    fieldbackground="#171a15",
    background="#171a15",
    foreground="#50C900",
    bordercolor="#30352e",
    lightcolor="#30352e",
    darkcolor="#30352e",
    arrowcolor="#50C900",
    padding=7
)

style.map(
    "Dark.TCombobox",
    fieldbackground=[
        ("readonly", "#171a15"),
        ("focus", "#171a15"),
        ("active", "#171a15")
    ],
    foreground=[
        ("readonly", "#50C900"),
        ("focus", "#50C900"),
        ("active", "#50C900")
    ],
    selectbackground=[
        ("readonly", "#171a15"),
        ("focus", "#171a15"),
        ("active", "#171a15")
    ],
    selectforeground=[
        ("readonly", "#50C900"),
        ("focus", "#50C900"),
        ("active", "#50C900")
    ],
    bordercolor=[
        ("focus", "#30352e"),
        ("!focus", "#30352e")
    ],
    lightcolor=[
        ("focus", "#30352e"),
        ("!focus", "#30352e")
    ],
    darkcolor=[
        ("focus", "#30352e"),
        ("!focus", "#30352e")
    ]
)

def make_section(parent, x, y, width, height):
    frame = tk.Frame(
        parent,
        bg="#11140f",
        highlightbackground="#252b22",
        highlightthickness=1
    )

    frame.place(
        x=x,
        y=y,
        width=width,
        height=height
    )

    return frame

def make_label(parent, text, x, y, size=11):
    label = tk.Label(
        parent,
        text=text,
        fg="#50C900",
        bg="#0b0d0a",
        font=("Arial", size, "bold")
    )

    label.place(
        x=x,
        y=y
    )

    return label

def make_field_label(parent, text, x, y):
    label = tk.Label(
        parent,
        text=text,
        fg="#899083",
        bg="#11140f",
        font=("Arial", 9, "bold")
    )

    label.place(
        x=x,
        y=y
    )

    return label

def make_combobox(parent, variable, values, x, y, width=250):
    combo = ttk.Combobox(
        parent,
        textvariable=variable,
        values=values,
        state="readonly",
        style="Dark.TCombobox"
    )

    combo.place(
        x=x,
        y=y,
        width=width
    )

    def on_selected(event=None):
        root.after_idle(root.focus_set)

        try:
            combo.selection_clear()
        except tk.TclError:
            pass

    combo.bind(
        "<<ComboboxSelected>>",
        on_selected
    )

    return combo

def create_checkbutton(parent, text, variable, x, y):
    check = tk.Checkbutton(
        parent,
        text=text,
        variable=variable,
        bg="#11140f",
        fg="#50C900",
        activebackground="#11140f",
        activeforeground="#50C900",
        selectcolor="#1b2118",
        borderwidth=0,
        highlightthickness=0,
        font=("Arial", 9, "bold")
    )

    check.place(
        x=x,
        y=y
    )

    return check

def run():
    query = Input.get().strip()

    if not query:
        status.config(
            text="● ВВЕДИТЕ ЗАПРОС",
            fg="#d6b329"
        )

        Input.focus_set()
        return

    exact_search = Search.get()
    Incognitoo = Inc.get()
    SMode = SafeMode.get()

    search_type = SearchType.get()
    Search_Engine = SearchEngine.get()
    target_type = TargetType.get()
    source_type = SourceType.get()
    language = Language.get()
    region = Region.get()

    status.config(
        text="● ЗАПУСК SELENIUM...",
        fg="#50C900"
    )

    print("\n" + "=" * 60)
    print("PySint")
    print("=" * 60)

    print("Запрос:", query)
    print("Точный поиск:", exact_search)
    print("Инкогнито:", Incognitoo)
    print("SafeSearch:", SMode)
    print("Тип поиска:", search_type)
    print("Поисковая система:", Search_Engine)
    print("Тип цели:", target_type)
    print("Источник:", source_type)
    print("Язык:", language)
    print("Регион:", region)

    print("=" * 60)

    try:
        RunOsint(
            query,
            exact_search,
            Incognitoo,
            SMode,
            search_type,
            Search_Engine,
            target_type,
            source_type,
            language,
            region
        )

        status.config(
            text="● БРАУЗЕР ЗАПУЩЕН",
            fg="#50C900"
        )

    except Exception as error:
        status.config(
            text="● ОШИБКА",
            fg="#d64040"
        )

        print("Ошибка:", error)

logo = tk.Label(
    root,
    text="PySint",
    font=("Arial", 40, "bold"),
    fg="#50C900",
    bg="#0b0d0a"
)

logo.place(
    x=25,
    y=20
)

make_label(
    root,
    "Основной запрос",
    25,
    110,
    12
)

Input = tk.Entry(
    root,
    bg="#171a15",
    fg="#50C900",
    insertbackground="#50C900",
    selectbackground="#345b22",
    selectforeground="white",
    relief="flat",
    font=("Arial", 14, "bold")
)

Input.place(
    x=25,
    y=138,
    width=570,
    height=42
)

quick = make_section(
    root,
    25,
    195,
    570,
    120
)

tk.Label(
    quick,
    text="БЫСТРЫЕ ПАРАМЕТРЫ",
    fg="#50C900",
    bg="#11140f",
    font=("Arial", 9, "bold")
).place(
    x=15,
    y=10
)

create_checkbutton(
    quick,
    "Точный поиск",
    Search,
    15,
    38
)

create_checkbutton(
    quick,
    "Режим инкогнито",
    Inc,
    180,
    38
)

create_checkbutton(
    quick,
    "SafeSearch",
    SafeMode,
    370,
    38
)

advanced = make_section(
    root,
    25,
    330,
    570,
    300
)

tk.Label(
    advanced,
    text="ПАРАМЕТРЫ ПОИСКА",
    fg="#50C900",
    bg="#11140f",
    font=("Arial", 9, "bold")
).place(
    x=15,
    y=10
)

make_field_label(
    advanced,
    "Поисковая система",
    15,
    42
)

make_combobox(
    advanced,
    SearchEngine,
    [
        "Google",
        "Bing",
        "DuckDuckGo"
    ],
    15,
    64
)

make_field_label(
    advanced,
    "Тип поиска",
    290,
    42
)

make_combobox(
    advanced,
    SearchType,
    [
        "Веб",
        "Новости",
        "Изображения",
        "Видео"
    ],
    290,
    64
)

make_field_label(
    advanced,
    "Тип цели",
    15,
    105
)

make_combobox(
    advanced,
    TargetType,
    [
        "Автоопределение",
        "Username",
        "E-mail",
        "Телефон",
        "Домен",
        "IP-адрес",
        "URL",
        "Имя"
    ],
    15,
    127
)

make_field_label(
    advanced,
    "Источник",
    290,
    105
)

make_combobox(
    advanced,
    SourceType,
    [
        "Все источники",
        "GitHub",
        "Reddit",
        "YouTube",
        "Scratch",
        "LinkedIn",
        "Wikipedia"
    ],
    290,
    127
)

make_field_label(
    advanced,
    "Язык",
    15,
    168
)

make_combobox(
    advanced,
    Language,
    [
        "Авто",
        "Русский",
        "English",
        "Deutsch",
        "Français",
        "Español"
    ],
    15,
    190
)

make_field_label(
    advanced,
    "Регион",
    290,
    168
)

make_combobox(
    advanced,
    Region,
    [
        "Не ограничивать",
        "Россия",
        "США",
        "Великобритания",
        "Германия",
        "Франция",
        "Европа"
    ],
    290,
    190
)

status = tk.Label(
    root,
    text="● ГОТОВ К РАБОТЕ",
    fg="#50C900",
    bg="#0b0d0a",
    font=("Arial", 9, "bold")
)

status.place(
    x=25,
    y=650
)

RunButton = tk.Button(
    root,
    text="ЗАПУСК ▶",
    command=run,
    bg="#50C900",
    fg="#081006",
    activebackground="#69ef20",
    activeforeground="#081006",
    relief="flat",
    bd=0,
    font=("Arial", 13, "bold"),
    cursor="hand2"
)

RunButton.place(
    x=25,
    y=690,
    width=570,
    height=55
)

footer = tk.Label(
    root,
    text="PySint • Selenium Search",
    fg="#454c40",
    bg="#0b0d0a",
    font=("Arial", 8)
)

footer.place(
    x=25,
    y=760
)

root.mainloop()