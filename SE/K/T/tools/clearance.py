"""Simplified secure-dispatch authorization demonstration, not production security."""
def permit(message, expected_route, latest_revision, now, issuer_active):
    return bool(message['signature_valid'] and issuer_active and
                message['route']==expected_route and
                message['revision']==latest_revision and
                0 <= now-message['issued_at'] <= 4 and
                message['action']=='CLEAR')

if __name__ == '__main__':
    m=dict(signature_valid=True,route='R1',revision=19,issued_at=10,action='CLEAR')
    print(permit(m,'R1',19,12,True),permit(m,'R1',20,12,True))
