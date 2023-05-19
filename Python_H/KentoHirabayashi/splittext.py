import sys

args = sys.argv

# input text and index
input_text = args[1]
index = int(args[2])

splited_input_text = input_text.split(" ")

if len(splited_input_text) >= index:
    print(f"{splited_input_text[index-1]}", end="")
else:
    print("正しい範囲を指定して下さい")