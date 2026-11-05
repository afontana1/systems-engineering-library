"""Present-value arithmetic with real cashflows and year-end timing."""
def present_cost(acquisition, annual_operating, years, rate):
    if years<0 or not isinstance(years,int) or rate<=-1: raise ValueError('invalid horizon/rate')
    return acquisition+sum(annual_operating/(1+rate)**t for t in range(1,years+1))

def annuity_factor(years,rate):
    if years<0 or not isinstance(years,int) or rate<=-1: raise ValueError('invalid horizon/rate')
    return sum(1/(1+rate)**t for t in range(1,years+1))

if __name__=='__main__':
    for acquisition,annual in ((1000,200),(1200,110)):
        print(round(present_cost(acquisition,annual,3,.05),2))
