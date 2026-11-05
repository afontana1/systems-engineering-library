"""Two-factor/two-level effect contrasts with order (A-B-,A+B-,A-B+,A+B+)."""
def effects(y_mm,y_pm,y_mp,y_pp):
    a=(y_pm+y_pp-y_mm-y_mp)/2
    b=(y_mp+y_pp-y_mm-y_pm)/2
    interaction_difference=(y_pp-y_pm)-(y_mp-y_mm)
    return {'effect_A':a,'effect_B':b,'difference_of_differences':interaction_difference}

if __name__=='__main__':
    print('Waiting time effects:',effects(15,10,12,7))
