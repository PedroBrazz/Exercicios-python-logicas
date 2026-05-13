vp = int(input())
fn = int(input())
fp = int(input())
vn = int(input())

ac = (vp + vn)/(vp +vn +fp +fn)

pre = vp /(vp + fp)

sen = vp /( vp + fn)
print(f'{ac:.2f}')
print(f'{pre:.2f}')
print(f'{sen:.2f}')