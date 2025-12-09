# Task Group 1: Data Analysis Tasks

## Steps to Complete Task Group 1

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_1/task_1b/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install testing dependencies: `python -m pip install pytest` (use `python -m pip` instead of `pip` directly, as `pip` may not be in PATH)
   - *Note for macOS/Apple users: If you encounter issues, you may need to install Python via Homebrew (`brew install python3`) or use `python3` instead of `python`*

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required function

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_1b/` directory)
   - Ensure all tests pass




Below is the deeper explanation of 
# GAIA-b — British Museum Mollusk Shell & Bead Age (Data Analysis Task)

## Task Overview

Analyze a CSV of mollusk bead research articles to find the minimum age of beads made from a specific species' shells. The species is linked to a British Museum object.

Find the minimum "at least" age (in thousands of years) from 2021 *Science Advances* articles about that species.

## Files and Structure

```
.
├─ README.md                # This file
├─ data/
│  └─ mollusk_bead_articles.csv
├─ src/
│  └─ solution.py           # Implement your solution here
└─ tests/
   └─ test_solution.py      # Automated tests
```

### data/mollusk_bead_articles.csv

CSV with columns: `museum_number`, `accepted_species_name`, `journal`, `publication_year`, `min_age_thousand_years_at_least`, etc.

## What You Need to Implement

Implement in `src/solution.py`:

```python
def find_min_bead_age(csv_path: str = "data/mollusk_bead_articles.csv") -> int:
    """
    Find the minimum 'at least' age (in thousands of years) of beads made from the mollusk species
    linked to British Museum object '2012,5015.17', as reported in 2021 Science Advances articles.
    """
    ...
```

## Input / Output

- **Input:** CSV path (default: "data/mollusk_bead_articles.csv")
- **Output:** Integer of the minimum age.

## Constraints

- Python 3, standard library only.
- Do not modify CSV or test files.

## Evaluation

Tests check the correct minimum age is returned.

## Hints

- Use `csv` module.
- Find species from museum_number "2012,5015.17".
- Filter by species, journal "Science Advances", year 2021.
- Find min of `min_age_thousand_years_at_least`.

---

# Görev Grubu 1: Veri Analizi Görevleri

## Görev Grubu 1'i Tamamlama Adımları

1. Python'u Yükleyin
   - Python 3.6+ sürümünü [python.org](https://www.python.org/downloads/) adresinden indirip yükleyin
   - Kurulumu doğrulayın: `python --version`
   - pip'in mevcut olduğundan emin olun: `pip --version`
     - Değilse, `python get-pip.py` (bootstrap.pypa.io'dan indirin) veya `python -m ensurepip --upgrade` ile yükleyin

2. Proje ortamını kurun
   - Görev dizinine gidin: `cd task_group_1/task_1b/`
   - (İsteğe bağlı) İzolasyon için sanal ortam oluşturun: `python -m venv venv` ardından aktif edin
   - Test bağımlılıklarını yükleyin: `python -m pip install pytest` (PATH'te olmayabileceğinden `pip` yerine `python -m pip` kullanın)

3. Çözümü uygulayın
   - Aşağıdaki görev açıklamasını okuyun
   - Gerekli fonksiyonu uygulamak için `src/solution.py` dosyasını düzenleyin

4. Çözümü çalıştırın ve doğrulayın
   - Testleri çalıştırın: `python -m pytest` (`task_1b/` dizininden)
   - Tüm testlerin geçtiğinden emin olun

# GAIA-b — British Museum Mollusk Kabuğu & Boncuk Yaşı (Veri Analizi Görevi)

## Görev Özeti

Belirli bir türün kabuklarından yapılmış boncukların minimum yaşını bulmak için mollusk boncuk araştırma makalelerinin bulunduğu bir CSV dosyasını analiz edin. Tür, bir British Museum nesnesine bağlıdır.

British Museum "2012,5015.17" nesnesiyle ilişkili türle ilgili 2021 *Science Advances* makalelerinden "en az" minimum yaşı (bin yıl cinsinden) bulun.

## Dosyalar ve Yapı

```
.
├─ README.md                # Bu dosya
├─ data/
│  └─ mollusk_bead_articles.csv
├─ src/
│  └─ solution.py           # Çözümünüzü buraya uygulayın
└─ tests/
   └─ test_solution.py      # Otomatik testler
```

### data/mollusk_bead_articles.csv

Sütunları içeren CSV: `museum_number`, `accepted_species_name`, `journal`, `publication_year`, `min_age_thousand_years_at_least`, vb.

## Uygulamanız Gerekenler

`src/solution.py` dosyasında uygulayın:

```python
def find_min_bead_age(csv_path: str = "data/mollusk_bead_articles.csv") -> int:
    """
    British Museum nesnesi '2012,5015.17' ile ilişkili mollusk türünden yapılmış boncukların
    2021 Science Advances makalelerinde bildirilen minimum 'en az' yaşını (bin yıl cinsinden) bulun.
    """
    ...
```

## Girdi / Çıktı

- **Girdi:** CSV dosya yolu (varsayılan: "data/mollusk_bead_articles.csv")
- **Çıktı:** Minimum yaşın tam sayı değeri.

## Kısıtlamalar

- Python 3, sadece standart kütüphane.
- CSV veya test dosyalarını değiştirmeyin.

## Değerlendirme

Testler doğru minimum yaşın döndürüldüğünü kontrol eder.

## İpuçları

- `csv` modülünü kullanın.
- museum_number "2012,5015.17" den türü bulun.
- Türe, "Science Advances" dergisine ve 2021 yılına göre filtreleyin.
- `min_age_thousand_years_at_least` değerinin minimumunu bulun.