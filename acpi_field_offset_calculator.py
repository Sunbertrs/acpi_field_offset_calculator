import os

while True:
    try:
        os.system("cls") if os.name=="nt" else os.system("clear")
        print("ACPI field offset calculator by Sunbertrs")
        offset = int(input("\nEnter your head offset: "),16)
    except ValueError:
        print("\nSomething wrong with your value, please type again.\n")
        input("Type [enter] to continue.")
    else:
        break

chart = input("\nEnter the bytes that are occupied ahead (separate with comma): ").split(",")
chart = [int(chart[i].strip()) for i in range(len(chart))]

result = []

for i in range(len(chart)):
    if i == 0:
        chart_sum = chart[i]
        current_addr = offset
        result.append(hex(current_addr))
    else:
        chart_sum = chart_sum + chart[i]
        current_addr = offset + (chart_sum - chart[i]) // 8 
        result.append(hex(current_addr))
    print("No.", i+1, "is start from", result[i])
    
    if i == len(chart)-1:
        next_addr = offset + chart_sum // 8
        result.append(hex(next_addr))
        print("No.", i+2, "should start from", result[i+1])

input("Type [enter] to continue.")
