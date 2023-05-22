import random


# Define the UPS ficility
Address = [
    ("Montclair State University",
     "1 Normal Ave, Montclair, NJ 07043"),
    ("Passaic County Community College",
     "1 College Blvd, Paterson, NJ 07505"),
    ("Rutgers University-New Brunswick", 
     "57 US-1, New Brunswick, NJ 08901"),
     ("Seton Hall University", 
      "400 S Orange Ave, South Orange, NJ 07079"),
      ("The College of New Jersey", "2000 Pennington Rd, Ewing Township, NJ 08628"),
      ("New Jersey Institute of Technology", "323 Dr Martin Luther King Jr Blvd, Newark, NJ 07102")
    ]


# Randomly select an address from Address and assign it to office_A
office_A = random.choice(Address)

# Create a new list Address2 that excludes the address that was randomly selected for office_A
Address2 = [addr for addr in Address if addr != office_A]

# Randomly select an address from Address and assign it to office_B
office_B = random.choice(Address2)

