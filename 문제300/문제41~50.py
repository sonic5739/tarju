# 문제 41 upper 소문자를 대문자로 벼화주는 함수
ticker = "btc_krw"
print( ticker.upper() )
# 문제 42 lower 대문자를 소문자로 변화주는 함수
ticker = "BTC_KRW"
print( ticker.lower() )
# 문제 43 capitalize() 함수 : 첮글자만 대문자로 변환 해주는 함수
ticker = "btc_krw"
print( ticker.capitalize() )
# 문제 44 : endswith() 함수 : 끝나는 문자가 맞는지 확인 함수
file_name = "보고서.xlsx" # 엑셀파일
print( file_name.endswith("xlsx") ) # 파일에서 "xlsx" 으로 끝나는지 확인
# 맞으면 true 틀리면 false
# 문제 45
file_name = "보고서.xlsx" # 엑셀파일
print( file_name.endswith(("xlsx" , "xls") ) )
# xlsx 혹은 xls 로 끝나는지 확인
# 문제 46 : startwith() 함수 : 시작하는 문자가 맞는지 확인
file_name = "2020_보고서.xlsx"
print( file_name.startswith("2020") )
# 문제 47
a = "Hell0 world"
print(a.split() )
# 문제 48
ticker = "btc_krw"
print(ticker.split("_") )
# 문제 49
data = "2020-05-01"
print(data.split("-") )
# 문제 50 # rsplit 오른쪽 공백 제거 # lstrip는 왼쪽공백 제거
data = "039490      "
print(data.rsplit() )