

def circle_area_circum():
    radius = int(input("원의 반지름을 입력하세요 : "))
    area = 3.14 * (radius ** 2)
    circum = 2 * 3.14 * radius
    return radius ,area, circum

radius_ex, area_ex, circum_ex = circle_area_circum()

print('반지름 {}인 원의 면적은 {}, 원의 둘레는 {}'.format(radius_ex,area_ex,circum_ex))