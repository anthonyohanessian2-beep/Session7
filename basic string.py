text = "Hello World"
print(text)
text = "Hello World 2" #single vs double
print(text[4])
print(len(text)) # length of text
text = ""
print(len(text))

text= "bob"
print(text[-1]) # last character in the string
print(text[-3])
print(text[6//3])

# if you cant add 2 strings

s1= ("hello")
s2= ("bye")
print(s1+s2)
print(s1*4)

# string is iterable you can use for over it

s1= ("hello my name is bob")
for c in s1:
    print(c)

s1= "i like to give hi fives"
# print this string, but replace 'i' with 'y'
# Y like to give hi fives
s1_new=""
for c in s1:
    if c=="i":
        s1_new+= "i"
    elif c == "I":
            s1_new+="y"
    else:
        s1_new= s1_new+c
        print(s1_new)