"""Trip state-machine and invariants, intentionally tiny teaching example."""
from dataclasses import dataclass, field
from enum import Enum

class Status(str,Enum):
    REQUESTED='requested'; CONFIRMED='confirmed'; IN_PROGRESS='in_progress'; COMPLETED='completed'; CANCELED='canceled'

TRANSITIONS={
    (Status.REQUESTED,'confirm'):Status.CONFIRMED,
    (Status.REQUESTED,'cancel'):Status.CANCELED,
    (Status.CONFIRMED,'board'):Status.IN_PROGRESS,
    (Status.CONFIRMED,'cancel'):Status.CANCELED,
    (Status.IN_PROGRESS,'finish'):Status.COMPLETED,
}

@dataclass
class Trip:
    trip_id:str
    status:Status=Status.REQUESTED
    active_assignment:str|None=None
    history:list[str]=field(default_factory=list)
    def apply(self,event:str):
        if (self.status,event) not in TRANSITIONS: raise ValueError(f'Illegal {event} in {self.status.value}')
        if event=='confirm' and not self.active_assignment: raise ValueError('confirmation requires assignment')
        self.status=TRANSITIONS[self.status,event]
        if self.status in (Status.COMPLETED,Status.CANCELED): self.active_assignment=None
        self.history.append(f'{event}:{self.status.value}')
        self.check()
    def check(self):
        if self.status in (Status.CONFIRMED,Status.IN_PROGRESS) and not self.active_assignment:
            raise AssertionError('active trip without assignment')
        if self.status in (Status.COMPLETED,Status.CANCELED) and self.active_assignment:
            raise AssertionError('terminal trip with active assignment')

if __name__=='__main__':
    t=Trip('trip-17',active_assignment='vehicle-04')
    for e in ('confirm','board','finish'):t.apply(e)
    print(t.status.value,t.history)
