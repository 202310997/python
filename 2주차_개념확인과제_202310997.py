def get_radius(prompt):
    r = int(input(prompt))
    return r


def get_circle_area(r) :
    print("결과 : ",3.14*r**2)
    


prompt = "반지름을 입력해주세요 : "
r = get_radius(prompt)

get_circle_area(r)