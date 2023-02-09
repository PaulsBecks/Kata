from typing import List
from pytest import fixture, mark, raises
from bowling_game.bowling_game import BowlingGame, RollImpossibleException

@fixture(autouse=True)
def bowling_game() -> BowlingGame:
    return BowlingGame()

def test_bowling_game_init(bowling_game: BowlingGame) -> None:
    # then
    assert bowling_game

def test_bowling_game_roll_executes_successfull(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(10)

def test_bowling_game_score_executes_successfully(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.score()

def test_bowling_game_score_returns_initial_score_of_zero(bowling_game: BowlingGame) -> None:
    # when
    score = bowling_game.score()

    # then
    assert score == 0

def test_bowling_game_roll_increases_score(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(10)
    score = bowling_game.score()
    print(bowling_game._rounds)

    # then 
    assert score == 10

@mark.parametrize("pins_left, pins_hit", [(10, 11),(9, 10), (4, 6), (1,2)])
def test_bowling_game_roll_cant_hit_more_pins_than_left_over(pins_left: int, pins_hit: int, bowling_game: BowlingGame) -> None:
    # given
    bowling_game.roll(10-pins_left)

    # when
    with raises(RollImpossibleException):
        bowling_game.roll(pins_hit) 

@mark.parametrize("pins_hit", [-1, -2, -100])
def test_bowling_game_roll_cant_hit_less_than_0_pins(pins_hit: int, bowling_game: BowlingGame) -> None:
    # when
    with raises(RollImpossibleException):
        bowling_game.roll(pins_hit)

def test_bowling_game_roll_increases_roll_count(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(3)
    assert len(bowling_game._rounds) == 1

@mark.parametrize("first_pins_hit, second_pins_hit", [(1, 1),(1, 9), (6, 3), (8,2)])
def test_bowling_game_two_valid_rolls_increment_round(first_pins_hit: int, second_pins_hit: int, bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(first_pins_hit)
    bowling_game.roll(second_pins_hit)

    # then
    assert len(bowling_game._rounds) == 1
    assert len(bowling_game._rounds[-1]) == 2

def test_bowling_game_strike_roll_increments_round(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(10)

    # then
    assert len(bowling_game._rounds) == 1

def test_bowling_game_roll_will_decrease_pins_left(bowling_game: BowlingGame) -> None:
    # when
    bowling_game.roll(8)

    # then 
    assert bowling_game._pins_left() == 2


def test_bowling_game(bowling_game: BowlingGame) -> None:
    pins_hit_in_rolls = [2,8,10,3,7,6,0,5,4,3,1,1,1,2,3,10,5,4]
    for pins_hit in pins_hit_in_rolls:
        bowling_game.roll(pins_hit)
    
    assert len(bowling_game._rounds) == 10

@mark.parametrize("rolls, expected_score", [([1,9,10], 30)])
def test_bowling_score_calculates_spares(rolls: List[int], expected_score:int , bowling_game: BowlingGame) -> None:
    # given
    for roll in rolls:
        bowling_game.roll(roll)
    
    # when
    score = bowling_game.score()

    # then
    assert score == expected_score

