// Educational SysML v2 textual *illustration*, not a conformant parser validation.
// Open in an official OMG pilot implementation before citing language conformance.
// Only a structural slice is shown; behavior and formal verification remain outside it.
package CampusMobility {
    part def SpeedSensor;
    part def BrakeSensor;
    part def DoorController;
    part def DispatchService;
    part def Shuttle {
        part speedSensor : SpeedSensor;
        part brakeSensor : BrakeSensor;
        part doorController : DoorController;
        part dispatch : DispatchService;
    }
    part campusShuttle : Shuttle;
}
