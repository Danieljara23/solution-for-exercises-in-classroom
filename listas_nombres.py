names_list = ["Daniel", "Alexis", "Violeta", "Victor", "Manuel"]

print(f"La lista tiene {len(names_list)} elementos")

print(names_list[1])
print(names_list[-1])

for i in range(len(names_list)):
  if names_list[i][0] == "V":
    print(names_list[i])