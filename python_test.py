# ============================================================
# GEE252: Basic Python Programming Assignment
# python_test.py
# ============================================================


# ============================================================
# Problem 1: Variables and Data Types
# ============================================================
print("=== Problem 1 ===")

# Define the required variables
market_name = "Balogun Market"          # string
num_traders = 5000                       # integer
location_coords = (6.4541, 3.3947)      # tuple (latitude, longitude)
is_open_sundays = False                  # boolean

# Print each variable with its data type
print(f"Market: {market_name}, Type: {type(market_name)}")
print(f"Traders: {num_traders}, Type: {type(num_traders)}")
print(f"Coordinates: {location_coords}, Type: {type(location_coords)}")
print(f"Open Sundays: {is_open_sundays}, Type: {type(is_open_sundays)}")

# Calculate average daily revenue per trader
total_revenue = 25_000_000              # N25,000,000 total daily revenue
avg_revenue = total_revenue / num_traders
print(f"Average Daily Revenue per Trader: {avg_revenue} Naira")


# ============================================================
# Problem 2: Lists and Basic Operations
# ============================================================
print("\n=== Problem 2 ===")

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]

# Add "Ivory Coast" to the end of the list
host_countries.append("Ivory Coast")

# Insert "Morocco" at position 1
host_countries.insert(1, "Morocco")

# Remove "Senegal" from the list
host_countries.remove("Senegal")

# Print the total number of countries in the list
print(f"Total countries: {len(host_countries)}")

# Print countries in alphabetical order WITHOUT modifying the original list
sorted_countries = sorted(host_countries)
print(f"Alphabetical order: {sorted_countries}")

# Print every second country using slicing
print(f"Every second country: {host_countries[::2]}")


# ============================================================
# Problem 3: Dictionaries
# ============================================================
print("\n=== Problem 3 ===")

river_data = {
    "Nile":  {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
    "Niger": {"length_km": 4180, "countries": 5}
}

# Add the Zambezi river
river_data["Zambezi"] = {"length_km": 2574, "countries": 6}

# Update the Niger river's countries value to 6
river_data["Niger"]["countries"] = 6

# Print all river names
print(f"Rivers: {list(river_data.keys())}")

# Print how many countries the Congo river flows through
print(f"Congo flows through: {river_data['Congo']['countries']} countries")

# Calculate and print the total combined length of all rivers
total_length = sum(r["length_km"] for r in river_data.values())
print(f"Total combined river length: {total_length} km")


# ============================================================
# Problem 4: Loops
# ============================================================
print("\n=== Problem 4 ===")

# --- Part A: For Loops ---

# Multiplication table of 7 (7x1 to 7x10)
print("Multiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# Print each letter in "AFRICA"
print("\nLetters in AFRICA:")
for letter in "AFRICA":
    print(letter)

# Sum of all even numbers from 1 to 50
even_sum = sum(n for n in range(1, 51) if n % 2 == 0)
print(f"\nSum of even numbers (1-50): {even_sum}")

# --- Part B: While Loops ---

# Countdown from 20 to 1
print("\nCountdown from 20 to 1:")
count = 20
while count >= 1:
    print(count)
    count -= 1

# Find first number > 500 divisible by both 3 and 7
num = 501
while not (num % 3 == 0 and num % 7 == 0):
    num += 1
print(f"\nFirst number > 500 divisible by 3 and 7: {num}")


# ============================================================
# Problem 5: Conditional Statements
# ============================================================
print("\n=== Problem 5 ===")

def classify_rainfall(mm):
    """Classify monthly rainfall level for West African weather monitoring."""
    if mm > 300:
        return "Flood Risk"
    elif mm >= 200:
        return "Heavy Rain"
    elif mm >= 100:
        return "Moderate Rain"
    elif mm >= 1:
        return "Light Rain"
    else:
        return "Dry"

# Test with the required values
for value in [350, 250, 150, 50, 0]:
    print(f"{value}mm: {classify_rainfall(value)}")


# ============================================================
# Problem 6: Functions
# ============================================================
print("\n=== Problem 6 ===")

# --- Part A: Basic currency conversion ---
def calculate_exchange(amount, rate):
    """Convert an amount in USD to Nigerian Naira using the given rate."""
    return float(amount * rate)

print(f"Exchange result: {calculate_exchange(100, 1580)}")  # Expected: 158000.0

# --- Part B: Formatted price string ---
def format_price(amount, currency="NGN"):
    """Return a formatted price string with the currency code and comma-separated amount."""
    return f"{currency} {amount:,}"

print(format_price(5000))        # "NGN 5,000"
print(format_price(200, "GHS"))  # "GHS 200"

# --- Part C: Analyse a list of exam scores ---
def analyze_scores(scores):
    """Return the lowest score, highest score, and class average."""
    lowest  = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)
    return lowest, highest, average

test_scores = [55, 72, 88, 61, 94, 47, 79]
low, high, avg = analyze_scores(test_scores)
print(f"Lowest: {low}, Highest: {high}, Average: {avg:.2f}")


# ============================================================
# Problem 7: String Operations
# ============================================================
print("\n=== Problem 7 ===")

proverb = "Slowly, slowly, catches the monkey, African wisdom"

# Convert to uppercase
print(proverb.upper())

# Split using comma as separator
print(proverb.split(","))

# Check whether the string contains "wisdom"
print("Contains 'wisdom':", "wisdom" in proverb)

# Replace "African wisdom" with "African proverb"
print(proverb.replace("African wisdom", "African proverb"))

# Count occurrences of the letter 'o' (case insensitive)
print(f"Count of 'o': {proverb.lower().count('o')}")


# ============================================================
# Problem 8: File Operations
# ============================================================
print("\n=== Problem 8 ===")

# Write the crops data to a file
try:
    with open("crops.txt", "w") as f:
        f.write("Cocoa,Nigeria,320000\n")
        f.write("Coffee,Ethiopia,480000\n")
        f.write("Cassava,Ghana,210000\n")
    print("crops.txt created successfully.")
except IOError as e:
    print(f"Error creating file: {e}")

# Read the file, print each line, and calculate total production
try:
    total_production = 0
    with open("crops.txt", "r") as f:
        for line in f:
            line = line.strip()
            print(line)
            # The third field (index 2) is the annual tonnes
            parts = line.split(",")
            total_production += int(parts[2])
    print(f"Total annual production: {total_production} tonnes")
except FileNotFoundError:
    print("Error: crops.txt not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# ============================================================
# Problem 9: List Comprehensions
# ============================================================
print("\n=== Problem 9 ===")

temperatures = [18, 23, 31, 27, 35, 19, 29, 33, 22, 28]

# Convert all temperatures to Fahrenheit
fahrenheit = [(c * 9/5) + 32 for c in temperatures]
print(f"Fahrenheit: {fahrenheit}")

# Only temperatures above 30 degrees Celsius
above_30 = [c for c in temperatures if c > 30]
print(f"Above 30°C: {above_30}")

# Temperatures between 20 and 29 (inclusive), rounded to nearest whole number
between_20_29 = [round(c) for c in temperatures if 20 <= c <= 29]
print(f"Between 20-29°C (rounded): {between_20_29}")


# ============================================================
# Problem 10: Error Handling
# ============================================================
print("\n=== Problem 10 ===")

try:
    balance    = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))

    # Custom check: withdrawal must not exceed balance
    if withdrawal > balance:
        print("Error: Insufficient funds! You cannot withdraw more than your balance.")
    else:
        remaining = balance - withdrawal
        print(f"Transaction successful. Remaining balance: {remaining:.2f}")

except ValueError:
    # Raised automatically if input() cannot be converted to float
    print("Error: Please enter a valid number for both balance and withdrawal amount.")

finally:
    # Always runs, regardless of success or failure
    print("Transaction attempt completed")
