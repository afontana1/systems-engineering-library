"""Dimensional arithmetic examples: does not infer tail latency or field reliability."""
def margin_ms(threshold_ms,segments_ms):
    if threshold_ms<0 or any(x<0 for x in segments_ms.values()):raise ValueError('nonnegative inputs required')
    return threshold_ms-sum(segments_ms.values())
def little_law(arrival_per_second,average_seconds):
    if arrival_per_second<0 or average_seconds<0:raise ValueError('nonnegative inputs required')
    return arrival_per_second*average_seconds
def downtime_minutes(availability_fraction,days):
    if not 0<=availability_fraction<=1 or days<0:raise ValueError('out of range')
    return (1-availability_fraction)*days*24*60
if __name__=='__main__':
    print('margin(ms):',margin_ms(900,{'ingress':80,'queue':150,'compute':120,'db':100,'egress':200}))
    print('average in flight:',little_law(25,0.4))
    print('downtime (minutes):',round(downtime_minutes(.999,30),2))
