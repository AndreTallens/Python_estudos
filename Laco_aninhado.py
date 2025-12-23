# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
for i in range(rows):
    # Inner loop for columns - build the row
    row = ""
    for j in range(cols):
        row += "*"
    # Print the completed row
    print(row)