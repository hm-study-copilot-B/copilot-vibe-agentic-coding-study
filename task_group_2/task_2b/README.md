# Task Group 2: SWE-inspired Tasks

## Steps to Complete Task Group 2

1. Install Python
   - Download and install Python 3.6+ from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`
   - Ensure pip is available: `pip --version`
     - If not, install via `python get-pip.py` (download from bootstrap.pypa.io) or `python -m ensurepip --upgrade`

2. Set up the project environment
   - Navigate to the task directory: `cd task_group_2/task_2b/`
   - (Optional) Create a virtual environment for isolation: `python -m venv venv` then activate it
   - Install dependencies: `python -m pip install matplotlib numpy`

3. Implement the solution
   - Read the task description below
   - Edit `src/solution.py` to implement the required functions

4. Run and validate the solution
   - Execute tests: `python -m pytest` (from `task_2b/` directory)
   - Or run the demo: `python src/demo.py`

---

# Task 2b: Fix JSON Config Validation Bug

## Objective

**This is a bug-fixing task.** A configuration file validator was implemented to validate JSON config files against a schema, but it fails to validate boolean values correctly when they're represented as strings (like `"true"` or `"false"`). This causes valid config files to be rejected.

## Issue Description

The `validate_config()` function validates configuration files against a schema. The schema specifies expected types for each field. However, when boolean values are provided as strings (common in config files from environment variables or CLI), the validator incorrectly rejects them.

### Example of the Problem

This config is rejected but should be valid:
```json
{
  "debug": "true",
  "max_connections": "100",
  "timeout": "30.5"
}
```

Schema expects:
```json
{
  "debug": "bool",
  "max_connections": "int",
  "timeout": "float"
}
```

The validator should convert string representations to proper types, but currently it only handles `"int"` and `"float"`, not `"bool"`.

## How to Reproduce

```python
from solution import validate_config

schema = {
    "debug": "bool",
    "port": "int"
}

config = {
    "debug": "true",  # String "true" should convert to bool
    "port": "8080"    # String "8080" should convert to int
}

# This raises ValueError but should succeed
result = validate_config(config, schema)
```

## Your Task

**Fix the bug in `src/solution.py`** to handle boolean string conversion.

The validator currently has code for `int` and `float` conversion:
```python
if expected_type == 'int':
    value = int(value)
elif expected_type == 'float':
    value = float(value)
```

**Add support for `'bool'` type** that converts:
- `"true"`, `"True"`, `"TRUE"`, `"1"` → `True`
- `"false"`, `"False"`, `"FALSE"`, `"0"`, `""` → `False`

### Expected Behavior

After fixing:
- String `"true"` converts to boolean `True`
- String `"false"` converts to boolean `False`
- Case-insensitive: `"True"`, `"TRUE"` all work
- Numeric strings: `"1"` → `True`, `"0"` → `False`
- Empty string `""` → `False`

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
2. Check the type conversion section in `validate_config()`
3. Add a new `elif` clause for `expected_type == 'bool'`
4. Use `.lower()` for case-insensitive string comparison

---

# Görev Grubu 2: Yazılım Mühendisliği Görevleri

## Görev Grubu 2'yi Tamamlama Adımları

1. Python'u Yükleyin
   - Python 3.6+ sürümünü [python.org](https://www.python.org/downloads/) adresinden indirip yükleyin
   - Kurulumu doğrulayın: `python --version`
   - pip'in mevcut olduğundan emin olun: `pip --version`
     - Değilse, `python get-pip.py` (bootstrap.pypa.io'dan indirin) veya `python -m ensurepip --upgrade` ile yükleyin

2. Proje ortamını kurun
   - Görev dizinine gidin: `cd task_group_2/task_2b/`
   - (İsteğe bağlı) İzolasyon için sanal ortam oluşturun: `python -m venv venv` ardından aktif edin
   - Bağımlılıkları yükleyin: `python -m pip install matplotlib numpy`

3. Çözümü uygulayın
   - Aşağıdaki görev açıklamasını okuyun
   - Gerekli fonksiyonları uygulamak için `src/solution.py` dosyasını düzenleyin

4. Çözümü çalıştırın ve doğrulayın
   - Testleri çalıştırın: `python -m pytest` (`task_2b/` dizininden)
   - Veya demoyu çalıştırın: `python src/demo.py`

---

# Görev 2b: JSON Yapılandırma Doğrulama Hatasını Düzeltme

## Amaç

**Bu bir hata düzeltme görevidir.** JSON yapılandırma dosyalarını bir şemaya göre doğrulamak için bir yapılandırma dosyası doğrulayıcısı uygulandı, ancak boolean değerler string olarak temsil edildiğinde (`"true"` veya `"false"` gibi) doğru doğrulamada başarısız oluyor. Bu, geçerli yapılandırma dosyalarının reddedilmesine neden oluyor.

## Sorun Açıklaması

`validate_config()` fonksiyonu yapılandırma dosyalarını bir şemaya göre doğrular. Şema, her alan için beklenen türleri belirtir. Ancak boolean değerler string olarak sağlandığında (ortam değişkenlerinden veya CLI'den gelen yapılandırma dosyalarında yaygın), doğrulayıcı bunları yanlış bir şekilde reddeder.

### Sorun Örneği

Bu yapılandırma reddediliyor ama geçerli olmalı:
```json
{
  "debug": "true",
  "max_connections": "100",
  "timeout": "30.5"
}
```

Şema bekliyor:
```json
{
  "debug": "bool",
  "max_connections": "int",
  "timeout": "float"
}
```

Doğrulayıcı string temsillerini uygun türlere dönüştürmelidir, ancak şu anda sadece `"int"` ve `"float"` değerlerini işliyor, `"bool"` değerini işlemiyor.

## Nasıl Yeniden Üretilir

```python
from solution import validate_config

schema = {
    "debug": "bool",
    "port": "int"
}

config = {
    "debug": "true",  # String "true" bool'a dönüşmeli
    "port": "8080"    # String "8080" int'e dönüşmeli
}

# Bu ValueError veriyor ama başarılı olmalı
result = validate_config(config, schema)
```

## Göreviniz

Boolean string dönüşümünü işlemek için **`src/solution.py` dosyasındaki hatayı düzeltin**.

Doğrulayıcı şu anda `int` ve `float` dönüşümü için kod içeriyor:
```python
if expected_type == 'int':
    value = int(value)
elif expected_type == 'float':
    value = float(value)
```

**`'bool'` türü için destek ekleyin** ve şunları dönüştürün:
- `"true"`, `"True"`, `"TRUE"`, `"1"` → `True`
- `"false"`, `"False"`, `"FALSE"`, `"0"`, `""` → `False`

### Beklenen Davranış

Düzeltme sonrası:
- String `"true"` boolean `True`'ya dönüşür
- String `"false"` boolean `False`'a dönüşür
- Büyük/küçük harf duyarsız: `"True"`, `"TRUE"` hepsi çalışır
- Sayısal stringler: `"1"` → `True`, `"0"` → `False`
- Boş string `""` → `False`

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
2. `validate_config()` içindeki tür dönüşümü bölümünü kontrol edin
3. `expected_type == 'bool'` için yeni bir `elif` cümlesi ekleyin
4. Büyük/küçük harf duyarsız string karşılaştırması için `.lower()` kullanın
