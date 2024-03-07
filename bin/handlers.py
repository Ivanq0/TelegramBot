from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.handlers import callback_query
from aiogram.types import Message, KeyboardButtonPollType
from aiogram import flags
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery

import utils
from states import Gen

import kb
import text

router = Router()

operation_lst_calculate = ["", "", "", "", ""]
operation_lst_transform = ["", "", ""]


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.callback_query(F.data == "menu")
async def menu_return(clbck: CallbackQuery):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


# -------------------------------------------------------------------------------------------------------

@router.callback_query(F.data == "transform_number")
async def input_numbers(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.transform_number)
    await clbck.message.edit_text(text.transform_enter_number)


@router.message(Gen.transform_number)
@flags.chat_action("typing")
async def transform_system_from(msg: Message):
    operation_lst_transform[0] = msg.text
    await msg.answer(text.transform_choice_system_from, reply_markup=kb.choice_system_from)


@router.callback_query(F.data.in_({"from_two", "from_eight", "from_ten", "from_sixteen"}))
async def transform_system_to(clbck: CallbackQuery, state: FSMContext):
    operation_lst_transform[1] = clbck.data
    await clbck.message.edit_text(text.transform_choice_system_to, reply_markup=kb.choice_system_to)


@router.callback_query(F.data.in_({"to_two", "to_eight", "to_ten", "to_sixteen"}))
async def transform_number(clbck: CallbackQuery):
    operation_lst_transform[2] = clbck.data
    print(operation_lst_transform)
    res = await utils.transform(operation_lst_transform)
    if not res:
        return await clbck.message.answer(text.calculate_error, reply_markup=kb.iexit_kb)
    await clbck.message.edit_text(res, disable_web_page_preview=True, reply_markup=kb.iexit_kb)


# -------------------------------------------------------------------------------------------------------

@router.callback_query(F.data == "calculate_number")
async def first_number(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.calculate_number)
    await clbck.message.edit_text(text.calculate_choice_first_system, reply_markup=kb.choice_system_first)


@router.callback_query(F.data == "first_menu")
async def first_menu(clbck: CallbackQuery):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data.in_({"first_two", "first_eight", "first_ten", "first_sixteen"}))
async def first_number_system(clbck: CallbackQuery, state: FSMContext):
    operation_lst_calculate[0] = clbck.data
    await state.set_state(Gen.input_first_number)
    await clbck.message.edit_text(text.calculate_enter_first)


@router.message(Gen.input_first_number)
@flags.chat_action("Typing")
async def input_first(msg: Message):
    operation_lst_calculate[1] = msg.text
    await msg.answer(text.calculate_choice_second_system, reply_markup=kb.choice_system_second)


@router.callback_query(F.data == "second_menu")
async def second_menu(clbck: CallbackQuery):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data.in_({"second_two", "second_eight", "second_ten", "second_sixteen"}))
async def second_number_system(clbck: CallbackQuery, state: FSMContext):
    operation_lst_calculate[2] = clbck.data
    await state.set_state(Gen.input_second_number)
    await clbck.message.edit_text(text.calculate_enter_second)


@router.message(Gen.input_second_number)
@flags.chat_action("Typing")
async def input_second(msg: Message):
    operation_lst_calculate[3] = msg.text
    await msg.answer(text.calculate_choice_answer_system, reply_markup=kb.choice_operation)


@router.callback_query(F.data.in_({"plus", "minus", "multiply", "divide"}))
async def show_result(clbck: CallbackQuery):
    operation_lst_calculate[4] = clbck.data
    await clbck.message.edit_text(text.calculate_choice_answer_system, reply_markup=kb.choice_system_answer)


@router.callback_query(F.data == "third_menu")
async def third_menu(clbck: CallbackQuery):
    await clbck.message.edit_text(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data.in_({"answer_two", "answer_eight", "answer_ten", "answer_sixteen"}))
async def choice_answer(clbck: CallbackQuery):
    operation_lst_calculate.append(clbck.data)
    res = await utils.calculate_extended(operation_lst_calculate)
    if not res:
        return await clbck.message.answer(text.calculate_error, reply_markup=kb.iexit_kb)
    await clbck.message.edit_text(res, disable_web_page_preview=True, reply_markup=kb.iexit_kb)
