temp = input("Input temperature: ")
degree = int(temp[:-1])  # :-1 is the number part
i_convention = temp[-1]  # -1 is the unit part

# for celsius
if i_convention.upper() == "C":
    fahr = int(round((9 * degree) / 5 + 32))
    Kelvin = degree + 273
    Unit = "Fahr and kelvin"

    print(f"Temperature in {Unit} is, 
          {fahr} degrees and {Kelvin} kelvin")

# for fahr
elif i_convention.upper() == "F":
    cel = int(round((degree - 32) * 5 / 9))
    Kelvin = cel + 273
    Unit = "Cel and Kelvin"

    print(f"Temperature in {Unit} is,
          {cel} degrees and {Kelvin} kelvin")

# for kelvin
elif i_convention.upper() == 'K':
    cel = degree - 273
    fahr = (degree - 273.15) * 9/5 + 32
    Unit = "cel and fahr"

    print(f"Temperature in {Unit} is,
          {cel} degrees and {fahr} fahr")

else:
    print("improper convention")
    quit()
