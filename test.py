import pyupbit

access = "4Q4G466ARkx67yZ6oq5ox1eddsgmrnLU67TMKCzp"          # 본인 값으로 변경
secret = "YKkz9nx7jR4MNDlL9YF7B0xDUjP618k5P3zF9MX7"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회