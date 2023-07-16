with open("origin.txt", "r") as file:
    data = file.read().replace("“", ")").replace("”", "(").replace("\n)", ")\n").replace("(\n", "\n(").replace("()", "").strip("()\n ").split("\n")

def show(data):
    import json
    length = len(data)
    conversation_length = length // 2
    for i in range(conversation_length):
        prompt = data[i*2]
        response = data[i*2 + 1]
        history = [[data[j*2], data[j*2+1]] for j in range(i)]
        result = {"prompt":prompt, "response":response, "history":history}
        print(json.dumps(result, ensure_ascii=False))

show(data)
show(data[1:])
