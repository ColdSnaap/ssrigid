"""
WYCKOFF DATA
no - Space group number
bl - Bravais lattice
T - Triclinic
'Wyckoff letter' : [Multiplicity, Site symmetry, Wyckoff position]

1 - 2      Triclinic (Tri)  - 
3 - 15     Monoclinic (Mon)  b(c)
16 - 74    Orthorhombic (Orh)  a b c   
75 - 142   Tetragonal (Tet)  c a [110]
143 - 167  Trigonal (Tri)  c a [210]
168 - 194  Hexagonal (Hex)  c a [210]
195 - 230  Cubic (Cub)  a [111] [110]
"""
# importrant!
# check sg_89 ('x', 'x', 0.5) (2 2 2.)
sg = {'sg_1': {'s1': [1, ['1'], ('x', 'y', 'z'), 1]},

      'sg_2': {'s1': [1, ['-1'], (0, 0, 0), 1],
               's2': [1, ['-1'], (0, 0, 0.5), 0],
               's3': [1, ['-1'], (0, 0.5, 0), 0],
               's4': [1, ['-1'], (0.5, 0, 0), 0],
               's5': [1, ['-1'], (0.5, 0.5, 0), 0],
               's6': [1, ['-1'], (0.5, 0, 0.5), 0],
               's7': [1, ['-1'], (0, 0.5, 0.5), 0],
               's8': [1, ['-1'], (0.5, 0.5, 0.5), 0],
               's9': [2, ['1'], ('x', 'y', 'z'), 1]},

      'sg_3': {'s1': [1, ['2'], (0, 'y', 0), 1],
               's2': [1, ['2'], (0, 'y', 0.5), 0],
               's3': [1, ['2'], (0.5, 'y', 0), 0],
               's4': [1, ['2'], (0.5, 'y', 0.5), 0],
               's5': [2, ['1'], ('x', 'y', 'z'), 1]},

      'sg_4': {'s1': [2, ['1'], ('x', 'y', 'z'), 1]},

      'sg_5': {'s1': [2, ['2'], (0, 'y', 0), 1],
               's2': [2, ['2'], (0, 'y', 0.5), 0],
               's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_6': {'s1': [1, ['m'], ('x', 0, 'z'), 1],
               's2': [1, ['m'], ('x', 0.5, 'z'), 0],
               's3': [2, ['1'], ('x', 'y', 'z'), 1]},

      'sg_7': {'s1': [2, ['1'], ('x', 'y', 'z'), 1]},

      'sg_8': {'s1': [2, ['m'], ('x', 0, 'z'), 1],
               's2': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_9': {'s1': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_10': {'s1': [1, ['2/m'], (0, 0, 0), 1],
                's2': [1, ['2/m'], (0, 1/2, 0), 0],
                's3': [1, ['2/m'], (0, 0, 0.5), 0],
                's4': [1, ['2/m'], (0.5, 0, 0), 0],
                's5': [1, ['2/m'], (0.5, 0.5, 0), 0],
                's6': [1, ['2/m'], (0, 0.5, 0.5), 0],
                's7': [1, ['2/m'], (0.5, 0, 0.5), 0],
                's8': [1, ['2/m'], (0.5, 0.5, 0.5), 0],
                's9': [2, ['2'], (0, 'y', 0), 1],
                's10': [2, ['2'], (0.5, 'y', 0), 0],
                's11': [2, ['2'], (0, 'y', 0.5), 0],
                's12': [2, ['2'], (0.5, 'y', 0.5), 0],
                's13': [2, ['m'], ('x', 0, 'z'), 1],
                's14': [2, ['m'], ('x', 0.5, 'z'), 0],
                's15': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_11': {'s1': [2, ['-1'], (0, 0, 0), 1],
                's2': [2, ['-1'], (0.5, 0, 0), 0],
                's3': [2, ['-1'], (0, 0, 0.5), 0],
                's4': [2, ['-1'], (0.5, 0, 0.5), 0],
                's5': [2, ['m'], ('x', 0.25, 'z'), 1],
                's6': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_12': {'s1': [2, ['2/m'], (0, 0, 0), 1],
                's2': [2, ['2/m'], (0, 0.5, 0), 0],
                's3': [2, ['2/m'], (0, 0, 0.5), 0],
                's4': [2, ['2/m'], (0, 0.5, 0.5), 0],
                's5': [4, ['-1'], (0.25, 0.25, 0), 1],
                's6': [4, ['-1'], (0.25, 0.25, 0.5), 0],
                's7': [4, ['2'], (0, 'y', 0), 1],
                's8': [4, ['2'], (0, 'y', 0.5), 0],
                's9': [4, ['m'], ('x', 0, 'z'), 1],
                's10': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_13': {'s1': [2, ['-1'], (0, 0, 0), 1],
                's2': [2, ['-1'], (0.5, 0.5, 0), 0],
                's3': [2, ['-1'], (0, 0.5, 0), 0],
                's4': [2, ['-1'], (0.5, 0, 0), 0],
                's5': [2, ['2'], (0, 'y', 0.25), 1],
                's6': [2, ['2'], (0.5, 'y', 0.25), 0],
                's7': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_14': {'s1': [2, ['-1'], (0, 0, 0), 1],
                's2': [2, ['-1'], (0.5, 0, 0), 0],
                's3': [2, ['-1'], (0, 0, 0.5), 0],
                's4': [2, ['-1'], (0.5, 0, 0.5), 0],
                's5': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_15': {'s1': [4, ['-1'], (0, 0, 0), 1],
                's2': [4, ['-1'], (0, 0.5, 0), 0],
                's3': [4, ['-1'], (0.25, 0.25, 0), 0],
                's4': [4, ['-1'], (0.25, 0.25, 0.5), 0],
                's5': [4, ['2'], (0, 'y', 0.25), 1],
                's6': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_16': {'s1': [2, ['x', 'y', '2'], (0.5, 0.5, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 0],
                's3': [2, ['x', 'y', '2'], (0.5, 0, 'z'), 0],
                's4': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [2, ['x', '2', 'z'], (0.5, 'y', 0.5), 1],
                's6': [2, ['x', '2', 'z'], (0.5, 'y', 0), 0],
                's7': [2, ['x', '2', 'z'], (0, 'y', 0.5), 0],
                's8': [2, ['x', '2', 'z'], (0, 'y', 0), 0],
                's9': [2, ['2', 'y', 'z'], ('x', 0.5, 0.5), 1],
                's10': [2, ['2', 'y', 'z'], ('x', 0.5, 0), 0],
                's11': [2, ['2', 'y', 'z'], ('x', 0, 0.5), 0],
                's12': [2, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's13': [2, ['2', '2', '2'], (0.5, 0.5, 0.5), 1],
                's14': [2, ['2', '2', '2'], (0, 0.5, 0.5), 1],
                's15': [2, ['2', '2', '2'], (0.5, 0, 0.5), 1],
                's16': [2, ['2', '2', '2'], (0.5, 0.5, 0), 1],
                's17': [2, ['2', '2', '2'], (0, 0, 0.5), 1],
                's18': [2, ['2', '2', '2'], (0, 0.5, 0), 1],
                's19': [2, ['2', '2', '2'], (0.5, 0, 0), 1],
                's20': [2, ['2', '2', '2'], (0, 0, 0), 1],
                's21': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_17': {'s1': [2, ['x', '2', 'z'], (0.5, 'y', 0.25), 1],
                's2': [2, ['x', '2', 'z'], (0, 'y', 0.25), 0],
                's3': [2, ['2', 'y', 'z'], ('x', 0.25, 0), 1],
                's4': [2, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's5': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_18': {'s1': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_19': {'s1': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_20': {'s1': [4, ['x', '2', 'z'], (0, 'y', 0.25), 1],
                's2': [4, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's3': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_21': {'s1': [4, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 0],
                's3': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [4, ['x', '2', 'z'], (0, 'y', 0.5), 1],
                's5': [4, ['x', '2', 'z'], (0, 'y', 0), 0],
                's6': [4, ['2', 'y', 'z'], ('x', 0, 0.5), 1],
                's7': [4, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's8': [2, ['2', '2', '2'], (0, 0, 0.5), 1],
                's9': [2, ['2', '2', '2'], (0.5, 0, 0.5), 0],
                's10': [2, ['2', '2', '2'], (0, 0.5, 0), 0],
                's11': [2, ['2', '2', '2'], (0, 0, 0), 0],
                's12': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_22': {'s1': [8, ['2', 'y', 'z'], ('x', 0.25, 0.25), 1],
                's2': [8, ['x', '2', 'z'], (0.25, 'y', 0.25), 1],
                's3': [8, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's4': [8, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [8, ['x', '2', 'z'], (0, 'y', 0), 0],
                's6': [8, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's7': [4, ['2', '2', '2'], (0.25, 0.25, 0.75), 1],
                's8': [4, ['2', '2', '2'], (0.25, 0.25, 0.25), 0],
                's9': [4, ['2', '2', '2'], (0, 0, 0.5), 0],
                's10': [4, ['2', '2', '2'], (0, 0, 0), 0],
                's11': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_23': {'s1': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['x', '2', 'z'], (0.5, 'y', 0), 1],
                's4': [4, ['x', '2', 'z'], (0, 'y', 0), 0],
                's5': [4, ['2', 'y', 'z'], ('x', 0, 0.5), 1],
                's6': [4, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's7': [2, ['2', '2', '2'], (0, 0.5, 0), 1],
                's8': [2, ['2', '2', '2'], (0, 0, 0.5), 0],
                's9': [2, ['2', '2', '2'], (0.5, 0, 0), 0],
                's10': [2, ['2', '2', '2'], (0, 0, 0), 0],
                's11': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_24': {'s1': [4, ['x', 'y', '2'], (0, 0.25, 'z'), 1],
                's2': [4, ['x', '2', 'z'], (0.25, 'y', 0), 1],
                's3': [4, ['2', 'y', 'z'], ('x', 0, 0.25), 1],
                's4': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_25': {'s1': [2, ['m', 'y', 'z'], (0.5, 'y', 'z'), 1],
                's2': [2, ['m', 'y', 'z'], (0, 'y', 'z'), 0],
                's3': [2, ['x', 'm', 'z'], ('x', 0.5, 'z'), 1],
                's4': [2, ['x', 'm', 'z'], ('x', 0, 'z'), 0],
                's5': [1, ['m', 'm', '2'], (0.5, 0.5, 'z'), 1],
                's6': [1, ['m', 'm', '2'], (0.5, 0, 'z'), 0],
                's7': [1, ['m', 'm', '2'], (0, 0.5, 'z'), 0],
                's8': [1, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's9': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_26': {'s1': [2, ['m', 'y', 'z'], (0.5, 'y', 'z'), 1],
                's2': [2, ['m', 'y', 'z'], (0, 'y', 'z'), 0],
                's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_27': {'s1': [2, ['x', 'y', '2'], (0.5, 0.5, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0.5, 0, 'z'), 0],
                's3': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 0],
                's4': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_28': {'s1': [2, ['m', 'y', 'z'], (0.25, 'y', 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's3': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_29': {'s1': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_30': {'s1': [2, ['x', 'y', '2'], (0.5, 0, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_31': {'s1': [2, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [4, ['1'], ('x', 'y', 'z'), 1]},
      
      'sg_32': {'s1': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_33': {'s1': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_34': {'s1': [2, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [2, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['1'], ('x', 'y', 'z'), 1]},

      'sg_35': {'s1': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's3': [4, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's4': [2, ['m', 'm', '2'], (0, 0.5, 'z'), 1],
                's5': [2, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's6': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_36': {'s1': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_37': {'s1': [4, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 0],
                's3': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_38': {'s1': [4, ['m', 'y', 'z'], (0.5, 'y', 'z'), 1],
                's2': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 0],
                's3': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's4': [2, ['m', 'm', '2'], (0.5, 0, 'z'), 1],
                's5': [2, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's6': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_39': {'s1': [4, ['x', 'm', 'z'], ('x', 0.25, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0.5, 0, 'z'), 1],
                's3': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_40': {'s1': [4, ['m', 'y', 'z'], (0.25, 'y', 'z'), 1],
                's2': [4, ['x', 'y', 'm'], (0, 0, 'z'), 1],
                's3': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_41': {'s1': [4, ['x', 'y', '2'], (0, 0, 'z'), 1],
                's2': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_42': {'s1': [8, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's2': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's3': [8, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's4': [4, ['m', 'm', '2'], (0, 0, 'z'), 1],
                's5': [16, ['1'], ('x', 'y', 'z')]},

      'sg_43': {'s1': [8, ['x', 'y', '2'], (0, 0, 'z'), 1],
                's2': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_44': {'s1': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's3': [2, ['m', 'm', '2'], (0, 0.5, 'z'), 1],
                's4': [2, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's5': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_45': {'s1': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_46': {'s1': [4, ['m', 'y', 'z'], (0.25, 'y', 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_47': {'s1': [4, ['x', 'y', 'm'], ('x', 'y', 0.5), 1],
                's2': [4, ['x', 'y', 'm'], ('x', 'y', 0), 0],
                's3': [4, ['x', 'm', 'z'], ('x', 0.5, 'z'), 1],
                's4': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 0],
                's5': [4, ['m', 'y', 'z'], (0.5, 'y', 'z'), 1],
                's6': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 0],
                's7': [2, ['m', 'm', '2'], (0.5, 0.5, 'z'), 1],
                's8': [2, ['m', 'm', '2'], (0.5, 0, 'z'), 0],
                's9': [2, ['m', 'm', '2'], (0, 0.5, 'z'), 0],
                's10': [2, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's11': [2, ['m', '2', 'm'], (0.5, 'y', 0.5), 1],
                's12': [2, ['m', '2', 'm'], (0.5, 'y', 0), 0],
                's13': [2, ['m', '2', 'm'], (0, 'y', 0.5), 0],
                's14': [2, ['m', '2', 'm'], (0, 'y', 0), 0],
                's15': [2, ['2', 'm', 'm'], ('x', 0.5, 0.5), 1],
                's16': [2, ['2', 'm', 'm'], ('x', 0.5, 0), 0],
                's17': [2, ['2', 'm', 'm'], ('x', 0, 0.5), 0],
                's18': [2, ['2', 'm', 'm'], ('x', 0, 0), 0],
                's19': [1, ['m', 'm', 'm'], (0.5, 0.5, 0.5), 1],
                's20': [1, ['m', 'm', 'm'], (0, 0.5, 0.5), 0],
                's21': [1, ['m', 'm', 'm'], (0.5, 0.5, 0), 0],
                's22': [1, ['m', 'm', 'm'], (0, 0.5, 0), 0],
                's23': [1, ['m', 'm', 'm'], (0.5, 0, 0.5), 0],
                's24': [1, ['m', 'm', 'm'], (0, 0, 0.5), 0],
                's25': [1, ['m', 'm', 'm'], (0.5, 0, 0), 0],
                's26': [1, ['m', 'm', 'm'], (0, 0, 0), 0],
                's27': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_48': {'s1': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['x', '2', 'z'], (0.5, 'y', 0), 1],
                's4': [4, ['x', '2', 'z'], (0, 'y', 0), 0],
                's5': [4, ['2', 'y', 'z'], ('x', 0, 0.5), 1],
                's6': [4, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's7': [4, ['-1'], (0.75, 0.75, 0.75), 1],
                's8': [4, ['-1'], (0.25, 0.25, 0.25), 0],
                's9': [2, ['2', '2', '2'], (0, 0.5, 0), 1],
                's10': [2, ['2', '2', '2'], (0, 0, 0.5), 0],
                's11': [2, ['2', '2', '2'], (0.5, 0, 0), 0],
                's12': [2, ['2', '2', '2'], (0, 0, 0), 0],
                's13': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_49': {'s1': [4, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [4, ['x', 'y', '2'], (0.5, 0, 'z'), 1],
                's3': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 0],
                's4': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [4, ['x', '2', 'z'], (0.5, 'y', 0.25), 1],
                's6': [4, ['x', '2', 'z'], (0, 'y', 0.25), 0],
                's7': [4, ['2', 'y', 'z'], ('x', 0.5, 0.25), 1],
                's8': [4, ['2', 'y', 'z'], ('x', 0, 0.25), 0],
                's9': [2, ['2', '2', '2'], (0.5, 0.5, 0.25), 1],
                's10': [2, ['2', '2', '2'], (0, 0.5, 0.25), 0],
                's11': [2, ['2', '2', '2'], (0.5, 0, 0.25), 0],
                's12': [2, ['2', '2', '2'], (0, 0, 0.25), 0],
                's13': [2, ['x', 'y', '2/m'], (0.5, 0, 0), 1],
                's14': [2, ['x', 'y', '2/m'], (0, 0.5, 0), 0],
                's15': [2, ['x', 'y', '2/m'], (0.5, 0.5, 0), 0],
                's16': [2, ['x', 'y', '2/m'], (0, 0, 0), 0],
                's17': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_50': {'s1': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [4, ['x', '2', 'z'], (0, 'y', 0.5), 1],
                's4': [4, ['x', '2', 'z'], (0, 'y', 0), 0],
                's5': [4, ['2', 'y', 'z'], ('x', 0, 0.5), 1],
                's6': [4, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's7': [4, ['-1'], (0.25, 0.25, 0.5), 1],
                's8': [4, ['-1'], (0.25, 0.25, 0), 1],
                's9': [2, ['2', '2', '2'], (0, 0, 0.5), 1],
                's10': [2, ['2', '2', '2'], (0.5, 0, 0.5), 0],
                's11': [2, ['2', '2', '2'], (0.5, 0, 0), 0],
                's12': [2, ['2', '2', '2'], (0, 0, 0), 0],
                's13': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_51': {'s1': [4, ['m', 'y', 'z'], (0.25, 'y', 'z'), 1],
                's2': [4, ['x', 'm', 'z'], ('x', 0.5, 'z'), 1],
                's3': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 0],
                's4': [4, ['x', '2', 'z'], (0, 'y', 0.5), 1],
                's5': [4, ['x', '2', 'z'], (0, 'y', 0), 0],
                's6': [2, ['m', 'm', '2'], (0.25, 0.5, 'z'), 1],
                's7': [2, ['m', 'm', '2'], (0.25, 0, 'z'), 0],
                's8': [2, ['x', '2/m', 'z'], (0, 0.5, 0.5), 1],
                's9': [2, ['x', '2/m', 'z'], (0, 0, 0.5), 0],
                's10': [2, ['x', '2/m', 'z'], (0, 0.5, 0), 0],
                's11': [2, ['x', '2/m', 'z'], (0, 0.5, 0), 0],
                's12': [2, ['x', '2/m', 'z'], (0, 0, 0), 0],
                's13': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_52': {'s1': [4, ['2', 'y', 'z'], ('x', 0.25, 0.25), 1],
                's2': [4, ['x', 'y', '2'], (0.25, 0, 'z'), 1],
                's3': [4, ['-1'], (0, 0, 0.5), 1],
                's4': [4, ['-1'], (0, 0, 0), 0],
                's5': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_53': {'s1': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [4, ['x', '2', 'z'], (0.25, 'y', 0.25), 1],
                's3': [4, ['2', 'y', 'z'], ('x', 0.5, 0), 1],
                's4': [4, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's5': [2, ['2/m', 'y', 'z'], (0, 0.5, 0), 1],
                's6': [2, ['2/m', 'y', 'z'], (0.5, 0.5, 0), 0],
                's7': [2, ['2/m', 'y', 'z'], (0.5, 0, 0), 0],
                's8': [2, ['2/m', 'y', 'z'], (0, 0, 0), 0],
                's9': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_54': {'s1': [4, ['x', 'y', '2'], (0.25, 0.5, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0.25, 0, 'z'), 0],
                's3': [4, ['x', '2', 'z'], (0, 'y', 0.25), 1],
                's4': [4, ['-1'], (0, 0.5, 0), 1],
                's5': [4, ['-1'], (0, 0, 0), 0],
                's6': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_55': {'s1': [4, ['x', 'y', 'm'], ('x', 'y', 0.5), 1],
                's2': [4, ['x', 'y', 'm'], ('x', 'y', 0), 0],
                's3': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's4': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [2, ['x', 'y', '2/m'], (0, 0.5, 0.5), 1],
                's6': [2, ['x', 'y', '2/m'], (0, 0.5, 0), 0],
                's7': [2, ['x', 'y', '2/m'], (0, 0, 0.5), 0],
                's8': [2, ['x', 'y', '2/m'], (0, 0, 0), 0],
                's9': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_56': {'s1': [4, ['x', 'y', '2'], (0.25, 0.75, 'z'), 1],
                's2': [4, ['x', 'y', '2'], (0.25, 0.25, 'z'), 0],
                's3': [4, ['-1'], (0, 0, 0.5), 1],
                's4': [4, ['-1'], (0, 0, 0), 0],
                's5': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_57': {'s1': [4, ['x', 'y', 'm'], ('x', 'y', 0.25), 1],
                's2': [4, ['2', 'y', 'z'], ('x', 0.25, 0), 1],
                's3': [4, ['-1'], (0.5, 0, 0), 1],
                's4': [4, ['-1'], (0, 0, 0), 0],
                's5': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_58': {'s1': [4, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [4, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's3': [4, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [2, ['x', 'y', '2/m'], (0, 0.5, 0.5), 1],
                's5': [2, ['x', 'y', '2/m'], (0, 0.5, 0), 0],
                's6': [2, ['x', 'y', '2/m'], (0, 0, 0.5), 0],
                's7': [2, ['x', 'y', '2/m'], (0, 0, 0), 0],
                's8': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_59': {'s1': [4, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's2': [4, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's3': [4, ['-1'], (0.25, 0.25, 0.5), 1],
                's4': [4, ['-1'], (0.25, 0.25, 0), 0],
                's5': [2, ['m', 'm', '2'], (0, 0.5, 'z'), 1],
                's6': [2, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's7': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_60': {'s1': [4, ['x', '2', 'z'], (0, 'y', 0.25), 1],
                's2': [4, ['-1'], (0, 0.5, 0), 1],
                's3': [4, ['-1'], (0, 0, 0), 0],
                's4': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_61': {'s1': [4, ['-1'], (0, 0, 0.5), 1],
                's2': [4, ['-1'], (0, 0, 0), 0],
                's3': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_62': {'s1': [4, ['x', 'm', 'z'], ('x', 0.25, 'z'), 1],
                's2': [4, ['-1'], (0, 0, 0.5), 1],
                's3': [4, ['-1'], (0, 0, 0), 0],
                's4': [8, ['1'], ('x', 'y', 'z'), 1]},

      'sg_63': {'s1': [8, ['x', 'y', 'm'], ('x', 'y', 0.25), 1],
                's2': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's3': [8, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's4': [8, ['-1'], (0.25, 0.25, 0), 1],
                's5': [4, ['m', '2', 'm'], (0, 'y', 0.25), 1],
                's6': [4, ['2/m', 'y', 'z'], (0, 0.5, 0), 1],
                's7': [4, ['2/m', 'y', 'z'], (0, 0, 0), 0],
                's8': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_64': {'s1': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's2': [8, ['x', '2', 'z'], (0.25, 'y', 0.25), 1],
                's3': [8, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's4': [8, ['-1'], (0.25, 0.25, 0), 1],
                's5': [4, ['2/m', 'y', 'z'], (0.5, 0, 0), 1],
                's6': [4, ['2/m', 'y', 'z'], (0.5, 0, 0), 0],
                's7': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_65': {'s1': [8, ['x', 'y', 'm'], ('x', 'y', 0.5), 1],
                's2': [8, ['x', 'y', 'm'], ('x', 'y', 0), 0],
                's3': [8, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's4': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's5': [8, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's6': [4, ['m', 'm', '2'], (0, 0.5, 'z'), 1],
                's7': [4, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's8': [4, ['m', '2', 'm'], (0, 'y', 0.5), 1],
                's9': [4, ['m', '2', 'm'], (0, 'y', 0), 0],
                's10': [4, ['2', 'm', 'm'], ('x', 0, 0.5), 1],
                's11': [4, ['2', 'm', 'm'], ('x', 0, 0), 0],
                's12': [4, ['x', 'y', '2/m'], (0.25, 0.25, 0.5), 1],
                's13': [4, ['x', 'y', '2/m'], (0.25, 0.25, 0), 0],
                's14': [2, ['m', 'm', 'm'], (0, 0, 0.5), 1],
                's15': [2, ['m', 'm', 'm'], (0.5, 0, 0.5), 0],
                's16': [2, ['m', 'm', 'm'], (0.5, 0, 0), 0],
                's17': [2, ['m', 'm', 'm'], (0, 0, 0), 0],
                's18': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_66': {'s1': [8, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [8, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's3': [8, ['x', 'y', '2'], (0, 0.25, 'z'), 0],
                's4': [8, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's5': [8, ['x', '2', 'z'], (0, 'y', 0.25), 1],
                's6': [8, ['2', 'y', 'z'], ('x', 0, 0.25), 1],
                's7': [4, ['x', 'y', '2/m'], (0.25, 0.75, 0), 1],
                's8': [4, ['x', 'y', '2/m'], (0.25, 0.25, 0), 0],
                's9': [4, ['x', 'y', '2/m'], (0, 0.5, 0), 0],
                's10': [4, ['x', 'y', '2/m'], (0, 0, 0), 0],
                's11': [4, ['2', '2', '2'], (0, 0.5, 0.25), 1],
                's12': [4, ['2', '2', '2'], (0, 0, 0.25), 0],
                's13': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_67': {'s1': [8, ['x', 'm', 'z'], ('x', 0.25, 'z'), 1],
                's2': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's3': [8, ['x', 'y', '2'], (0.25, 0, 'z'), 1],
                's4': [8, ['x', '2', 'z'], (0.25, 'y', 0.5), 1],
                's5': [8, ['x', '2', 'z'], (0.25, 'y', 0), 0],
                's6': [8, ['2', 'y', 'z'], ('x', 0, 0.5), 1],
                's7': [8, ['2', 'y', 'z'], ('x', 0, 0), 0],
                's8': [4, ['m', 'm', '2'], (0, 0.25, 'z'), 1],
                's9': [4, ['x', '2/m', 'z'], (0.25, 0.25, 0.5), 1],
                's10': [4, ['x', '2/m', 'z'], (0.25, 0.25, 0), 0],
                's11': [4, ['2/m', 'y', 'z'], (0, 0, 0.5), 1],
                's12': [4, ['2/m', 'y', 'z'], (0, 0, 0), 0],
                's13': [4, ['2', '2', '2'], (0.25, 0, 0.5), 1],
                's14': [4, ['2', '2', '2'], (0.25, 0, 0), 0],
                's15': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_68': {'s1': [8, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's2': [8, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's3': [8, ['x', '2', 'z'], (0, 'y', 0), 1],
                's4': [8, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's5': [8, ['-1'], (0, 0.25, 0.25), 1],
                's6': [8, ['-1'], (0.25, 0, 0.25), 0],
                's7': [4, ['2', '2', '2'], (0, 0, 0.5), 1],
                's8': [4, ['2', '2', '2'], (0, 0, 0), 0],
                's9': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_69': {'s1': [16, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [16, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's3': [16, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's4': [16, ['2', 'y', 'z'], ('x', 0.25, 0.25), 1],
                's5': [16, ['x', '2', 'z'], (0.25, 'y', 0.25), 1],
                's6': [16, ['x', 'y', '2'], (0.25, 0.25, 'z'), 1],
                's7': [8, ['m', 'm', '2'], (0, 0, 'z'), 1],
                's8': [8, ['m', '2', 'm'], (0, 'y', 0), 1],
                's9': [8, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's10': [8, ['2', '2', '2'], (0.25, 0.25, 0.25), 1],
                's11': [8, ['x', 'y', '2/m'], (0.25, 0.25, 0), 1],
                's12': [8, ['x', '2/m', 'z'], (0.25, 0, 0.25), 0],
                's13': [8, ['2/m', 'y', 'z'], (0, 0.25, 0.25), 0],
                's14': [4, ['m', 'm', 'm'], (0, 0, 0.5), 1],
                's15': [4, ['m', 'm', 'm'], (0, 0, 0), 1],
                's16': [32, ['1'], ('x', 'y', 'z'), 1]},

      'sg_70': {'s1': [16, ['x', 'y', '2'], (0, 0, 'z'), 1],
                's2': [16, ['x', '2', 'z'], (0, 'y', 0), 1],
                's3': [16, ['2', 'y', 'z'], ('x', 0, 0), 1],
                's4': [16, ['-1'], (0.625, 0.625, 0.625), 1],
                's5': [16, ['-1'], (0.125, 0.125, 0.125), 0],
                's6': [8, ['2', '2', '2'], (0, 0, 0.5), 1],
                's7': [8, ['2', '2', '2'], (0, 0, 0), 0],
                's8': [32, ['1'], ('x', 'y', 'z'), 1]},

      'sg_71': {'s1': [8, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [8, ['x', 'm', 'z'], ('x', 0, 'z'), 1],
                's3': [8, ['m', 'y', 'z'], (0, 'y', 'z'), 1],
                's4': [8, ['-1'], (0.25, 0.25, 0.25), 1],
                's5': [4, ['m', 'm', '2'], (0.5, 0, 'z'), 1],
                's6': [4, ['m', 'm', '2'], (0, 0, 'z'), 0],
                's7': [4, ['m', '2', 'm'], (0, 'y', 0.5), 1],
                's8': [4, ['m', '2', 'm'], (0, 'y', 0), 0],
                's9': [4, ['2', 'm', 'm'], ('x', 0.5, 0), 1],
                's10': [4, ['2', 'm', 'm'], ('x', 0, 0), 0],
                's11': [2, ['m', 'm', 'm'], (0.5, 0, 0.5), 1],
                's12': [2, ['m', 'm', 'm'], (0.5, 0.5, 0), 0],
                's13': [2, ['m', 'm', 'm'], (0, 0.5, 0.5), 0],
                's14': [2, ['m', 'm', 'm'], (0, 0, 0), 0],
                's15': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_72': {'s1': [8, ['x', 'y', 'm'], ('x', 'y', 0), 1],
                's2': [8, ['x', 'y', '2'], (0, 0.5, 'z'), 1],
                's3': [8, ['x', 'y', '2'], (0, 0, 'z'), 0],
                's4': [8, ['x', '2', 'z'], (0, 'y', 0.25), 1],
                's5': [8, ['2', 'y', 'z'], ('x', 0, 0.25), 1],
                's6': [8, ['-1'], (0.25, 0.25, 0.25), 1],
                's7': [4, ['x', 'y', '2/m'], (0.5, 0, 0), 1],
                's8': [4, ['x', 'y', '2/m'], (0, 0, 0), 0],
                's9': [4, ['2', '2', '2'], (0.5, 0, 0.25), 1],
                's10': [4, ['2', '2', '2'], (0, 0, 0.25), 0],
                's11': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_73': {'s1': [8, ['x', 'y', '2'], (0, 0.25, 'z'), 1],
                's2': [8, ['x', '2', 'z'], (0.25, 'y', 0), 1],
                's3': [8, ['2', 'y', 'z'], ('x', 0, 0.25), 1],
                's4': [8, ['-1'], (0.25, 0.25, 0.25), 1],
                's5': [8, ['-1'], (0, 0, 0), 0],
                's6': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_74': {'s1': [8, ['x', 'm', 'z'], ('x', 0.25, 'z'), 1],
                's2': [8, ['m', 'x', 'z'], (0, 'y', 'z'), 1],
                's3': [8, ['x', '2', 'z'], (0.25, 'y', 0.25), 1],
                's4': [8, ['2', 'x', 'z'], ('x', 0, 0), 1],
                's5': [4, ['m', 'm', '2'], (0, 0.25, 'z'), 1],
                's6': [4, ['x', '2/m', 'z'], (0.25, 0.25, 0.75), 1],
                's7': [4, ['x', '2/m', 'z'], (0.25, 0.25, 0.25), 0],
                's8': [4, ['2/m', 'y', 'z'], (0, 0, 0.5), 1],
                's9': [4, ['2/m', 'y', 'z'], (0, 0, 0), 0],
                's10': [16, ['1'], ('x', 'y', 'z'), 1]},

      'sg_77': {'s1':[2, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's2':[2, ['2', 'y', 'z'], (0.5, 0.5, 'z')],
                's3':[2, ['2', 'y', 'z'], (0, 0, 'z')],
                's4':[4, ['1'], ('x', 'y', 'z')]},
      
      'sg_81':{'s1':[2, ['2', 'y', 'z'], (0, 0.5, 'z')],
               's2':[2, ['2', 'y', 'z'], (0.5, 0.5, 'z')],
               's3':[2, ['2', 'y', 'z'], (0, 0, 'z')],
               's4':[1, ['-4', 'y', 'z'], (0.5, 0.5, 0.5)],
               's5':[1, ['-4', 'y', 'z'], (0.5, 0.5, 0)],
               's6':[1, ['-4', 'y', 'z'], (0, 0, 0.5)],
               's7':[1, ['-4', 'y', 'z'], (0, 0, 0)],
               's8':[4, ['1'], ('x', 'y', 'z')]},
      
      'sg_82':{'s1':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
               's2':[4, ['2', 'y', 'z'], (0, 0, 'z')],
               's3':[2, ['-4', 'y', 'z'], (0, 0.5, 0.75)],
               's4':[2, ['-4', 'y', 'z'], (0, 0.5, 0.25)],
               's5':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
               's6':[2, ['-4', 'y', 'z'], (0, 0, 0)],
               's7':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_84':{'s1':[4, ['m', 'y', 'z'], ('x', 'y', 0)],
               's2':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
               's3':[4, ['2', 'y', 'z'], (0.5, 0.5, 'z')],
               's4':[4, ['2', 'y', 'z'], (0, 0, 'z')],
               's5':[2, ['-4', 'y', 'z'], (0.5, 0.5, 0.25)],
               's6':[2, ['-4', 'y', 'z'], (0, 0, 0.25)],
               's7':[2, ['2/m', 'y', 'z'], (0, 0.5, 0.5)],
               's8':[2, ['2/m', 'y', 'z'], (0, 0.5, 0)],
               's9':[2, ['2/m', 'y', 'z'], (0.5, 0.5, 0)],
               's10':[2, ['2/m', 'y', 'z'], (0.5, 0.5, 0)],
               's11':[2, ['2/m', 'y', 'z'], (0, 0, 0)],
               's12':[8, ['1'], ('x', 'y', 'z')]},

      'sg_85':{'s1':[4, ['2', 'y', 'z'], (0, 0, 'z')],
               's2':[4, ['-1'], (0.25, 0.25, 0.5)],
               's3':[4, ['-1'], (0.25, 0.25, 0)],
               's4':[2, ['4'], (0, 0.25, 'z')],
               's5':[2, ['-4', 'y', 'z'], (0, 0, 0.25)],
               's6':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
               's7':[2, ['-4', 'y', 'z'], (0, 0, 0)],
               's8':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_86':{'s1':[4, ['2', 'y', 'z'], (0, 0, 'z')],
               's2':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
               's3':[4, ['-1'], (0.25, 0.25, 0.75)],
               's4':[4, ['-1'], (0.25, 0.25, 0.25)],
               's4':[2, ['4'], (0, 0.25, 'z')],
               's5':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
               's6':[2, ['-4', 'y', 'z'], (0, 0, 0)],
               's7':[8, ['1'], ('x', 'y', 'z')]},

      'sg_112':{'s1':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's2':[4, ['2', 'y', 'z'], (0.5, 0.5, 'z')],
                's3':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's4':[4, ['x', '2', 'z'], (0, 'y', 0.25)],
                's5':[4, ['x', '2', 'z'], ('x', 0.5, 0.25)],
                's6':[4, ['x', '2', 'z'], (0.5, 'y', 0.25)],
                's7':[4, ['x', '2', 'z'], ('x', 0, 0.25)],
                's8':[2, ['-4', 'y', 'z'], (0.5, 0.5, 0)],
                's9':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's10':[2, ['2', '2', '2'], (0, 0.5, 0.25)],
                's11':[2, ['2', '2', '2'], (0.5, 0.5, 0.25)],
                's12':[2, ['2', '2', '2'], (0.5, 0, 0.25)],
                's13':[2, ['2', '2', '2'], (0, 0, 0.25)],
                's14':[2, ['1'], ('x', 'y', 'z')]},
      
      'sg_113':{'s1':[4, ['x', 'y', 'm'], ('x', 'x+0.5', 'z')],
                's2':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's3':[2, ['2', 'm', 'm'], (0, 0.5, 'z')],
                's4':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
                's5':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's6':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_114':{'s1':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's2':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's3':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
                's4':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's5':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_116':{'s1':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's2':[4, ['2', 'y', 'z'], (0.5, 0.5, 'z')],
                's3':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's4':[4, ['x', 'y', '2'], ('x', 'x', 0.75)],
                's5':[4, ['x', 'y', '2'], ('x', 'x', 0.25)],
                's6':[2, ['-4', 'y', 'z'], (0.5, 0.5, 0)],
                's7':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's8':[2, ['2', '2', '2'], (0.5, 0.5, 0.25)],
                's9':[2, ['2', '2', '2'], (0, 0, 0.25)],
                's10':[8, ['1'], ('x', 'y', 'z')]},

      'sg_117':{'s1':[4, ['x', 'y', '2'], ('x', 'x+0.5', 0.5)],
                's2':[4, ['x', 'y', '2'], ('x', 'x+0.5', 0)],
                's3':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's4':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's5':[2, ['2', '2', '2'], (0, 0.5, 0.5)],
                's6':[2, ['2', '2', '2'], (0, 0.5, 0)],
                's7':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
                's8':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's9':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_118':{'s1':[4, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's2':[4, ['x', 'y', '2'], ('x', 'x+0.5', 0.25)],
                's3':[4, ['x', 'y', '2'], ('x', '-x+0.5', 0.25)],
                's4':[4, ['2', 'y', 'z'], (0, 0, 'z')],
                's5':[2, ['2', '2', '2'], (0, 0.5, 0.75)],
                's6':[2, ['2', '2', '2'], (0, 0.5, 0.25)],
                's7':[2, ['-4', 'y', 'z'], (0, 0, 0.5)],
                's8':[2, ['-4', 'y', 'z'], (0, 0, 0)],
                's9':[8, ['1'], ('x', 'y', 'z')]},
      
      'sg_121':{'s1':[8, ['x', 'y', 'm'], ('x', 'y', 'z')],
                's2':[8, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's3':[8, ['x', '2', 'z'], ('x', 0, 0.5)],
                's4':[8, ['x', '2', 'z'], ('x', 0, 0)],
                's5':[4, ['2', 'm', 'm'], (0, 0, 'z')],
                's6':[4, ['-4', 'y', 'z'], (0, 0.5, 0.25)],
                's7':[4, ['2', '2', '2'], (0, 0.5, 0)],
                's8':[2, ['-4', '2', 'm'], (0, 0, 0.5)],
                's9':[2, ['-4', '2', 'm'], (0, 0, 0)],
                's10':[16, ['1'], ('x', 'y', 'z')]},
      
      'sg_125':{'s1':[8, ['x', 'y', 'm'], ('x', 'x+0.5', 'z')],
                's2':[8, ['x', '2', 'z'], ('x', 0, 0.5)],
                's3':[8, ['x', '2', 'z'], ('x', 0, 0)],
                's4':[8, ['x', 'y', '2'], ('x', 'x', 0.5)],
                's5':[8, ['x', 'y', '2'], ('x', 'x', 0)],
                's6':[4, ['2', 'm', 'm'], (0, 0.5, 'z')],
                's7':[4, ['4', 'y', 'z'], (0, 0, 'z')],
                's8':[4, ['x', 'y', '2/m'], (0.25, 0.25, 0.5)],
                's9':[4, ['x', 'y', '2/m'], (0.25, 0.25, 0)],
                's10':[2, ['-4', '2', 'm'], (0, 0.5, 0.5)],
                's11':[2, ['-4', '2', 'm'], (0, 0.5, 0)],
                's12':[2, ['4', '2', '2'], (0, 0, 0.5)],
                's13':[2, ['4', '2', '2'], (0, 0, 0)],
                's14':[16, ['1'], ('x', 'y', 'z')]},
      
      'sg_132':{'s1':[8, ['x', 'y', 'm'], ('x', 'x', 'z')],
                's2':[8, ['m', 'y', 'z'], ('x', 'x', 0)],
                's3':[8, ['x', '2', 'z'], ('x', 0.5, 0.25)],
                's4':[8, ['x', '2', 'z'], ('x', 0, 0.25)],
                's5':[8, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's6':[4, ['m', '2', 'm'], ('x', 'x', 0.5)],
                's7':[4, ['m', '2', 'm'], ('x', 'x', 0)],
                's8':[4, ['2', 'm', 'm'], (0.5, 0.5, 'z')],
                's9':[4, ['2', 'm', 'm'], (0, 0, 'z')],
                's10':[4, ['2/m', 'y', 'z'], (0, 0.5, 0)],
                's11':[4, ['2', '2', '2'], (0, 0.5, 0.25)],
                's12':[2, ['-4', '2', 'm'], (0.5, 0.5, 0.25)],
                's13':[2, ['m', 'm', 'm'], (0.5, 0.5, 0)],
                's14':[2, ['-4', '2', 'm'], (0, 0, 0.25)],
                's15':[2, ['m', 'm', 'm'], (0, 0, 0)],
                's16':[16, ['1'], ('x', 'y', 'z')]},

      'sg_134':{'s1':[8, ['x', 'y', 'm'], ('x', 'x', 'z')],
                's2':[8, ['x', 'y', '2'], ('x', 'x+0.5', 0.75)],
                's3':[8, ['x', '2', 'z'], ('x', 'x+0.5', 0.25)],
                's4':[8, ['x', '2', 'z'], ('x', 0, 0.5)],
                's5':[8, ['x', '2', 'z'], ('x', 0, 0)],
                's6':[8, ['2', 'y', 'z'], (0, 0.5, 'z')],
                's7':[4, ['2', 'm', 'm'], (0, 0, 'z')],
                's8':[4, ['x', 'y', '2/m'], (0.75, 0.75, 0.75)],
                's9':[4, ['2', '2', '2'], (0, 0.5, 0.25)],
                's10':[4, ['2', '2', '2'], (0, 0.5, 0)],
                's11':[2, ['-4', '2', 'm'], (0, 0, 0.5)],
                's12':[2, ['-4', '2', 'm'], (0, 0, 0)],
                's13':[16, ['1'], ('x', 'y', 'z')]}


      }