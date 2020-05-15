import builtwith

U = raw_input('Enter Target Website: ')

R = builtwith.builtwith(U)

for i in R:

    print i, ":",R[i][0]
