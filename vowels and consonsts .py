letter="barathkumarinmailam"
vowel_count=0
const_count=0
for i in range(len(letter)):
    if(letter[i] in "aeiou"):
        vowel_count=vowel_count+1
        
    else:
        const_count=const_count+1
print(vowel_count)
print(const_count)

