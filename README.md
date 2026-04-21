# Assignment 5

Python programs covering conditionals, loops, exception handling, functions, and libraries.

## Requirements

Python 3.x is required. Install the `requests` library before running `inventory_spotcheck.py`:

```
pip install requests
```

---

## Exercise 1 — Point-of-Sale Checkout System

**File:** `pos_checkout.py`

### How to run

```
python pos_checkout.py
```

### Example run

```
Student key: fairfield
Item name (or DONE to finish): Coffee
Unit price for 'Coffee': 4.50
Quantity for 'Coffee': 3
Item name (or DONE to finish): Notebook
Unit price for 'Notebook': 12.00
Quantity for 'Notebook': 8
Item name (or DONE to finish): DONE

Seed: 874
Units: 11
Subtotal: $109.50
Discount: 10%
Perk applied: NO
Total: $98.55
```

---

## Exercise 2 — Inventory Spot Check

**File:** `inventory_spotcheck.py`

### How to run

```
python inventory_spotcheck.py
```

### Example run

```
Student key: fairfield
SKU: ITEM-101
On hand: 5
  ITEM-101: REORDER
SKU: ITEM-202
On hand: 30
  ITEM-202: OK
SKU: DONE

Seed: 874
Threshold: 12
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
