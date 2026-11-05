"""Idempotency and capacity in a toy single-process simulator. NOT production service."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Decision:
    trip:str; vehicle:str; accepted:bool; reason:str
class ReservationService:
    def __init__(self, vehicles):
        self.available=set(vehicles); self.assigned={}; self.replays={}
    def reserve(self,token,trip,vehicle):
        payload=(trip,vehicle)
        if token in self.replays:
            old_payload,old_result=self.replays[token]
            if old_payload!=payload: raise ValueError('same token different request')
            return old_result
        if trip in self.assigned:
            result=Decision(trip,vehicle,False,'trip already assigned')
        elif vehicle not in self.available:
            result=Decision(trip,vehicle,False,'vehicle unavailable')
        else:
            self.available.remove(vehicle);self.assigned[trip]=vehicle
            result=Decision(trip,vehicle,True,'reserved')
        self.replays[token]=(payload,result)
        return result
if __name__=='__main__':
    s=ReservationService(['V-1']);print(s.reserve('token-a','T-1','V-1'));print(s.reserve('token-a','T-1','V-1'))
