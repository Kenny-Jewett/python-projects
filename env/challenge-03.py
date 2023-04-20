# multi_dim = [[0] * 10 for i in range(10)]

# for i in range(10):
#     for j in range(10):
#         multi_dim[i][j] = i * j

# print(multi_dim[5][5])


# Russia, Russia, USA, USA, Russia, France, Australia = ("Vladimir Lenin", "Joseph Stalin", "Thomas Jefferson", "Barack Obama", "Tsar Nicolas III", "Napoleon Bonapart", "John Curtin")

# print(Russia, Russia, Russia)

# a, b, c = ("A", "B", "C")

# print(a, b, c)

historical_figures = {('Vladimir Lenin', 'Tsar Nicolas III'): 
                      'Russia', ('Thomas Jefferson', "Idly", "Dosa"): 
                      'USA', ('John Curtin',) : "Australia"}

print(historical_figures[('Vladimir Lenin', 'Tsar Nicolas III')])