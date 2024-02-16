from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    transform_number = State()
    calculate_number = State()