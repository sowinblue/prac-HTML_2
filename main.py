
tag_name = "h1"
angle_bracket = ["<",">"]
content = "블루윈"


tag_jolib_open = angle_bracket[0] + tag_name + angle_bracket[1]
tag_jolib_close = angle_bracket[0] + "/" + tag_name + angle_bracket[1]


#열기/닫기 -> 이분법 코드 생각
def make_tag(isOpen):
    if isOpen == True:
        open = tag_jolib_open
        return open
    else:
        close = tag_jolib_close
        return close
    

result= make_tag(True) + "블루윈" + make_tag(False)


print(result)