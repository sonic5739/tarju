# 2차원 리스트 : [ [1차원]  ,  [1차원]  ,  [1차원]  ,  [1차원]  ]
# 문제 181
apart =  [ ["101호","102호"] , ["201호","202호"] , ["301호","302호"]  ]
# 문제 182
stock = [ ["시가",100,200,300] , ["종가",80,210,330]  ]
# 문제 183
stock = {  "시가" : [100,200,300] , "종가" : [80,210,330]  }
# 문제 184
stock = { "10/10" : [80,110,70,90] , "10/11" : [210,230,190,200] }
# 문제 185
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart :
    for 열 in 행 :
        print( 열 , "호" )
# 문제 186
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart[ : : -1] :
    for 열 in 행 :
        print( 열 , "호" )
# 문제 187
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart[ : : -1] :
    for 열 in 행[ : : -1] :
        print( 열 , "호" )
# 문제 188
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart :
    for 열 in 행 :
        print( 열 , "호" )
        print("-----")
# 문제 189
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart :
    for 열 in 행 :
        print( 열 , "호" )
    print("-----")
# 문제 190
apart =  [ [101,102] , [201,202] , [301,302] ]
for 행 in apart :
    for 열 in 행 :
        print( 열 , "호" )
print("-----")