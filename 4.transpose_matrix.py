'''
input = [[3, 4, 5],
     [7, 8, 9],
     [2, 1, 0]]
     
output = [
    [3,7,2],
    [4,8,1],
    [5,9,0]
]
'''

a = [[3, 4, 5],
     [7, 8, 9],
     [2, 1, 0],
     [1, 2, 3]
    ]

# * Works with any matrix
# Initialize an empty matrix for transpose
rows = len(a)
cols = len(a[0])
transposed = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(a[i][j])
    transposed.append(new_row)
    
print(transposed)



