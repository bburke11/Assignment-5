import requests

student_key = input("Student key: ")
seed = sum(ord(ch) for ch in student_key.strip())

if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

total_skus = 0
reorder_count = 0

while True:
    sku = input("SKU: ").strip()
    if sku.upper() == "DONE":
        break
    if not sku:
        print("SKU cannot be blank. Please try again.")
        continue

    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("Quantity must be 0 or greater. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")

    total_skus += 1
    if on_hand < threshold:
        reorder_count += 1
        print(f"  {sku}: REORDER")
    else:
        print(f"  {sku}: OK")

term = "weezer" if seed % 2 == 0 else "drake"

songs_returned = "N/A"
api_status = "FAILED"

try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={"term": term, "entity": "song", "limit": 5},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    results = data.get("results", [])
    song_count = sum(1 for item in results if item.get("kind") == "song")
    songs_returned = song_count
    api_status = "OK"
except requests.exceptions.RequestException:
    api_status = "FAILED"
except (KeyError, ValueError, TypeError):
    api_status = "INVALID_RESPONSE"

print()
print(f"Seed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {term}")
print(f"Songs returned: {songs_returned}")
print(f"API status: {api_status}")
