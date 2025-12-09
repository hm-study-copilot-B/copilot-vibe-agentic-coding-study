# Task Group 1: Data Analysis Tasks

## Steps to Complete Task Group 1

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_1/task_1a/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install testing dependencies: `python -m pip install pytest` (use `python -m pip` instead of `pip` directly, as `pip` may not be in PATH)

3. Implement the solution
   - Read `task_1a/README.md` for details
   - Edit `task_1a/src/solution.py` to implement the required function

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_1a/` directory)
   - Ensure all tests pass

# GAIA-a – Invasive Species Research (Data Analysis Task)

## Task Overview

Analyze a CSV of USGS invasive species records for a pet fish from *Finding Nemo*. Find all unique 5-digit ZIP codes where this fish was observed as nonnative before 2020. Do not use web access or external APIs.

## Files and Structure

```
.
├─ README.md                # This file
├─ data/
│  └─ usgs_nemo_observations.csv
├─ src/
│  └─ solution.py           # Implement your solution here
└─ tests/
   └─ test_solution.py      # Automated tests
```

### data/usgs_nemo_observations.csv

CSV with columns: `species_common_name`, `data_source`, `observation_year`, `zip_code`, etc. Inspect header for exact names.

## What You Need to Implement

Implement in `src/solution.py`:

```python
from typing import List

def find_nonnative_zip_codes(csv_path: str = "data/usgs_nemo_observations.csv") -> List[str]:
    """
    Return unique 5-digit ZIP codes where the Nemo fish (clownfish) was observed as nonnative by USGS before 2020.
    Filter: data_source == "USGS", observation_year < 2020, species contains "clownfish" (case-insensitive).
    Return sorted list of strings.
    """
    ...
```

## Input / Output

- **Input:** CSV path (default: "data/usgs_nemo_observations.csv")
- **Output:** List[str] of unique ZIP codes, sorted ascending.

Example: ["33040", "60601", "96701", "96706", "96734"]

## Constraints

- Python 3, standard library only.
- Do not modify CSV or test files.

## Evaluation

Tests check correct filtering, unique/sorted ZIP codes, and match expected results.

## Hints

- Use `csv` module.
- Lowercase for species matching.
- ZIP codes as strings to preserve leading zeros.
- Use `set` for uniqueness, then sort.

---

# Görev Grubu 1: Veri Analizi Görevleri

## Görev Grubu 1'i Tamamlama Adımları

1. Python'u Yükleyin
   - Python 3.6+ sürümünü [python.org](https://www.python.org/downloads/) adresinden indirip yükleyin
   - Kurulumu doğrulayın: `python --version`
   - pip'in mevcut olduğundan emin olun: `pip --version`
     - Değilse, `python get-pip.py` (bootstrap.pypa.io'dan indirin) veya `python -m ensurepip --upgrade` ile yükleyin

2. Proje ortamını kurun
   - Görev dizinine gidin: `cd task_group_1/task_1a/`
   - (İsteğe bağlı) İzolasyon için sanal ortam oluşturun: `python -m venv venv` ardından aktif edin
   - Test bağımlılıklarını yükleyin: `python -m pip install pytest` (PATH'te olmayabileceğinden `pip` yerine `python -m pip` kullanın)

3. Çözümü uygulayın
   - Detaylar için `task_1a/README.md` dosyasını okuyun
   - Gerekli fonksiyonu uygulamak için `task_1a/src/solution.py` dosyasını düzenleyin

4. Çözümü çalıştırın ve doğrulayın
   - Testleri çalıştırın: `python -m pytest` (`task_1a/` dizininden)
   - Tüm testlerin geçtiğinden emin olun

# GAIA-a – İstilacı Tür Araştırması (Veri Analizi Görevi)

## Görev Özeti

*Finding Nemo* filminden bir evcil balık için USGS istilacı tür kayıtlarının bulunduğu bir CSV dosyasını analiz edin. Bu balığın 2020'den önce yerli olmayan tür olarak gözlemlendiği tüm benzersiz 5 haneli posta kodlarını bulun. Web erişimi veya harici API kullanmayın.

## Dosyalar ve Yapı

```
.
├─ README.md                # Bu dosya
├─ data/
│  └─ usgs_nemo_observations.csv
├─ src/
│  └─ solution.py           # Çözümünüzü buraya uygulayın
└─ tests/
   └─ test_solution.py      # Otomatik testler
```

### data/usgs_nemo_observations.csv

Sütunları içeren CSV: `species_common_name`, `data_source`, `observation_year`, `zip_code`, vb. Tam isimler için başlığı inceleyin.

## Uygulamanız Gerekenler

`src/solution.py` dosyasında uygulayın:

```python
from typing import List

def find_nonnative_zip_codes(csv_path: str = "data/usgs_nemo_observations.csv") -> List[str]:
    """
    Nemo balığının (palyaço balığı) 2020'den önce USGS tarafından yerli olmayan tür olarak 
    gözlemlendiği benzersiz 5 haneli posta kodlarını döndürün.
    Filtre: data_source == "USGS", observation_year < 2020, tür adında "clownfish" içerir (büyük/küçük harf duyarsız).
    Sıralanmış string listesi döndürün.
    """
    ...
```

## Girdi / Çıktı

- **Girdi:** CSV dosya yolu (varsayılan: "data/usgs_nemo_observations.csv")
- **Çıktı:** Artan sırada sıralanmış benzersiz posta kodlarının List[str] listesi.

Örnek: ["33040", "60601", "96701", "96706", "96734"]

## Kısıtlamalar

- Python 3, sadece standart kütüphane.
- CSV veya test dosyalarını değiştirmeyin.

## Değerlendirme

Testler doğru filtreleme, benzersiz/sıralı posta kodları ve beklenen sonuçlarla eşleşmeyi kontrol eder.

## İpuçları

- `csv` modülünü kullanın.
- Tür eşleştirmesi için küçük harf kullanın.
- Başta sıfırları korumak için posta kodlarını string olarak tutun.
- Benzersizlik için `set` kullanın, sonra sıralayın.