# Unit Converter Project


'''
- Length ( Lambai)
units:
    Meter(m) >> basic unit
    kilometer(km) >> 1000 meter
    Centimeter(cm) >> 1 meter = 100 cm

Real life:
    Ghar ki lambai = meter(m)
    Road ki lambai = kilometer(km)
    Pencil ki lambai = centimeter
short:
    1 km = 1000 cm
    1 m = 100 cm

==========================

⚖️ Weight (Wazan)
👉 Weight ko bolte hain: wazan

Units:
Kilogram (kg) → heavy cheezon ke liye
Gram (g) → choti cheezon ke liye
Pound (lb) → foreign system

Real Life Example:
Aata ke bori = kg
Cheeni = gram
Gym weight machine = pound

👉 Samajh:
1 kg = 1000 gram
1 kg ≈ 2.2 pound

==========================

🌡️ Temperature (Hararat)
👉 Temperature ko bolte hain: garmi ya thandak ki measurement

Units:
Celsius (°C) → Pakistan mein use hota hai
Fahrenheit (°F) → USA system

Real Life Example:
Weather app = Celsius
Fever check = temperature

👉 Samajh:
0°C = freezing
100°C = boiling

'''

# =====================================
# ADVANCED UNIT CONVERTER PROJECT

# history store karne kalie empty list create karenge
history = []

# Function: Screen clear karne kalie
def clear_screen():
    print("\n" * 5)


# Main Menu
def main_menu():
    print("========================================")
    print("  ADVANCED UNIT CONVERTER PROJECT")
    print("========================================")
    print("1. Lenght (Lambai)")
    print("2. Weight (Wazan)")
    print("3. Temperature (Hararat)")
    print("4. History Dekho")
    print("5. Exit")


# ==========================================
# Lenght Converter 
# ==========================================

def lenght_converter():
    while True:
        print("\n --- LENGHT CONVERTER (LAMBAI) ---")
        print("1. Meter to kilometer")
        print("2. kilometer to meter")
        print("3. Meter to Centimeter")
        print("4. Centimeter to Meter")
        print("5. Back")

        choice = input("choice enter karo:")

        try:
            if choice == "1":
                m = float(input("Meter enter karo:"))
                result = m / 1000
                print("Result:", result, "km")
                history.append(f"{m} m = {result} km")
            
            elif choice == "2":
                km = float(input("kilometer enter karo:"))
                result = km * 1000
                print("Result:", result, "m")
                history.append(f"{km} km = {result} m")
            
            elif choice == "3":
                m = float(input("Meter enter karo"))
                result = m * 100
                print("Result:", result, "cm")
                history.append(f"{m} m = {result} cm")

            elif choice == "4":
                cm = float(input("Centimeter enter karo :"))
                result = cm / 100
                print("Result:", result, "m")
                history.append(f"{cm} cm = {result} m")

            elif choice == "5":
                break

            else:
                print("Galat choice!")

        except:
            print("Invalid! Input Number Enter karo.")


# ========================================
# Weight Converter
# ========================================
def weight_converter():
    while True:
        print("\n --- Weight(wazan) Converter ---")
        print("1. KG to Gram")
        print("2. Gram to KG")
        print("3. KG to Pound")
        print("4. Pound to KG")
        print("5. Back")

        choice = input("choice enter karo")

        try: 
            if choice == "1":
                kg = float(input("KG enter karo:"))
                result = kg * 1000
                print("Result:", result, "Gram")
                history.append(f"{kg} kg = {result} gram")

            elif choice == "2":
                g = float(input("Gram enter karo:"))
                result = g / 1000
                print("Result:", result, "KG")
                history.append(f"{g} gram = {result} kg ")

            elif choice == "3":
                kg = float(input("KG enter karo:"))
                result = kg * 2.20462
                print("Result:", result, "Pound")
                history.append(f"{kg} kg = {result} lb")

            elif choice == "4":
                lb = float(input("Pound enter karo:"))
                result = lb / 2.20462
                print("Result:", result, "KG")
                history.append(f"{lb} lb = {result} kg")
            
            elif choice == "5":
                break

            else:
                print("Ghalat choice")

        except:
            print("Invalid input!")
    
    # =====================================
    # Temperature converter
    # =====================================
def temperature_converter():
    while True:
        print("\n --- TEMPERATURE (HERARAT) ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Back")
    
        choice = input("choice enter karo:")
    
        try:
            if choice == "1":
                    c = float(input("Celsius ener karo:"))
                    result = (c * 9/5) + 32
                    print("Result:", result, "F")
                    history.append(f"{c} C = {result} F")

            elif choice == "2":
                    f = float(input("Fahrenheit enter karo:"))
                    result = (f - 32) * 5/9
                    print("Result:", result, "C")
                    history.append(f"{f} F = {result} C")
                        
            elif choice == 3:
                break

            else:
                print("Ghalat choice!")
            
        except:
            print("Invalid Input!")

# =============================================
# History show karna
# ==============================================
def show_history():
    print("\n ---  HISTORY ---")
    if len(history) == 0:
        print("Abhi koi history nahi hai.")
    else:
        for item in history:
            print(item)


# ==========================================
# Main Program
# ==========================================

def main():
    while True:
        main_menu()
        choice = input("Apni choice enter karo")

        if choice == "1":
            lenght_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            show_history()
        
        elif choice == "5":
            print("Program band ho gaya hai, Allah Haifz")
            break

        else:
            print("Invalid Choice")
main()


