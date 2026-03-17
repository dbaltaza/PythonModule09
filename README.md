# Python Module 09 - Data Validation with Pydantic

**Author:** dbaltaza (42 Network)

## Overview

This module explores data validation in Python using Pydantic models through space-themed exercises. Each exercise demonstrates progressively more complex validation patterns, from basic field constraints to custom business logic validators.

## Exercises

### Ex00: Space Station
Basic Pydantic model with field validation constraints.

**Features:**
- String length validation (`station_id`, `name`)
- Numeric range validation (`crew_size`, `power_level`, `oxygen_level`)
- DateTime handling
- Optional fields with defaults

**Run:**
```bash
python ex0/space_station.py
```

### Ex01: Alien Contact
Introduces enums and custom model validators.

**Features:**
- Enum-based field validation (`ContactType`)
- Custom `@model_validator` for business rules
- Cross-field validation logic
- Pattern validation (ID prefix checking)

**Run:**
```bash
python ex1/alien_contact.py
```

### Ex02: Space Crew
Complex nested models with list validation.

**Features:**
- Nested Pydantic models (`CrewMember` within `SpaceMission`)
- List field validation with size constraints
- Complex business rules (leadership requirements, experience ratios)
- Multi-field conditional validation

**Run:**
```bash
python ex2/space_crew.py
```

## Key Concepts

- **Field Constraints**: `Field()` with `min_length`, `max_length`, `ge`, `le`
- **Type Safety**: Strong typing with Python type hints
- **Enums**: Type-safe enumeration with `str` and `Enum`
- **Custom Validators**: `@model_validator` for complex business logic
- **Nested Models**: Composing models within models
- **Automatic Coercion**: DateTime parsing from strings

## Requirements

```bash
pip install pydantic
```

## 42 Project

Part of the 42 Network Common Core curriculum - Python specialization.

**Project:** Python Module 09
**Campus:** 42
**Login:** dbaltaza
