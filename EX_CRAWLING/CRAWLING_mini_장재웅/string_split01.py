import re

span_string='<span>데이터분석가</span><span>데이터분석</span><span>데이터엔지니어</span>'

remove_span = re.split(r'<span>|</span>', span_string)
print(remove_span)
print('-' * 80)

item_list =[]
for word in remove_span:
    if word !='':
        item_list.append(word)

print(item_list)

