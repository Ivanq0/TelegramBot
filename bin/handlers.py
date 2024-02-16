import time

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


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "calculate_number")
async def input_numbers(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.calculate_number)
    await clbck.message.edit_text(text.calculate_text)
    await clbck.message.answer(text.calculate_exit, reply_markup=kb.exit_kb)


@router.message(Gen.calculate_number)
@flags.chat_action("typing")
async def generate_text(msg: Message, state: FSMContext):
    problem = msg.text
    mesg = await msg.answer(text.calculate_wait)
    res = await utils.calculate(problem)
    if not res:
        return await mesg.edit_text(text.calculate_error, reply_markup=kb.iexit_kb)
    await mesg.edit_text(res, disable_web_page_preview=True)


@router.callback_query(F.data == "transform_number")
async def first_number(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(Gen.transform_number)
    await clbck.message.edit_text("Выберите систему счисления первого числа", reply_markup=kb.choice_system_first)


@router.callback_query(F.data == "first_two")
@router.callback_query(F.data == "first_three")
@router.callback_query(F.data == "first_eight")
@router.callback_query(F.data == "first_ten")
@router.callback_query(F.data == "first_sixteen")
async def second_number(clbck: CallbackQuery):
    utils.operation_lst.append(clbck.data)
    await clbck.message.edit_text("Выберите систему счисления второго числа", reply_markup=kb.choice_system_second)


@router.callback_query(F.data == "second_two")
@router.callback_query(F.data == "second_three")
@router.callback_query(F.data == "second_eight")
@router.callback_query(F.data == "second_ten")
@router.callback_query(F.data == "second_sixteen")
async def choice_operation(clbck: CallbackQuery):
    utils.operation_lst.append(clbck.data)
    await clbck.message.edit_text("Выберите операцию", reply_markup=kb.choice_operation)


@router.callback_query(F.data == "plus")
@router.callback_query(F.data == "minus")
@router.callback_query(F.data == "multiply")
@router.callback_query(F.data == "divide")
async def show_result(clbck: CallbackQuery):
    utils.operation_lst.append(clbck.data)
    await clbck.message.edit_text("В какой системе исчисления писать ответ?", reply_markup=kb.choice_system_answer)

@router.callback_query(F.data == "answer_two")
@router.callback_query(F.data == "answer_three")
@router.callback_query(F.data == "answer_eight")
@router.callback_query(F.data == "answer_ten")
@router.callback_query(F.data == "answer_sixteen")
async def choice_answer(clbck: CallbackQuery):
    utils.operation_lst.append(clbck.data)
    await clbck.message.edit_text("Вычисление потом добавлю...")
    time.sleep(3)
    await clbck.message.edit_text("Выберите операцию", reply_markup=kb.menu)
    print(utils.operation_lst)
    utils.operation_lst = []