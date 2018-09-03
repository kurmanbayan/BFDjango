v = int(input())
t = int(input())

ans = (abs(v) * t) % 109
if v < 0: 
	ans = (109 - ans) % 109

print(ans)