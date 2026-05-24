# Parity Checker 🔢

Une bibliothèque Python simple pour vérifier la parité des nombres (pair ou impair).

## 📋 Fonctionnalités

- Vérifier si un nombre est pair ou impair
- Filtrer une liste selon la parité
- Compter les nombres pairs/impairs dans une liste

## 🚀 Installation

```bash
git clone https://github.com/ton-username/parity-checker.git
cd parity-checker
```

## 💻 Utilisation

```python
from utils.parity import parity_of_number, parity_of_list, count_of_elements

# Vérifier un nombre
print(parity_of_number(12))  # True (pair)
print(parity_of_number(13))  # False (impair)

# Filtrer une liste
print(parity_of_list([12, 13, 14, 15], 'odd'))  # [13, 15]

# Compter les éléments
numbers = [126, 128, 2789, 98163, 6751, 1522]
print(count_of_elements(numbers, "even"))  # 3
print(count_of_elements(numbers, "odd"))   # 3

## 🎓 Objectif

Projet d'apprentissage créé pour pratiquer :
- La modularisation du code Python
- La création de fonctions réutilisables
- L'organisation d'un projet

## 📝 Licence

Libre d'utilisation (MIT)