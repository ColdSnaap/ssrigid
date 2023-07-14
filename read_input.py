import os

def input_params():
    # Input file directory and name
    cwd = os.getcwd()
    sym_path = cwd + '/input_file/INPUT'
    isfile1 = os.path.isfile(sym_path)
    isfile = str(isfile1)
    if isfile == 'True':
        os.chdir(cwd + '/input_file')
        params = {}
        with open('INPUT', 'r') as input_read:
            for line in input_read:
                line = line.strip()
                if not line.startswith('#'):
                    key_value = line.split('=')
                    if len(key_value) == 2:
                        params[key_value[0].strip()] = key_value[1].strip()

    # Convert the parameters to desired types
    params['sym_no'] = int(params['sym_no'])
    params['rigid_type'] = str(params['rigid_type'])
    params['rigid_element'] = params['rigid_element'].split()
    params['single_element'] = params['single_element'].split()
    params['rigid_bond'] = float(params['rigid_bond'])
    params['atom_density'] = float(params['atom_density'])
    params['box_type'] = str(params['box_type'])
    params['dis_limit'] = float(params['dis_limit'])
    params['vol_start'] = float(params['vol_start'])
    params['vol_end'] = float(params['vol_start'])
    params['step_number'] = int(params['step_number'])
    params['internal_circulation'] = int(params['internal_circulation'])
    params['step_algorithm'] = str(params['step_algorithm'])
    params['temp_algorithm'] = str(params['temp_algorithm'])
    params['step_initial'] = float(params['step_initial'])
    params['step_final'] = float(params['step_final'])
    params['temp_initial'] = float(params['temp_initial'])
    params['temp_final'] = float(params['temp_final'])
    params['ratio'] = params['ratio'].split()
    for count, value in enumerate(params['ratio']):
        params['ratio'][count] = int(value)
    return params