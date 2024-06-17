from typing import List
import sorter as s
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''
Name:   Emily Lewis Dando
SID:    500687002
Unikey: elew6213

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class LaserCircuit:


    def __init__(self, width: int, height: int):
        '''        
        
         a LaserCircuit instance given a width and height. All 
        lists of components and photons are empty by default.
        board_displayer is initialised to a BoardDisplayer instance. clock is
        0 by default.

        emitters:        list[Emitter]  - all emitters in this circuit
        receivers:       list[Receiver] - all receivers in this circuit
        photons:         list[Photon]   - all photons in this circuit
        mirrors:         list[Mirror]   - all mirrors in this circuit
        width:           int            - the width of this circuit board
        height:          int            - the height of this circuit board
        board_displayer: BoardDisplayer - helper class for storing and 
                                          displaying the circuit board
        clock:           int            - a clock keeping track of how many 
                                          nanoseconds this circuit has run for

        Parameters
        ----------
        width  - the width to set this circuit board to
        height - the width to set this circuit board to
        '''
        self.emitters: list = []
        self.receivers: list = []
        self.photons: List[Photon] = []
        self.mirrors: list = []
        self.width: int = width
        self.height: int = height
        self.board_displayer: BoardDisplayer = BoardDisplayer(width, height)
        self.clock: int = 0

    def emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Gets each emitter in this circuit's list of emitters to emit a photon.
        The photons emitted should be added to this circuit's photons list.
        '''
        i = 0
        while i < len(self.emitters):
            p = Photon(self.emitters[i].x, self.emitters[i].y, self.emitters[i].frequency, self.emitters[i].direction)
            # p.move(self.width, self.height)
            self.add_photon(p)
            i += 1

    def is_finished(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Returns whether or not this circuit has finished running. The
        circuit is finished running if every photon in the circuit has been
        absorbed.

        Returns
        -------
        True if the circuit has finished running or not, else False.
        '''
        i = 0
        while i < len(self.photons):
            if self.photons[i].absorbed == False:
                return False
            i += 1
        return True


    def print_emit_photons(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for each emitter emitting a photon.
        
        It will also need to write the output into a
        /home/output/emit_photons.out output file. 
        
        You can assume the /home/output/ path exists.
        '''
        filename = "/home/output/emit_photons.out"
        fobj = open(filename, "w")
        print("0ns: Emitting photons.")
        i = 0
        while i < len(self.emitters):
            print(self.emitters[i].__str__())
            fobj.write(f"{self.emitters[i].__str__()}\n")
            # print(self.emitters.__str__, file=filename)
            i += 1
        fobj.close()

    def activated_receivers(self):
        i = 0
        self.get_receivers()
        active_receiver = []
        while i < len(self.receivers):
            # print(f"DEBUG: {self.receivers[i].symbol}: {self.receivers[i].activated}")
            if self.receivers[i].activated == True:
                active_receiver.append(self.receivers[i])
                i += 1
            else:
                i += 1
        return active_receiver
        


    def print_activation_times(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the activation times for each receiver, sorted
        by activation time in ascending order. Any receivers that have not
        been activated should not be included.
        
        It will also need to write the output into a
        /home/output/activation_times.out output file.

        You can assume the /home/output/ path exists.
        '''
        active = self.activated_receivers()
        
        #sort activated receivers
        sorted_receivers =  s.sort_receivers_by_activation_time(active)

        #print result
        print("Activation times:")
        filename =  "/home/output/activation_times.out"
        fobj = open(filename, "w")
        j = 0
        while j < len(sorted_receivers):
            print(f"{sorted_receivers[j].symbol}: {sorted_receivers[j].activation_time}ns")
            fobj.write(f"{sorted_receivers[j].symbol}: {sorted_receivers[j].activation_time}ns\n")
            #print(f"{sorted_receivers[j].symbol}: {sorted_receivers[j].activation_time}ns", filename)
            j += 1
        fobj.close()


    def print_total_energy(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Prints the output for the total energy absorbed for each receiver,
        sorted by total energy absorbed in descending order. Any receivers
        that have not been activated should not be included.
        
        It will also need to write the output into a
        /home/output/total_energy_absorbed.out output file.

        You can assume the /home/output/ path exists.
        '''
        #create list of activated receivers
        active = self.activated_receivers()
        
        #sort activated receivers
        sorted_receivers =  s.sort_receivers_by_total_energy(active)

        #print result
        print("Total energy absorbed:")
        filename =  "/home/output/total_energy.out"
        fobj = open(filename, "w")
        j = 0
        while j < len(sorted_receivers):
            print(f"{sorted_receivers[j].symbol}: {round(sorted_receivers[j].total_energy, 2)}eV ({sorted_receivers[j].photons_absorbed})")
            fobj.write(f"{sorted_receivers[j].symbol}: {round(sorted_receivers[j].total_energy, 2)}eV ({sorted_receivers[j].photons_absorbed})\n")
            #print(f"{sorted_receivers[j].symbol}: {sorted_receivers[j].total_energy}eV ({sorted_receivers[i].photons_absorbed})", filename)
            j += 1
        fobj.close()

    
    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()


    def get_collided_emitter(self, entity):
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another emitter in the 
        circuit. 

        If it does, return the emitter already in the entity's position.
        Else, return None, indicating there is no emitter occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        An emitter if it has the same position as entity, else None.
        '''
        i = 0
        while i < len(self.emitters):
            if self.emitters[i].x == entity.x and self.emitters[i].y == entity.y:
                return self.emitters[i]
            else:
                i += 1
        return None


    def get_collided_receiver(self, entity):
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another receiver in the 
        circuit. 

        If it does, return the receiver already in the entity's position.
        Else, return None, indicating there is no receiver occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A receiver if it has the same position as entity, else None.
        '''
        i = 0
        while i < len(self.receivers):
            if self.receivers[i].x == entity.x and self.receivers[i].y == entity.y:
                return self.receivers[i]
            else:
                i += 1
        return None


    def get_collided_mirror(self, entity):
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Takes in one argument entity which is either a component or a photon
        and checks if it has the same position as another mirror in the 
        circuit. 

        If it does, return the mirror already in the entity's position.
        Else, return None, indicating there is no mirror occupying entity's
        position.
        
        Parameter
        ---------
        entity - an emitter, receiver, photon or mirror

        Returns
        -------
        A mirror if it has the same position as entity, else None.
        '''
        #remove the line below once you start implementing this function
        i = 0
        while i < len(self.mirrors):
            if self.mirrors[i].x == entity.x and self.mirrors[i].y == entity.y:
                return self.mirrors[i]
            else:
                i += 1
        return None


    def get_collided_component(self, photon: Photon):
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Given a photon, returns the component it has collided with (if any).
        A collision occurs if the positions of photon and the component are
        the same.

        Parameters
        ----------
        photon - a photon to check for collision with the circuit's components

        Returns
        -------
        If the photon collided with a component, return that component.
        Else, return None.

        Hint
        ----
        Use the three collision methods above to handle this.
        '''
        if self.get_collided_emitter(photon) is not None:
            return self.get_collided_emitter(photon)
        elif self.get_collided_receiver(photon) is not None:
            return self.get_collided_receiver(photon)
        else:
            return None


    def tick(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs a single nanosecond (tick) of this circuit. If the circuit has
        already finished, this method should return out early.
        
        Otherwise, for each photon that has not been absorbed, this method is
        responsible for moving it, updating the board to show its new position
        and checking if it collided with a component (and handling it if did
        occur). At the end, we then increment clock.
        '''
        
        self.clock += 1
        if self.is_finished() == True:
            return None
        else:
            i = 0
            while i < len(self.photons):
                if self.photons[i].is_absorbed() == True:
                    i += 1
                    continue
                else:
                    self.photons[i].move(self.width, self.height)
                    self.board_displayer.add_photon_to_board(self.photons[i])

                    collided_component = self.get_collided_component(self.photons[i])
                    if collided_component is not None and collided_component.component_type == 'receiver':
                        self.photons[i].interact_with_component(collided_component, self.clock)
                    
                    collided_mirror = self.get_collided_mirror(self.photons[i])
                    if collided_mirror is not None:
                        self.photons[i].interact_with_component(collided_mirror, self.clock)
                    i += 1


    def run_circuit(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Runs the entire circuit from start to finish. This involves getting
        each emitter to emit a photon, and continuously running tick until the
        circuit is finished running. All output in regards of running the 
        circuit should be contained in this method.
        '''
        #print start message
        print('''
========================
   RUNNING CIRCUIT...
========================
''')
        
        #emitting photons
        self.emit_photons()
        self.print_emit_photons()
        print("")


        #tick
        while self.is_finished() == False:
            # print(f"pretick {self.clock}, {self.activated_receivers()}")
            self.tick()
            # print(f"posttick {self.clock}, {self.activated_receivers()}")
            # print(f" finished: {self.is_finished()}")
            if (self.is_finished()):
                break
            
            if self.clock % 5 == 0 and self.clock >= 5:
                print(f"{self.clock}ns: {len(self.activated_receivers())}/{len(self.receivers)} receiver(s) activated.")
                self.board_displayer.print_board()
                print("")

        print(f"{self.clock}ns: {len(self.activated_receivers())}/{len(self.receivers)} receiver(s) activated.")
        self.board_displayer.print_board()
        print("")

        #print receivers
        self.print_activation_times()
        print("")
        self.print_total_energy()

        print('''
========================
   CIRCUIT FINISHED!
========================''')
        
        

    def get_used_symbol(self, entity):
        i = 0
        while i < len(self.receivers):
            if self.receivers[i].symbol.strip('R') == entity.symbol.strip('R'):
                return self.receivers[i]
            else:
                i += 1
        j=0
        while j <  len(self.emitters):
            if self.emitters[j].symbol == entity.symbol:
                return self.emitters[j]
            else:
                j+=1
        return None
    
    def add_emitter(self, emitter: Emitter) -> bool:
        '''
        If emitter is not an Emitter instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The emitter's position is within the bounds of the circuit.
          2)  The emitter's position is not already taken by another emitter in
              the circuit.
          3)  The emitter's symbol is not already taken by another emitter in 
              the circuit.
          
        If at any point a check is not passed, an error message is printed
        stating the causeof the error and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur:
          1)  emitter is added in the circuit's list of emitters. emitter
              needs to be added such that the list of emitters remains sorted
              in alphabetical order by the emitter's symbol. You can assume the
              list of emitters is already sorted before you add the emitter.
          2)  emitter's symbol is added into board_displayer.
          3)  The method returns True.   

        Parameters
        ----------
        emitter - the emitter to add into this circuit's list of emitters

        Returns
        ----------
        Returns true if all checks are passed and the emitter is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        
        ----
        Use the get_collided_emitter method to check for position collision.
        You will need to find your own way to check for symbol collisions
        with other emitters.
        '''
        if self.valid_emitter(emitter) == True:
            self.ordered_emitter(emitter)
            self.board_displayer.add_component_to_board(emitter)
            return True
        else:
            return False
    
    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        return self.emitters

    def valid_emitter(self, emitter: Emitter):
        if emitter.component_type != 'emitter':
            return False
        else:
            if emitter.x <  self.width and emitter.y < self.height:
                if self.get_collided_emitter(emitter) == None:
                    if self.get_used_symbol(emitter) == None:
                        return True
                    else:
                        print(emitter)
                        print(f"Error Symbol {self.get_used_symbol(emitter)} is already taken.")
                        return False
                else:
                    print(f"Error: position ({emitter.x}, {emitter.y}) is already taken by emitter '{self.get_collided_emitter(emitter).symbol}'")
                    return False
            else:
                print(f"Error: position ({emitter.x}, {emitter.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
                return False
    
    def add_receiver(self, receiver: Receiver) -> bool:
        '''
        If receiver is not a Receiver instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The receiver's position is within the bounds of the circuit.
          2)  The receiver's position is not already taken by another emitter
              or receiver in the circuit.
          3)  The receiver's symbol is not already taken by another receiver in
              the circuit. 
             
        If at any point a check is not passed, an error message is printed stating
        the cause of the error and returns False, skipping any further checks. If 
        all checks pass, then the following needs to occur:
          1)  receiver is added in the circuit's list of receivers. receiver
              needs to be added such that the list of receivers  remains sorted
              in alphabetical order by the receiver's symbol. You can assume the
              list of receivers is already sorted before you add the receiver. 
          2)  receiver's symbol is added into board_displayer.
          3)  The method returns True.

        Parameters
        ----------
        receiver - the receiver to add into this circuit's list of receivers

        Returns
        ----------
        Returns true if all checks are passed and the receiver is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.

        Hint
        ----
        Use the get_collided_emitter and get_collided_receiver methods to
        check for position collisions.
        You will need to find your own way to check for symbol collisions
        with other receivers.
        '''
        if self.valid_receiver(receiver) == True:
            self.ordered_receiver(receiver)
            self.board_displayer.add_component_to_board(receiver)
            return True
        else:
            return False
            
    def valid_receiver(self, receiver: Receiver):
        if receiver.component_type != 'receiver':
            return False
        else:
            if receiver.x <  self.width and receiver.y < self.height:
                if self.get_collided_receiver(receiver) is None:
                    if self.get_collided_emitter(receiver) is None:
                        if self.get_used_symbol(receiver) == None:
                            return True
                        else:
                            print(f"Error: symbol '{self.get_used_symbol(receiver).symbol}' is already taken")
                            return False
                    else:
                        print(f"Error: position ({receiver.x}, {receiver.y}) is already taken by emitter '{self.get_collided_emitter(receiver).symbol}'")
                        return False
                else:
                    print(f"Error: position ({receiver.x}, {receiver.y}) is already taken by receiver '{self.get_collided_receiver(receiver).symbol}'")
                    return False
            else:
                print(f"Error: position ({receiver.x}, {receiver.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
                return False

    def ordered_emitter(self, emitter: Emitter):
        if len(self.emitters) == 0 or emitter.symbol > self.emitters[-1].symbol:
            self.emitters.append(emitter)
        elif emitter.symbol < self.emitters[0].symbol:
            self.emitters.insert(0, emitter)
        else:
            i = 1
            while i < len(self.emitters):
                if emitter.symbol < self.emitters[i].symbol:
                    self.emitters.insert(i, emitter)
                    break
                else:
                    i += 1  

    def ordered_receiver(self, receiver: Receiver):
        if len(self.receivers) == 0 or receiver.symbol.strip('R') > self.receivers[-1].symbol.strip('R'):
            self.receivers.append(receiver)
        elif receiver.symbol.strip('R') < self.receivers[0].symbol.strip('R'):
            self.receivers.insert(0, receiver)
        else:
            i = 1
            while i < len(self.receivers):
                if receiver.symbol.strip('R') < self.receivers[i].symbol.strip('R'):
                    self.receivers.insert(i, receiver)
                    break
                else:
                    i += 1   

    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        return self.receivers


    def add_photon(self, photon: Photon) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        If the photon passed in is not a Photon instance, it does not add it in
        and returns False. Else, it adds photon in this circuit's list of
        photons and returns True.

        Parameters
        ----------
        photon - the photon to add into this circuit's list of photons

        Returns
        -------
        Returns True if the photon is added in, else False.
        '''
        if photon.type == 'Photon':
            self.photons.append(photon)
            self.board_displayer.add_photon_to_board(photon)
            return True
        else:
            return False


    def get_photons(self) -> list[Photon]:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns photons.'''
        return self.photons


    def add_mirror(self, mirror: Mirror) -> bool:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        If mirror is not a Mirror instance, return False. Else, you need to
        perform the following checks in order for any errors:
          1)  The mirror's position is within the bounds of the circuit.
          2)  The mirror's position is not already taken by another emitter, 
              receiver or mirror in the circuit.
             
        If at any point a check is not passed, an error message is printed
        stating the cause of theerror and returns False, skipping any further
        checks. If all checks pass, then the following needs to occur: 
          1)  mirror is added in the circuit's list of mirrors.
          2) mirror's symbol is added into board_displayer.
          3)   The method returns True.

        Paramaters
        ----------
        mirror - the mirror to add into this circuit's list of mirrors

        Returns
        ----------
        Returns true if all checks are passed and the mirror is added into
        the circuit.
        Else, if any of the checks are not passed, prints an error message
        stating the cause of the error and returns False, skipping any
        remaining checks.
        '''
        if self.valid_mirror(mirror) == True:
            self.mirrors.append(mirror)
            self.board_displayer.add_component_to_board(mirror)
            return True
        else:
            return False
            
    def valid_mirror(self, mirror: Mirror):
        if mirror.get_component_type() != 'mirror':
            return False
        else:
            if mirror.x < self.width and mirror.y < self.height:
                if self.get_collided_emitter(mirror) == None:
                    if self.get_collided_receiver(mirror) == None:
                        if self.get_collided_mirror(mirror) == None:
                            return True
                        else:
                            print(f"Error: position ({mirror.x}, {mirror.y}) is already taken by mirror '{self.get_collided_mirror(mirror).symbol}'")
                            return False
                    else:
                        print(f"Error: position ({mirror.x}, {mirror.y}) is already taken by receiver '{self.get_collided_receiver(mirror).symbol}'")
                        return False
                else:
                    print(f"Error: position ({mirror.x}, {mirror.y}) is already taken by emitter '{self.get_collided_emitter(mirror).symbol}'")
                    return False
            else:
                print(f"Error: position ({mirror.x}, {mirror.y}) is out-of-bounds of {self.width}x{self.height} circuit board")
                return False


    def get_mirrors(self) -> list[Mirror]:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns mirrors.'''
        return self.mirrors

    
    def get_width(self) -> int:
        '''Returns width.'''
        return self.width


    def get_height(self) -> int:
        '''Returns height.'''
        return self.height

# e1 = Emitter('A',0,0)
# e2 = Emitter('B',6, 2)
# e3 = Emitter('C',13,0)
# e4 = Emitter('D',1,1)
# e1.set_pulse_sequence(90, "S")
# e2.set_pulse_sequence(70, "E")
# e3.set_pulse_sequence(70, "S")
# e4.set_pulse_sequence(900, "E")
# r0 = Receiver('R0', 0, 2)
# r1 = Receiver('R1', 13, 2)
# r2 = Receiver('R2', 11, 1)
# c = LaserCircuit(14,3)  
# c.add_emitter(e1)
# c.add_emitter(e2)
# c.add_emitter(e3)
# c.add_emitter(e4)
# c.add_receiver(r0)
# c.add_receiver(r1)
# c.add_receiver(r2)
# # #ph = Photon(1,4,232,'N')
# # #c.add_photon(ph)
# # # c.board_displayer.print_board()
# # # ph.move(8,8)
# # # c.add_photon(ph)
# c.run_circuit()

