def krw_to_usd(won):  # 1$는 1000원
    dollars = []
    for i in won:
        dollars.append(i/1000)
    print("미국화페 :", dollars)
    usd_to_jpy(dollars)

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars): # 1000엔 8$
    yens = []
    for i in dollars:
        yens.append(i * 1000 / 8)
    print("일본화페 :", yens)

amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐 : " + str(amounts))
krw_to_usd(amounts)