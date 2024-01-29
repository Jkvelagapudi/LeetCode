# Number 299

# Finished

# Runtime: 1045 ms (Beats 5.30% of Python Users)

# Memory 11.69 mb (Beats 98.82% of Python Users)

secret = "12"
guess = "21"

length = len(secret)

exact = 0
almost = 0

secret2 = secret
guess2 = guess

for i in range(length):
    if (secret[i] == guess[i]):
        exact += 1
        secret2 = secret2.replace(secret[i], "", 1)
        guess2 = guess2.replace(guess[i], "", 1)
       

length = len(secret2)



for i in range(length):
    for j in range(length):
        if (secret2[i] == guess2[j]):
            if(secret2[i] != " " and guess2 != " "):
                almost += 1
                secret2 = secret2.replace(secret2[i], " ", 1)
                guess2 = guess2.replace(guess2[j], " ", 1)

exact = str(exact)
almost = str(almost)

print(exact + "A" + almost + "B")