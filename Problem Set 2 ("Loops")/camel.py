camel = input("Variable name: ")
snake = camel
index_list = []
for i in range(len(camel)):
    if camel[i].isupper():
        in_lower = camel[i].lower()
        snake = snake.replace(camel[i], "_" + in_lower)

print(snake)