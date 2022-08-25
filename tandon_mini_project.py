#  Tandon: Build a Punnet Square generator, where a user can enter two parents alleles and it will output a punnet square with the different possibilities for the children of those two parents.

parent_1_allele = input("What is your first parent's allele? ") # AA
parent_2_allele = input("What is your second parent's allele? ") # Aa

punnet_squares = [
    parent_1_allele[0] + parent_2_allele[0],
    parent_1_allele[0] + parent_2_allele[1],
    parent_1_allele[1] + parent_2_allele[0],
    parent_1_allele[1] + parent_2_allele[1]
]

uppercase = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
lowercase = 'qwertyuioplkjhgfdsazxcvbnm'

for i, square in enumerate(punnet_squares):
    if square[0] in lowercase and square[1] in uppercase:
        punnet_squares[i] = square[::-1]

print(f"""\npunnet square:\n | {parent_1_allele[0]}| {parent_1_allele[1]}
{parent_2_allele[0]}|{punnet_squares[0]}|{punnet_squares[1]}
{parent_2_allele[1]}|{punnet_squares[2]}|{punnet_squares[3]}""")