import pyperclip

# 將文字複製到系統剪貼簿
pyperclip.copy('知識就像內褲，看不見但很重要。')

# 從系統剪貼簿讀取 (貼上) 內容，並存到 string 變數中
string = pyperclip.paste()

print(string)