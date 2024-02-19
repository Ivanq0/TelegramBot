from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    transform_number = State()
    calculate_number = State()
    input_first_number = State()
    input_second_number = State()