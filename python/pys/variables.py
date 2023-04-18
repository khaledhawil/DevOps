
# name = 'khaled'

# if name == 'khaled':
#     print('Hello Khaled from py file!')


# this will print in one line
# paragraph = 'My name is  Khaled,' \
#                'I work at Vois,' \
#                'I live in Al Nawyah'


# print (paragraph)

# - to print them on multiline
# - To print multiline text in Python, you can use triple quotes (''' or """)

# cv = """
# My name is Khaled,
# I work from Home,
# I work as a Devops
# """

# print(cv)

# "1- Straing"




# fullName = 'Khaled Abd El-Hay Hawil'

# print(fullName[0:20])






height = int(input("Enter pyramid height: "))

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()


