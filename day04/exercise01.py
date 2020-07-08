# 倒计时120秒
"""
" / "  表示浮点数除法，返回浮点结果;
" // " 表示整数除法,返回不大于结果的一个最大的整数
"""
for time in range(120, -1, -1):
    min = time // 60
    sec = time % 60
    print("%02d:%02d" % (min, sec))
