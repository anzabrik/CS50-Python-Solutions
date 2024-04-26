gr = input("Hi! ")

gr = gr.strip()
gr = gr.lower()

if gr[0] == "h":
    if gr[:5] == "hello":
        print("$0")
    else:
        print("$20")
else:
    print("$100")