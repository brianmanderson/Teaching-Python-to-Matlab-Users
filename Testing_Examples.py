def Example3_list_and_dict(x):
    if x[1] != 5:
        print('Messed up somewhere')
    else:
        print('Success!')
    return None
import numpy as np
def Example4_list_and_dict(dictionary):
    true_dictionary = {'Pat 1':{'Name':'John Smith','Age':52,'Image':np.zeros([512,512,50])}}
    if true_dictionary == dictionary:
        print('Success!')
    else:
        for key in true_dictionary['Pat 1'].keys():
            try:
                if dictionary['Pat 1'][key] != true_dictionary['Pat 1'][key]:
                    print('Off at ' + key)
            except:
                print('Off at ' + key)
        print('Try again')
    return None
if __name__ == '__main__':
    None
