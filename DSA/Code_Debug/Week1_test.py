# 1. Write a program to print absolute vlaue of a number entered by user.


def absolute_value(value: int) -> int:
    return abs(value)


# value = int(input("Enter a signed value : "))

# print(f"absolute value is : {absolute_value(value)}")

# 2. Given three angles of a triangle, determine whether it is an acute, obtuse, or right-angled triangle.


def triangle_check(angle1: int, angle2: int, angle3: int) -> str:
    # check if sum is 180
    if (angle3 + angle1 + angle2 != 180) or (angle1 == 0 or angle2 == 0 or angle3 == 0):
        return "ivalid"
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "right angle"
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "obtuse"
    else:
        return "acute"


# angle1 = int(input("Enter angle 1 : "))
# angle2 = int(input("Enter angle 2 : "))
# angle3 = int(input("Enter angle 3 : "))

# print(f"the triangle is  : {triangle_check(angle1,angle2,angle3)}")

print(1 + (3 - 4) * 2**10 // 6)
print(1 + (3 - 4) * 2**10 // 6)
print(1 + (3 - 4) * 2**10 // 6)
