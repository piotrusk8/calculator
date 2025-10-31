# 🧮 Calculator  

# 🧠 Wybrane zagadnienia z inżynierii oprogramowania

Projekt zaliczeniowy z laboratoriów *Wybrane zagadnienia z inżynierii oprogramowania* – AGH  
Autor: **Piotr K. (@piotrusk8)**  
Data: **październik 2025**

---

## 📘 Opis
Prosty kalkulator w Pythonie z czterema podstawowymi operacjami:
- Dodawanie (sum)
- Odejmowanie (sub)
- Mnoenie (mul)
- Dzielenie (div) — z obsug bdu *dzielenia przez zero*

---

## 🧪 Testy
Testy jednostkowe napisane w **pytest**  
Pokrycie kodu: **100%**

Uruchomienie testów:
\\\ash
pytest --cov=. --cov-report=term-missing
\\\

Generowanie raportu HTML:
\\\ash
coverage html
\\\

---

## 📁 Struktura projektu
\\\
calculator.py         # Implementacja klasy
test_calculator.py    # Testy jednostkowe
.gitignore
.coverage
htmlcov/
\\\

---

## 🏁 Uruchomienie kalkulatora
\\\ash
python calculator.py
\\\

