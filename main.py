
content = "블루윈"


#열기/닫기 -> 이분법 코드 생각
def make_tag(isOpen,tag_name):
    angle_bracket = ["<",">"]
    slash = "/"

    if isOpen == True:
        open = angle_bracket[0] + tag_name + angle_bracket[1]
        return open
    else:
        close = angle_bracket[0] + slash + tag_name + angle_bracket[1]
        return close
    

for i in range(100):
    result= make_tag(True,"h1") + content + make_tag(False,"h1")
    print(result)