ptxt=input("请输入一串字符：")
key=input("请输入位移长度")
for c in ptxt:
      if "a"<=c<="z":
            print(chr(ord("a")+(ord(c)-ord("a")+int(key))%26),end="")
      elif "A"<=c<="Z":
            print(chr(ord("A")+(ord(c)-ord("A")+int(key))%26),end="")
      else:
            print(c,end="")