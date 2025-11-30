print("A - Density (p=m/V)")
print("B - Kinetic Energy (KE=0.5*m*v^2)")
print("C - Ohm's Law (V=I*R)")
print("D - Potential Energy (PE=m*g*h)")
print("E - Force (F=m*a)")

choice = input("Enter formula: ").upper()

elif choice == "A":
    m = float(input("Enter mass (Kg): "))
    V = float(input("Enter volume (m^3): "))
    density = m/V
    print("Density =",density, Kg/m^3)

elif choice == "B":
    m = float(input("enter mass (Kg): "))
    v = float(input("Enter velocity (m/s): "))
    KE = 0.5*m*v*v
    print("Kinetic Energy =",KE,"J")

elif choice == "C":
    I = float(input("Enter current (A): "))
    R = float(input("Enter resistance: "))
    V = I*R
    print("Voltage =",V,"V")


elif choice == "D":
    m = float(input("Enter mass (Kg): "))
    g = 98
    h = float(input("Enter height (m): "))
    PE = m*g*h
    print("Potential Energy =", PE,"J")

if choice == "E":
    m = float(input("Enter mass (Kg): "))
    a = float(input("Enter acceleration (m/s^2): "))
    F = m*a
    print("Force =",F,"N")

else:
    print("Invalid choice")