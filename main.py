
tag_name = "h1"
angle_bracket = ["<",">"]
content = "블루윈"


#열기/닫기 -> 이분법 코드 생각
def make_tag(isOpen):
    if isOpen == True:
        open = angle_bracket[0] + tag_name + angle_bracket[1]
        return open
    else:
        close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]
        return close
    

result= make_tag(True) + "블루윈" + make_tag(False)


print(result)