import numpy as np

test_1_values = {'X': np.array([[2, 3, 9, 12],
                                [5, 2, 6, 5]]),
                 'Y': np.array([[0, 1, 0, 1],
                                [1, 0, 1, 0]]),
                 'linear_1.W': np.array([[1.24737338, 0.28295388, 0.69207227],
                                         [1.58455078, 1.32056292, -0.69103982]]),
                 'linear_1.W0': np.array([[0],
                                          [0],
                                          [0]]),
                 'linear_2.W': np.array([[0.5485338, -0.08738612],
                                         [-0.05959343, 0.23705916],
                                         [0.08316359, 0.83962520]]),
                 'linear_2.W0': np.array([[0],
                                          [0]]),
                 'z_1': np.array([[10.41750064, 6.91122168, 20.73366505, 22.8912344],
                                  [7.16872235, 3.48998746, 10.46996239, 9.9982611],
                                  [-2.07105455, 0.69413716, 2.08241149, 4.84966811]]),
                 'a_1': np.array([[1., 0.99999801, 1., 1.],
                                  [0.99999881, 0.99814108, 1., 1.],
                                  [-0.96871843, 0.60063321, 0.96941021, 0.99987736]]),
                 'z_2': np.array([[0.40837833, 0.53900088, 0.56956001, 0.57209377],
                                  [-0.66368766, 0.65353931, 0.96361427, 0.98919526]]),
                 'a_2': np.array([[0.74498961, 0.47139666, 0.4027417, 0.39721055],
                                  [0.25501039, 0.52860334, 0.5972583, 0.60278945]]),
                 'loss': 3.5572007784781565,
                 'dloss': np.array([[0.74498961, -0.52860334, 0.4027417, -0.60278945],
                                    [-0.74498961, 0.52860334, -0.4027417, 0.60278945]]),
                 'dL_dz2': np.array([[0.74498961, -0.52860334, 0.4027417, -0.60278945],
                                     [-0.74498961, 0.52860334, -0.4027417, 0.60278945]]),
                 'dL_da1': np.array([[0.47375374, -0.3361494, 0.25611147, -0.38332583],
                                     [-0.2210031, 0.15681155, -0.11947437, 0.17881905],
                                     [-0.56355604, 0.39986813, -0.30465863, 0.45598708]]),
                 'dL_dz1': np.array([[1.69467553e-09, -1.33530535e-06, 0.00000000e+00, -0.00000000e+00],
                                     [-5.24547376e-07, 5.82459519e-04, -3.84805202e-10, 1.47943038e-09],
                                     [-3.47063705e-02, 2.55611604e-01, -1.83538094e-02, 1.11838432e-04]]),
                 'dL_dX': np.array([[-2.40194628e-02, 1.77064845e-01, -1.27021626e-02, 7.74006953e-05],
                                    [2.39827939e-02, -1.75870737e-01, 1.26832126e-02, -7.72828555e-05]]),
                 'updated_linear_1.W': np.array([[1.2473734,  0.28294514,  0.68940437],
                                                 [1.58455079, 1.32055711, -0.69218045]]),
                 'updated_linear_1.W0': np.array([[6.66805339e-09],
                                                  [-2.90968033e-06],
                                                  [-1.01331631e-03]]),
                 'updated_linear_2.W': np.array([[0.54845211, -0.08730443],
                                                 [-0.05968003, 0.23714576],
                                                 [0.08942097, 0.83336782]]),
                 'updated_linear_2.W0': np.array([[-8.16925787e-05],
                                                  [8.16925787e-05]])}

test_2_values = {'X': np.array([[2, 3, 9, 12],
                                [5, 2, 6, 5]]),
                 'Y': np.array([[0, 1, 0, 1],
                                [1, 0, 1, 0]]),
                 'linear_1.W': np.array([[1.24737338, 0.28295388, 0.69207227],
                                         [1.58455078, 1.32056292, -0.69103982]]),
                 'linear_1.W0': np.array([[0],
                                          [0],
                                          [0]]),
                 'linear_2.W': np.array([[0.5485338, -0.08738612],
                                         [-0.05959343, 0.23705916],
                                         [0.08316359, 0.83962520]]),
                 'linear_2.W0': np.array([[0],
                                          [0]]),
                 'z_1': np.array([[10.41750064, 6.91122168, 20.73366505, 22.8912344],
                                  [7.16872235, 3.48998746, 10.46996239, 9.9982611],
                                  [-2.07105455, 0.69413716, 2.08241149, 4.84966811]]),
                 'a_1': np.array([[10.41750064, 6.91122168, 20.73366505, 22.8912344],
                                  [7.16872235, 3.48998746, 10.46996239, 9.9982611],
                                  [0., 0.69413716, 2.08241149, 4.84966811]]),
                 'z_2': np.array([[5.28714248, 3.64078533, 10.92235599, 12.36410102],
                                  [0.78906625, 0.80620366, 2.41861097, 4.44170662]]),
                 'a_2': np.array([[9.88992134e-01, 9.44516196e-01, 9.99797333e-01, 9.99637598e-01],
                                  [1.10078665e-02, 5.54838042e-02, 2.02666719e-04, 3.62401857e-04]]),
                 'loss': 13.070537746542422,
                 'dloss': np.array([[9.88992134e-01, -5.54838042e-02, 9.99797333e-01, -3.62401857e-04],
                                    [-9.88992134e-01, 5.54838042e-02, -9.99797333e-01, 3.62401857e-04]]),
                 'dL_dz2': np.array([[9.88992134e-01, -5.54838042e-02, 9.99797333e-01, -3.62401857e-04],
                                     [-9.88992134e-01, 5.54838042e-02, -9.99797333e-01, 3.62401857e-04]]),
                 'dL_da1': np.array([[6.28919807e-01, -3.52832568e-02, 6.35791049e-01, -2.30458563e-04],
                                     [-2.93387075e-01, 1.64594141e-02, -2.96592466e-01, 1.07507449e-04],
                                     [-7.48134578e-01, 4.19713676e-02, -7.56308297e-01, 2.74143091e-04]]),
                 'dL_dz1': np.array([[6.28919807e-01, -3.52832568e-02, 6.35791049e-01, -2.30458563e-04],
                                     [-2.93387075e-01, 1.64594141e-02, -2.96592466e-01, 1.07507449e-04],
                                     [-0.00000000e+00, 4.19713676e-02, -7.56308297e-01, 2.74143091e-04]]),
                 'dL_dX': np.array([[7.01482813e-01, -1.03069207e-02, 1.85726843e-01, -6.73213966e-05],
                                    [6.09119276e-01, -6.31763062e-02, 1.13841333e+00, -4.12646736e-04]]),
                 'updated_linear_1.W': np.array([[1.21301666, 0.29898107, 0.72546012],
                                                 [1.55011264, 1.33662809, -0.66877713]]),
                 'updated_linear_1.W0': np.array([[-0.00614599],
                                                  [0.00286706],
                                                  [0.00357031]]),
                 'updated_linear_2.W': np.array([[0.39533114, 0.06581654],
                                                 [-0.14639538, 0.3238611],
                                                 [0.072955, 0.84983379]]),
                 'updated_linear_2.W0': np.array([[-0.00966472],
                                                  [0.00966472]])}
