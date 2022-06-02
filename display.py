menu = ["ham", "butter", "tomato", "bread"]

def display(_menu,_name):
    
    contents = f"========={_name}===========" + "\n"
    for item in _menu:
        contents += f"{item}\n"
    return contents

print(display(menu, 'Menu'))