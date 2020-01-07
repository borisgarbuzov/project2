import numpy as np

bootstrap = np.array([np.nan, np.nan, 251.8685033, 253.5954079, 250.9137024,
                      249.7972269, 251.5174499, 253.5257251, 252.0431497,
                      254.5691208, 255.6432405, 252.7091047, 250.8903176,
                      250.6469398, 252.5010225, 252.8278624, 249.4171177,
                      253.0669622, 252.5249882, 252.0863912, 251.7852744,
                      251.840054, 250.0037797, 255.1181013, 248.8213637,
                      252.8666574, 251.5610602, 250.2320766, 254.4392544,
                      251.4896883, 250.9316425, 251.4759798, 250.4772313,
                      252.2710524, 251.955603, 251.1779755, 253.0841104,
                      253.1715636, 253.6973887, 251.9880264, 252.0003728,
                      251.720019, 254.9401791, 252.4984417, 253.3265094,
                      254.8330645, 252.755509, 249.2950142, 251.5472908,
                      251.530146, 250.7589417, 249.80701, 250.1322974,
                      250.4580215, 252.1299784, 250.3376993, 252.2424122,
                      249.6187552, 250.9937249, 251.1923302, 252.7418565,
                      249.6960813, 252.0284297, 250.5348589, 249.4808821,
                      247.3278795, 249.7927425, 248.101917, 249.6633471,
                      249.9228838, 249.5088962, 251.7008444, 253.3701579,
                      248.1451978, 249.2144575, 250.9542582, 250.0448838,
                      250.0897398, 251.8312064, 249.0977677, 248.6507893,
                      252.3081616, 252.2203333, 250.8917742, 250.6467748,
                      251.3697246, 250.1491118, 248.7419358, 252.5293295,
                      248.6927442, 248.2714244, 252.7515542, 251.8095728,
                      250.0274762, 251.0368061, 251.3820715, 248.7764889,
                      248.4915075, 248.5213141, 248.5298203, 249.2531964,
                      250.343559, 252.6717848, 251.6168105, 248.3292555,
                      249.3737467, 252.4079155, 246.9925897, 248.2693143,
                      248.1124259, 249.2901127, 248.317006, 250.5351494,
                      246.7054025, 249.7534405, 248.7938675, 249.6992435,
                      247.9293185, 248.4763759, 250.4793429, 248.9607974,
                      247.6941727, 248.6454761, 251.7254649, 249.5611513,
                      248.35359, 246.406774, 249.5558168, 249.6303951,
                      250.0933821, 248.3535972, 251.1842845, 252.759601,
                      248.8681294, 248.5006537, 249.2062542, 251.1145843,
                      249.8508364, 247.1030027, 246.5067905, 245.3371828,
                      251.4263772, 246.5813785, 250.4703218, 249.4313394,
                      247.291281, 249.1013977, 249.0429769, 247.4715018,
                      249.1610367, 247.0873578, 251.8640648, 248.6763441,
                      247.9528017, 247.2366412, 247.7908355, 247.2935087,
                      246.930278, 248.0402705, 247.43208, 247.0461224,
                      247.0200147, 245.0729086, 246.8825828, 247.6619134,
                      249.9375566, 250.693214, 247.7435216, 246.1337575,
                      248.3645899, 250.0302455, 247.3500098, 247.5551321,
                      248.9807989, 249.527696, 247.0008589, 247.4047445,
                      246.7018211, 245.4891541, 248.0170984, 246.4498153,
                      248.4531581, 245.822499, 247.7391881, 245.5793299,
                      247.4274618, 244.5679649, 245.2447194, 246.5634401,
                      247.0925592, 249.1497035, 248.5326785, 247.5653701,
                      245.7253889, 243.7819914, 248.6009036, 244.7636041,
                      250.5563526, 245.2895596, 247.4512788, 246.5441723,
                      248.0400799, 245.9271004, 247.6024044, 247.9244389,
                      246.2945961, 246.9718671, 245.7191987, 247.1122336,
                      247.6725205, 245.632792, 245.5857199, 245.4555674,
                      245.2915297, 244.4638461, 244.409217, 245.1949765,
                      248.677201, 246.2859198, 245.4745469, 246.9148612,
                      246.4505766, 244.4658745, 245.9920699, 244.2922571,
                      244.3922277, 244.9924984, 246.9216935, 244.8797661,
                      245.619708, 243.2397393, 243.3151721, 243.962391,
                      246.1432476, 243.861889, 243.1699478, 246.1774321,
                      245.2954429, 245.9778792, 247.2394439, 244.0911548,
                      242.8798378, 245.0991781, 244.8616837, 246.0060913,
                      245.3259773, 245.8388986, 244.0319906, 244.8792498,
                      245.1060188, 242.967902, 246.6943473, 248.3112699,
                      242.8560783, 246.0045711, 246.6016873, 244.1330198,
                      242.3446858, 247.223515, 244.2561875, 241.1260509,
                      245.0701715, 245.1248993, 244.5680091, 243.4394227,
                      242.9273955, 243.2947584, 242.2305397, 244.0861137,
                      244.4328914, 243.9936761, 241.4809655, 245.5985225,
                      245.0352218, 246.8220855, 243.8896495, 244.9581433,
                      245.1962655, 244.9441373, 241.0558896, 244.2361381,
                      243.6891178, 244.2393182, 244.4121151, 242.439956,
                      242.5442376, 243.2415904, 242.9152694, 245.2039725,
                      242.2295131, 244.0184829, 244.678085, 244.8592954,
                      243.3888658, 244.5657765, 243.4993155, 242.2242026,
                      242.1472359, 244.2033757, 242.8253542, 240.9948366])

native = np.array([np.nan, np.nan, 238.4139233, 237.4496663, 246.7759745,
                   246.2766428, 241.8935248, 239.9841011, 234.1630173,
                   240.7119207, 238.9856422, 242.0867977, 242.3475492,
                   234.5472864, 240.8216918, 241.6845243, 239.614781,
                   240.1118916, 237.7193488, 238.443108, 235.5843635,
                   238.4624426, 236.4334549, 236.4633264, 239.3736388,
                   239.6484054, 240.9730772, 233.9645151, 235.6979787,
                   234.0065974, 234.5985562, 237.7543685, 238.6632091,
                   237.0319394, 238.2195882, 234.7434559, 236.1716371,
                   238.6114255, 243.2730591, 237.4120283, 233.2190376,
                   234.3820636, 239.4717532, 232.0454922, 236.8576857,
                   234.0350273, 237.3712546, 236.7883179, 235.3025456,
                   234.8171379, 235.0265758, 235.3844367, 238.3779449,
                   235.739797, 228.1851548, 235.9037863, 231.6051718,
                   232.8195099, 237.3693074, 228.7973177, 234.735486,
                   235.9115854, 233.5585878, 231.1827731, 233.029137,
                   236.6601561, 237.4046985, 234.3063151, 232.736133,
                   235.4700019, 227.7376924, 229.0926549, 236.7286871,
                   225.1673324, 232.3587101, 228.352085, 238.5635228,
                   232.6914112, 235.7103385, 235.3947857, 224.4592003,
                   229.7168003, 230.0935383, 229.9218705, 234.3415268,
                   233.6299282, 231.565914, 228.667453, 233.7171607,
                   228.2372662, 232.6472935, 235.5206313, 231.3364353,
                   229.8597207, 230.7819742, 230.0986267, 235.3156968,
                   226.3970084, 227.0130327, 227.8072356, 227.6568525,
                   233.3062559, 228.6349769, 231.4710268, 232.5668576,
                   226.6281343, 233.376444, 226.8592533, 227.7678321,
                   226.4459009, 229.3735919, 226.7806441, 221.5976665,
                   230.3209292, 226.3642517, 223.0956419, 226.3103673,
                   227.7433997, 223.1054822, 231.9059043, 229.1189729,
                   223.6077529, 223.4078709, 232.0322507, 229.1443491,
                   223.9583704, 218.7462952, 229.7254175, 223.6897019,
                   225.6184965, 224.2978918, 228.6607585, 225.165179,
                   223.7727373, 225.0571493, 225.3401804, 228.0011634,
                   226.7108398, 226.4397613, 224.1463, 224.9234796,
                   227.4525954, 226.6950074, 224.2540149, 225.5714904,
                   225.3068053, 225.1027088, 225.1108022, 230.3352262,
                   223.9988596, 230.2433835, 225.3439938, 222.5584386,
                   227.8544017, 223.7621121, 226.3164527, 218.7138937,
                   221.2154648, 222.2482269, 223.2161673, 220.4958671,
                   220.099166, 222.2356338, 224.3058999, 219.9660346,
                   221.3463635, 219.5587031, 222.8101315, 224.3591502,
                   222.2997797, 224.469024, 219.8685739, 224.0744959,
                   229.1868557, 222.606317, 216.9129317, 222.1122826,
                   226.2392654, 221.5133196, 223.737215, 223.9150212,
                   217.3011947, 222.9104565, 223.7852383, 222.6953474,
                   217.2340643, 222.6789089, 217.1560849, 219.7575659,
                   216.9504445, 219.2700324, 215.8499645, 217.1645719,
                   212.807649, 217.1637734, 219.6538059, 220.0878403,
                   220.6305562, 224.0539266, 217.5173791, 212.2426321,
                   216.2300981, 216.2865351, 217.199587, 219.905211,
                   219.0307488, 218.4341911, 214.5781167, 220.8564646,
                   214.2563435, 217.5464998, 215.1810417, 221.1999039,
                   219.4330922, 219.4663203, 209.5394264, 220.6821159,
                   215.8915294, 218.4869774, 216.1444288, 218.5967805,
                   216.9683676, 215.6100006, 216.4583239, 216.9293374,
                   215.5896447, 221.5966907, 215.249164, 222.0065281,
                   216.5832865, 212.1619019, 216.0413432, 210.9413048,
                   208.2053429, 214.1523884, 216.422174, 218.3284808,
                   211.9775062, 213.6642785, 213.1285667, 218.6590225,
                   214.5790551, 211.3257712, 212.9903484, 215.3390504,
                   216.0733572, 218.2698162, 211.6007714, 212.780147,
                   213.0243143, 214.6688075, 220.1223284, 211.5700648,
                   209.9435292, 211.0786782, 208.812307, 213.2771414,
                   210.7096213, 208.7720333, 215.0440725, 206.6947962,
                   214.0581148, 212.2760147, 214.9501144, 209.0441954,
                   208.841896, 209.2630832, 209.7383755, 208.7552825,
                   215.5528964, 212.7290263, 215.1947524, 211.2645173,
                   210.5555002, 208.8201605, 213.4854027, 208.6892763,
                   211.5975131, 208.8458699, 210.8669257, 216.1038968,
                   214.756696, 209.8799836, 208.4799828, 212.2031342,
                   207.0655128, 205.5614865, 207.5427021, 213.6835986,
                   209.7751773, 209.8299776, 206.1431123, 210.6916957,
                   204.7205516, 213.9524561, 210.8362023, 207.8348778,
                   208.083749, 208.6342461, 207.4624949, 209.9593264])

def sd_cov_hat(sample_size: int,
               lag: int,
               noise_type: str,
               sd_type: str) -> float:
    """
    Computes an estimate of standard deviation for sample autocovariance, 
    for a given lag, sample size and sd type. 
    Upgrade considerations are described in
    LRV3a / computing 2 / project 2 / Threshold / sd_cov_hat(n, k, nType, estType)

    :param sample_size: Sample size for the sample autocovariance, whose variance we need. 
    :param lag: Lag for the sample autocovariance, whose variance we need. 
    :param noise_type: Noise type for the sample autocovariance, whose variance we need. 
    :param sd_type: block_est or native. Depends, which threshold - estimated or exact we want to use. 
    :return: A scalar value of estimated standard deviation. 
    """

    if sd_type == 'block_est':
        if lag == 0:
            if noise_type == "gaussian":
                value = 512.1593454
            elif noise_type == "bernoulli":
                value = 147.5176373
        elif lag == 1:
            if noise_type == "gaussian":
                value = 289.1486113
            elif noise_type == "bernoulli":
                value = 213.1219444
        else:
            value = bootstrap[lag]
    elif sd_type == 'native_sim':
        if lag == 0:
            if noise_type == "gaussian":
                value = 491.6375
            elif noise_type == "bernoulli":
                value = 144.7827951
        elif lag == 1:
            if noise_type == "gaussian":
                value = 271.12191
            elif noise_type == "bernoulli":
                value = 202.8997932
        else:
            value = native[lag]
    else:
        raise ValueError("'sd_type' should be equal 'block_est' or "
                         "'native_sim'")

    sd = np.sqrt(value) / np.sqrt(sample_size)

    return sd
