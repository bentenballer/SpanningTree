# submitted by Sophie Foreman, OMSCS Fall 2018
# # ---------------
# |             |
# 1------2------3    
# |\\_  /|\  _//|
# | \ \/ | \/ / |
# |  \/\_|_/\/  |
# |  /\/ | \/\  |
# | / /\ | /\ \ |
# |/_/  \|/  \_\|
# 6------5------4
# |             |
# ---------------

topo = {
    1: [2, 3, 4, 5, 6],
    2: [3, 1, 4, 5, 6],
    3: [1, 4, 2, 6, 5],
    4: [2, 1, 3, 5, 6],
    5: [3, 2, 1, 6, 4],
    6: [5, 3, 4, 1, 2]
}

### SOLUTION ###

# ---------------
# |             |
# 1------2      3    
# |\\_
# | \ \  
# |  \ \_ _ 
# |   \    \  
# |    \    \  
# |     \    \_
# 6      5     4
# 

# 1 - 2, 1 - 3, 1 - 4, 1 - 5, 1 - 6
# 2 - 1
# 3 - 1
# 4 - 1
# 5 - 1
# 6 - 1
