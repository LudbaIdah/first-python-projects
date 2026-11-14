def calculate_uniform_acceleration():
    print("==========================================")
    print("   PHYSICS UNIFORM ACCELERATION (SUVAT)   ")
    print("==========================================")
    print("Select what you want to calculate:")
    print("1. Final Velocity (v) given u, a, t")
    print("2. Displacement (s) given u, a, s")
    print("3. Final Velocity squared (v^2) given u, a, s")
    print("4. Time (t) given s, u, v")
    print("5. Acceleration (a) given v, u, t")
    print("------------------------------------------")

    choice = input("Enter option number (1-5): ")


    if choice == '1':
        u = float(input("Enter initial velocity (u): "))
        a = float(input("Enter acceleration (a): "))
        t = float(input("Enter time (t): "))
        v = u + (a * t)
        print(f"Result: Final Velocity (v) = {v} m/s")

    elif choice == '2':
        v = float(input("Enter final velocity (v): "))
        u = float(input("Enter initial velocity (u): "))
        a = float(input("Enter acceleration (a): "))
        s = (v**2 - u**2) / (2 * a)
        print(f"Result: Displacement (s) = {s} meters")

    elif choice == '3':
        u = float(input("Enter initial velocity (u): "))
        a = float(input("Enter acceleration (a): "))
        s = float(input("Enter displacement (s): "))
        v_squared = (u ** 2) + (2 * a * s)
        print(f"Result: Final Velocity squared (v^2) = {v_squared}")
        if v_squared >= 0:
            print(f"Final Velocity (v) = {v_squared**0.5} m/s")

    elif choice == '4':
        s = float(input("Enter displacement (s): "))
        u = float(input("Enter initial velocity (u): "))
        v = float(input("Enter final velocity (v): "))
        t = (2 * s) / (u + v)
        print(f"Result: Time (t) = {t} seconds")

    elif choice == '5':
        v = float(input("Enter final velocity (v): "))
        u = float(input("Enter initial velocity (u): "))
        t = float(input("Enter time (t): "))
        a = (v - u) / t
        print(f"Result: Acceleration (a) = {a} m/s^2")

    else:
        print("Invalid choice. Please select between 1 and 5.")


while True:
    calculate_uniform_acceleration()
    again = input("Do another calculation? (y/n): ")

    if again != 'y'.lower():
        print("Exiting calculator...")
        break