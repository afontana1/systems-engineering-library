"""Teaching-only zone release rule; not vehicle safety logic."""
def authorized(now, last_valid, zone_clear, signature_valid=True, revision_current=True):
    if now < last_valid: return False
    return all((signature_valid, revision_current, zone_clear, now-last_valid <= 6))

if __name__ == "__main__":
    for args in [(12,8,True),(12,4,True),(12,9,False)]: print(args,authorized(*args))
