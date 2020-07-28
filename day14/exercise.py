

def get_score():
    while True:
        try:
            score = int(input("输入成绩："))
        except ValueError:
            print("输入有误")
            continue

        if 0 <= score <= 100:
            return score
        else:
            print("不在0-100范围之内")


get_score()
