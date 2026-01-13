content = "공욱재"

def make_element(tag_name, content):
    # 여는 태그와 닫는 태그를 만드는 헬퍼 함수 (Closure)
    def make_tag(tag, is_close=False):
        if is_close:
            return f"</{tag}>"
        return f"<{tag}>"

    # f-string을 사용하여 직관적으로 조합
    return f"{make_tag(tag_name)}{content}{make_tag(tag_name, is_close=True)}"

result_element = make_element("h1", content)
print(result_element)