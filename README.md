# Kalkulator Kosztów Paliwa

Prosty i wydajny program z interfejsem wiersza poleceń (CLI) napisany w języku Python. Narzędzie służy do szybkiego obliczania całkowitego kosztu tankowania. Projekt demonstruje dobre praktyki inżynierii oprogramowania: separację logiki biznesowej od interfejsu użytkownika, testy jednostkowe oraz automatyzację za pomocą GitHub Actions.

**Autor:** Rafał Pokorny (Uniwersytet WSB Merito Wrocław)

## Wymagania wstępne

Aby uruchomić projekt lokalnie, potrzebujesz:
* **Python** w wersji 3.12 lub nowszej.
* Narzędzia **Git** (do sklonowania repozytorium).
* Terminala (np. PowerShell, CMD, Bash).

## Instalacja i uruchomienie (Quick Start)

### 1. Pobranie repozytorium
Skopiuj kod na swój komputer lokalny i przejdź do folderu z projektem:
```bash
git clone https://github.com/Humble72/Program-Python.git
cd Program-Python
```

### 2. Utworzenie wirtualnego środowiska
Zaleca się izolację zależności projektu za pomocą `venv`:
* **Windows (PowerShell):** `py -m venv .venv` lub `python -m venv .venv`
* **Linux / macOS:** `python3 -m venv .venv`

### 3. Aktywacja środowiska
* **Windows (PowerShell):** `.\.venv\Scripts\activate` 
  *(Jeśli napotkasz błąd uprawnień, uruchom najpierw: `Set-ExecutionPolicy Bypass -Scope Process`)*
* **Linux / macOS:** `source .venv/bin/activate`

### 4. Instalacja zależności
Po aktywacji środowiska zainstaluj wymagane pakiety (`pytest`, `black`, `pylint`):
```bash
pip install -r requirements.txt
```

## Przykłady użycia

Program obsługuje dwa wymagane parametry: 
* `-l` lub `--liters` (ilość zatankowanego paliwa w litrach)
* `-p` lub `--price` (cena za jeden litr w PLN)

**Przykład 1: Standardowe obliczenie kosztu tankowania (np. 50 litrów po 6.55 PLN/l):**
```bash
python cli.py -l 50 -p 6.55
# Wynik: Całkowity koszt: 327.50 PLN
```

**Przykład 2: Zabezpieczenie przed błędnymi danymi (wartości ujemne):**

```bash
python cli.py -l -10 -p 6.55
# Wynik: Błąd: Ilość litrów i cena nie mogą być ujemne.
```

## Jakość kodu i Testy (Lokalnie)

Projekt zawiera zestaw narzędzi dbających o czystość kodu. Zanim wyślesz zmiany na serwer, możesz uruchomić je na swoim komputerze (wymaga aktywnego środowiska `.venv`):

**Uruchomienie testów jednostkowych (pytest):**
```bash
pytest
```

**Formatowanie kodu (Black):**
```bash
black cli.py logic/ tests/
```

**Analiza statyczna (Pylint):**
```bash
pylint cli.py logic/ tests/
```
*(Dla systemów Linux/macOS przygotowano również gotowe skrypty pomocnicze w folderze `scripts/`).*

## Struktura projektu

* `cli.py` - Główny punkt wejścia, obsługuje interfejs wiersza poleceń i parsowanie argumentów.
* `logic/calculator.py` - Czysta logika biznesowa i algorytmy obliczeniowe.
* `tests/test_calculator.py` - Scenariusze testowe weryfikujące poprawność obliczeń i obsługę błędów.
* `requirements.txt` - Lista zewnętrznych bibliotek i ich wersji.
* `.github/workflows/ci.yml` - Konfiguracja potoku automatyzacji CI.

## Automatyzacja CI (Continuous Integration)

Repozytorium wykorzystuje **GitHub Actions**. Przy każdym wypchnięciu kodu (`push`) na gałęzie `main` oraz `develop`, serwer automatycznie wykonuje następujące kroki:

1. Konfiguruje środowisko Python 3.12.
2. Weryfikuje formatowanie (`black --check`).
3. Ocenia kod pod kątem dobrych praktyk (`pylint`).
4. Uruchamia wszystkie testy jednostkowe (`pytest`).