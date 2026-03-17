<div align="center">

# 🚀 Python Module 09

### Data Validation with Pydantic

[![42 Network](https://img.shields.io/badge/42-Network-000000?style=flat&logo=42&logoColor=white)](https://42.fr)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)

*A space-themed exploration of data validation patterns in Python*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Exercises](#-exercises)
- [Key Concepts](#-key-concepts)
- [Installation](#-installation)
- [Usage](#-usage)
- [Author](#-author)

---

## 🌌 Overview

This module explores **data validation** in Python using Pydantic models through space-themed exercises. Each exercise demonstrates progressively more complex validation patterns, from basic field constraints to custom business logic validators.

### What You'll Learn

- ✅ Field-level validation with constraints
- ✅ Type safety with Python type hints
- ✅ Custom validators for business logic
- ✅ Nested model composition
- ✅ Enum-based validation
- ✅ Automatic type coercion and parsing

---

## 🎯 Exercises

### Ex00: Space Station
> *Basic Pydantic model with field validation constraints*

Validates space station data with constraints on IDs, crew size, and resource levels.

**Key Features:**
- 🔤 String length validation (`station_id`, `name`)
- 🔢 Numeric range validation (`crew_size`, `power_level`, `oxygen_level`)
- 📅 DateTime handling
- ⚙️ Optional fields with defaults

**Run:**
```bash
python ex0/space_station.py
```

---

### Ex01: Alien Contact
> *Introduces enums and custom model validators*

Validates alien contact records with type classification and cross-field validation.

**Key Features:**
- 🏷️ Enum-based field validation (`ContactType`)
- 🔧 Custom `@model_validator` for business rules
- 🔗 Cross-field validation logic
- 🆔 Pattern validation (ID prefix checking)

**Run:**
```bash
python ex1/alien_contact.py
```

---

### Ex02: Space Crew
> *Complex nested models with list validation*

Validates space mission crew compositions with leadership and experience requirements.

**Key Features:**
- 🪆 Nested Pydantic models (`CrewMember` within `SpaceMission`)
- 📊 List field validation with size constraints
- 👨‍✈️ Complex business rules (leadership requirements, experience ratios)
- 🔀 Multi-field conditional validation

**Run:**
```bash
python ex2/space_crew.py
```

---

## 🔑 Key Concepts

| Concept | Description |
|---------|-------------|
| **Field Constraints** | `Field()` with `min_length`, `max_length`, `ge`, `le` |
| **Type Safety** | Strong typing with Python type hints |
| **Enums** | Type-safe enumeration with `str` and `Enum` |
| **Custom Validators** | `@model_validator` for complex business logic |
| **Nested Models** | Composing models within models |
| **Automatic Coercion** | DateTime parsing from strings |

---

## 📦 Installation

### Requirements

```bash
pip install pydantic
```

### Python Version

- Python 3.8 or higher

---

## 🚀 Usage

Each exercise can be run independently:

```bash
# Exercise 0
python ex0/space_station.py

# Exercise 1
python ex1/alien_contact.py

# Exercise 2
python ex2/space_crew.py
```

---

## 👤 Author

**dbaltaza** - *42 Network*

Part of the 42 Network Common Core curriculum - Python specialization.

---

<div align="center">

**[42 Network](https://42.fr)** | **Python Module 09**

</div>
