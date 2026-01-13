
content = "블루윈"

def make_element(isOpen,tag_name, content):
    def make_tag(isOpen,tag_name):
        angle_bracket = ["<",">"]
        slash = "/"

        if isOpen == True:
            open = angle_bracket[0] + tag_name + angle_bracket[1]
            return open
        else:
            close = angle_bracket[0] + slash + tag_name + angle_bracket[1]
            return close
    result= make_tag(isOpen,tag_name) + content + make_tag(not isOpen,tag_name)
    return result


result_element = make_element(True, "h1", content)
print(result_element)


    