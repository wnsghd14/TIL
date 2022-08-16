# 문제1
# SELECT COUNT(age) FROM healthcare;
# COUNT(age)
# ----------
# 1000000
# 문제2
# SELECT COUNT(age) FROM healthcare WHERE age >= 10;
# COUNT(age)
# ----------
# 843723
# SELECT COUNT(gender) FROM healthcare WHERE gender == 1;
# COUNT(gender)
# -------------
# 510689
# sqlite> SELECT COUNT(*) FROM healthcare WHERE smoking==3 AND is_drinking==1;
# COUNT(*)
# --------
# 150361
# sqlite> SELECT COUNT(*) FROM healthcare WHERE va_left>=2.0 AND va_right>=2.0;
# COUNT(*)
# --------
# 2614
# sqlite> SELECT DISTINCT sido FROM healthcare;
# sido
# ----
# 36
# 27
# 11
# 31
# 41
# 44
# 48
# 30
# 42
# 43
# 46
# 28
# 26
# 47
# 45
# 29
# 49