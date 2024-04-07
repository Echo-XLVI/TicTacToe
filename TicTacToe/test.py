rows=[[0,1,2],[3,4,5],[6,7,8]]
print("""
    ___ ___ ___
   | {} | {} | {} |
    ___ ___ ___ 
   | {} | {} | {} |
    ___ ___ ___
   | {} | {} | {} |
    ___ ___ ___
    """.format(*[num for row in rows for num in row]))

# player=[1,2]

# def turn():
#     try:
#         for num in player:
#             yield num
#     except Exception as e:
#         return turn()
# t=turn()
# print(next(t))
# print(next(t))
# print(next(t))

# try:
#     assert 1/2 and 2/1 , "Devision by zero"
#     assert 1/2 and 0/1 , "Devision by zero"
# except:
#     print("fuck you")