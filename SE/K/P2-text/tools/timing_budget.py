"""Serial nominal timing budget; cannot establish tail-latency claims."""
def serial_budget(stages_ms, target_ms):
    if target_ms <= 0 or any(v < 0 for v in stages_ms.values()):
        raise ValueError('timing inputs must be nonnegative with positive target')
    total=sum(stages_ms.values())
    return {'nominal_total_ms':total,'nominal_margin_ms':target_ms-total,'nominal_within_target':total <= target_ms}

if __name__=='__main__':
    print(serial_budget({'ingress':80,'queue':150,'decision':120,'storage':100,'network':200},900))
