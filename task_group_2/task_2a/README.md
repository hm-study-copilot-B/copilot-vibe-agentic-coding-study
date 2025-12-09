# Task Group 2: SWE-inspired Tasks

## Steps to Complete Task Group 2

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_2/task_2a/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install dependencies: `python -m pip install matplotlib numpy`

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required functions

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_2a/` directory)
   - Or run the demo: `python src/demo.py`

---

# Task 2a: Fix CSV Parser Case Sensitivity Bug

## Objective

**This is a bug-fixing task.** A CSV configuration parser was implemented to read special commands from CSV files, but it incorrectly assumes all commands must be UPPERCASE. Real users create files by hand and use lowercase commands, causing the parser to crash.

## Issue Description

The `parse_csv_with_commands()` function reads CSV files that can contain special command lines starting with `#` (like `#SKIP 2` or `#DELIMITER tab`). However, the parser only recognizes UPPERCASE commands and crashes on lowercase ones.

### Example of the Problem

This file crashes:
```
#skip 2
#delimiter tab
Name	Value	Error
Alice	1.5	0.1
```

But this works fine:
```
#SKIP 2
#DELIMITER tab
Name	Value	Error
Alice	1.5	0.1
```

Since users create these files by hand, the parser should be case-insensitive like other tools.

## How to Reproduce

```python
from solution import parse_csv_with_commands

# This crashes with "Unrecognized command: #skip 2"
data = """#skip 2
#delimiter tab
Name	Value
Alice	1.5
Bob	2.3"""

result = parse_csv_with_commands(data)
```

## Your Task

**Fix the bug in `src/solution.py`** to make command parsing case-insensitive.

The parser currently checks commands like:
```python
if line.startswith('#SKIP'):
    # handle skip
elif line.startswith('#DELIMITER'):
    # handle delimiter
```

**Hint**: Convert the line to uppercase before checking, or use case-insensitive comparison.

### Expected Behavior

After fixing:
- `#SKIP 2`, `#skip 2`, `#Skip 2` should all work
- `#DELIMITER tab`, `#delimiter tab`, `#Delimiter tab` should all work
- The parser should handle mixed case in command names

## Files Structure

```
.
├─ README.md                # This file
├─ src/
│  ├─ solution.py           # FIX THE BUG HERE
│  └─ demo.py               # Demo script
└─ tests/
   └─ test_solution.py      # Tests
```

## Debugging Tips

1. Run the tests: `python -m pytest tests/ -v`
2. Try parsing files with lowercase commands
3. Check where command recognition happens
4. Use `.upper()` or `.lower()` for case-insensitive comparison

## Constraints

- Python 3, use matplotlib and numpy.
- Do not modify test files.

## Hints

- Use `matplotlib.animation.FuncAnimation` for animations.
- Implement easing functions for smooth transitions.
- Consider using numpy for interpolation between data states.

---

# Görev Grubu 2: Yazılım Mühendisliği Görevleri

## Görev Grubu 2'yi Tamamlama Adımları

1. Python'u Yükleyin
   - Python 3.6+ sürümünü [python.org](https://www.python.org/downloads/) adresinden indirip yükleyin
   - Kurulumu doğrulayın: `python --version`
   - pip'in mevcut olduğundan emin olun: `pip --version`
     - Değilse, `python get-pip.py` (bootstrap.pypa.io'dan indirin) veya `python -m ensurepip --upgrade` ile yükleyin

2. Proje ortamını kurun
   - Görev dizinine gidin: `cd task_group_2/task_2a/`
   - (İsteğe bağlı) İzolasyon için sanal ortam oluşturun: `python -m venv venv` ardından aktif edin
   - Bağımlılıkları yükleyin: `python -m pip install matplotlib numpy`

3. Çözümü uygulayın
   - Aşağıdaki görev açıklamasını okuyun
   - Gerekli fonksiyonları uygulamak için `src/solution.py` dosyasını düzenleyin

4. Çözümü çalıştırın ve doğrulayın
   - Testleri çalıştırın: `python -m pytest` (`task_2a/` dizininden)
   - Veya demoyu çalıştırın: `python src/demo.py`

---

# Görev 2a: CSV Ayrıştırıcı Büyük/Küçük Harf Duyarlılığı Hatasını Düzeltme

## Amaç

**Bu bir hata düzeltme görevidir.** CSV dosyalarından özel komutları okumak için bir CSV yapılandırma ayrıştırıcısı uygulandı, ancak tüm komutların BÜYÜK HARF olması gerektiğini varsayıyor. Gerçek kullanıcılar dosyaları elle oluşturuyor ve küçük harf komutlar kullanıyor, bu da ayrıştırıcının çökmesine neden oluyor.

## Sorun Açıklaması

`parse_csv_with_commands()` fonksiyonu, `#` ile başlayan özel komut satırları (`#SKIP 2` veya `#DELIMITER tab` gibi) içerebilen CSV dosyalarını okur. Ancak ayrıştırıcı yalnızca BÜYÜK HARF komutları tanır ve küçük harfli komutlarda çöker.

### Sorun Örneği

Bu dosya çöküyor:
```
#skip 2
#delimiter tab
Name	Value	Error
Alice	1.5	0.1
```

Ama bu düzgün çalışıyor:
```
#SKIP 2
#DELIMITER tab
Name	Value	Error
Alice	1.5	0.1
```

Kullanıcılar bu dosyaları elle oluşturduğundan, ayrıştırıcı diğer araçlar gibi büyük/küçük harf duyarsız olmalıdır.

## Nasıl Yeniden Üretilir

```python
from solution import parse_csv_with_commands

# Bu "Unrecognized command: #skip 2" hatası vererek çöker
data = """#skip 2
#delimiter tab
Name	Value
Alice	1.5
Bob	2.3"""

result = parse_csv_with_commands(data)
```

## Göreviniz

Komut ayrıştırmasını büyük/küçük harf duyarsız yapmak için **`src/solution.py` dosyasındaki hatayı düzeltin**.

Ayrıştırıcı şu anda komutları şöyle kontrol ediyor:
```python
if line.startswith('#SKIP'):
    # skip işle
elif line.startswith('#DELIMITER'):
    # delimiter işle
```

**İpucu**: Kontrol etmeden önce satırı büyük harfe dönüştürün veya büyük/küçük harf duyarsız karşılaştırma kullanın.

### Beklenen Davranış

Düzeltme sonrası:
- `#SKIP 2`, `#skip 2`, `#Skip 2` hepsi çalışmalı
- `#DELIMITER tab`, `#delimiter tab`, `#Delimiter tab` hepsi çalışmalı
- Ayrıştırıcı komut adlarında karışık büyük/küçük harfi desteklemeli

## Dosya Yapısı

```
.
├─ README.md                # Bu dosya
├─ src/
│  ├─ solution.py           # HATAYI BURADA DÜZELTİN
│  └─ demo.py               # Demo scripti
└─ tests/
   └─ test_solution.py      # Testler
```

## Hata Ayıklama İpuçları

1. Testleri çalıştırın: `python -m pytest tests/ -v`
2. Küçük harfli komutlarla dosyaları ayrıştırmayı deneyin
3. Komut tanımanın nerede gerçekleştiğini kontrol edin
4. Büyük/küçük harf duyarsız karşılaştırma için `.upper()` veya `.lower()` kullanın

## Kısıtlamalar

- Python 3, matplotlib ve numpy kullanın.
- Test dosyalarını değiştirmeyin.

## İpuçları

- Animasyonlar için `matplotlib.animation.FuncAnimation` kullanın.
- Yumuşak geçişler için kolaylaştırma fonksiyonları uygulayın.
- Veri durumları arasında interpolasyon için numpy kullanmayı düşünün.
