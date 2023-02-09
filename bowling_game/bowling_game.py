
from typing import List
class RollImpossibleException(Exception):
    ...

class BowlingGame():
    _rounds: List[List[int]] = []

    def __init__(self):
        self._rounds = []

    def score(self) -> int:
        return sum(sum(round) for round in self._rounds)

    def roll(self, pins_hit: int):
        self._raise_on_illegal_roll(pins_hit)
        self._add_hit_pins_to_round(pins_hit)

    def _add_hit_pins_to_round(self, pins_hit: int) -> None:
        if self._is_first_round() or self._is_last_round_finished():
            self._rounds.append([pins_hit])
        else:
            self._rounds[-1].append(pins_hit)

    def _pins_left(self) -> int:
        if self._is_first_round() or self._is_last_round_finished():
            return 10
        else:
            last_round = self._rounds[-1]
            return 10 - last_round[0]

    def _is_first_round(self) -> bool:
        return len(self._rounds) == 0
    
    def _is_last_round_finished(self) -> bool:
        last_round = self._rounds[-1]
        return sum(last_round) == 10 or len(last_round) == 2
            

    def _raise_on_illegal_roll(self, pins_hit: int) -> None:
        if pins_hit > self._pins_left():
            raise RollImpossibleException()
        if pins_hit < 0:
            raise RollImpossibleException()
        
    
