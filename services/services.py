def getPrintStatement(input):
    name = input.get("name")
    if name:
        return [f"Hi, {name}"]
    else:
        return ["No name provided"]
