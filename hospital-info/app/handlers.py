from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def echo(message: Message):
    answer = 'Приветствую! Я — чат-бот Белгородской областной клинической ' \
             'больницы Святителя Иоасафа. ' \
             'Если у вас возникли вопросы, вы можете задать их мне.'
    
    await message.answer(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    with open('app/info/about.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())


@router.callback_query(F.data == "main")
async def main(callback: CallbackQuery):
    answer = 'Приветствую! Я — чат-бот Белгородской областной клинической ' \
             'больницы Святителя Иоасафа. ' \
             'Если у Вас возникли вопросы, вы можете задать их мне.'
    
    await callback.message.edit_text(answer, reply_markup=kb.main_keyboard())


@router.callback_query(F.data == "work_time")
async def work_time(callback: CallbackQuery):
    with open('app/info/work_time.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())


@router.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    with open('app/info/contacts.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())
    

@router.callback_query(F.data == "driveway")
async def driveway(callback: CallbackQuery):
    with open('app/info/driveway.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.back_keyboard())
    

@router.callback_query(F.data == "faq")
async def faq(callback: CallbackQuery):
    await callback.message.edit_text('Выберите вопрос из списка 🔽',
                                     reply_markup=kb.faq_keyboard())
    

@router.callback_query(F.data == "hospitalization_rules")
async def hospitalization_rules(callback: CallbackQuery):
    with open('app/info/hospitalization_rules.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "hospitalization_length")
async def hospitalization_length(callback: CallbackQuery):
    with open('app/info/hospitalization_length.txt', 'r', encoding='utf-8') as file:
        answer = file.read()

    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "register_rules")
async def register_rules(callback: CallbackQuery):
    with open('app/info/register_rules.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "consultation_rules")
async def consultation_rules(callback: CallbackQuery):
    with open('app/info/consultation_rules.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "traumatology_consultation")
async def traumatology_consultation(callback: CallbackQuery):
    with open('app/info/traumatology_consultation.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "about_med_help")
async def about_med_help(callback: CallbackQuery):
    with open('app/info/about_med_help.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "med_help_availability")
async def med_help_availability(callback: CallbackQuery):
    with open('app/info/med_help_availability.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "rights_and_duties_1")
async def rights_and_duties(callback: CallbackQuery):
    with open('app/info/rights_and_duties_1.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.rights_and_duties_1_keyboard())
    

@router.callback_query(F.data == "rights_and_duties_2")
async def rights_and_duties_2(callback: CallbackQuery):
    with open('app/info/rights_and_duties_2.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.rights_and_duties_2_keyboard())
    

@router.callback_query(F.data == "rights_and_duties_3")
async def rights_and_duties_3(callback: CallbackQuery):
    with open('app/info/rights_and_duties_3.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.rights_and_duties_3_keyboard())
    

@router.callback_query(F.data == "rights_and_duties_4")
async def rights_and_duties_4(callback: CallbackQuery):
    with open('app/info/rights_and_duties_4.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.rights_and_duties_4_keyboard())
    

@router.callback_query(F.data == "rights_and_duties_5")
async def rights_and_duties_5(callback: CallbackQuery):
    with open('app/info/rights_and_duties_5.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.rights_and_duties_5_keyboard())
    

@router.callback_query(F.data == "health_protection_1")
async def health_protection_1(callback: CallbackQuery):
    with open('app/info/health_protection_1.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_1_keyboard())
    

@router.callback_query(F.data == "health_protection_2")
async def health_protection_2(callback: CallbackQuery):
    with open('app/info/health_protection_2.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_2_keyboard())


@router.callback_query(F.data == "health_protection_3")
async def health_protection_3(callback: CallbackQuery):
    with open('app/info/health_protection_3.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_3_keyboard())


@router.callback_query(F.data == "health_protection_4")
async def health_protection_4(callback: CallbackQuery):
    with open('app/info/health_protection_4.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_4_keyboard())
    

@router.callback_query(F.data == "health_protection_5")
async def health_protection_5(callback: CallbackQuery):
    with open('app/info/health_protection_5.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_5_keyboard())
    

@router.callback_query(F.data == "health_protection_6")
async def health_protection_6(callback: CallbackQuery):
    with open('app/info/health_protection_6.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_6_keyboard())


@router.callback_query(F.data == "health_protection_7")
async def health_protection_7(callback: CallbackQuery):
    with open('app/info/health_protection_7.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_7_keyboard())
    

@router.callback_query(F.data == "health_protection_8")
async def health_protection_8(callback: CallbackQuery):
    with open('app/info/health_protection_8.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.health_protection_8_keyboard())
    

@router.callback_query(F.data == "disabled")
async def disabled(callback: CallbackQuery):
    with open('app/info/disabled.txt', 'r', encoding='utf-8') as file:
        answer = file.read()

    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "stationary_rules_1")
async def stationary_rules_1(callback: CallbackQuery):
    with open('app/info/stationary_rules_1.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.stationary_rules_1_keyboard())
    

@router.callback_query(F.data == "stationary_rules_2")
async def stationary_rules_2(callback: CallbackQuery):
    with open('app/info/stationary_rules_2.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.stationary_rules_2_keyboard())
    

@router.callback_query(F.data == "stationary_rules_3")
async def stationary_rules_3(callback: CallbackQuery):
    with open('app/info/stationary_rules_3.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.stationary_rules_3_keyboard())
    

@router.callback_query(F.data == "stationary_rules_4")
async def stationary_rules_4(callback: CallbackQuery):
    with open('app/info/stationary_rules_4.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.stationary_rules_4_keyboard())
    

@router.callback_query(F.data == "stationary_rules_5")
async def stationary_rules_5(callback: CallbackQuery):
    with open('app/info/stationary_rules_5.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.stationary_rules_5_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_1")
async def extraordinary_order_1(callback: CallbackQuery):
    with open('app/info/extraordinary_order_1.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_1_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_2")
async def extraordinary_order_2(callback: CallbackQuery):
    with open('app/info/extraordinary_order_2.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_2_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_3")
async def extraordinary_order_3(callback: CallbackQuery):
    with open('app/info/extraordinary_order_3.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_3_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_4")
async def extraordinary_order_4(callback: CallbackQuery):
    with open('app/info/extraordinary_order_4.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_4_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_5")
async def extraordinary_order_5(callback: CallbackQuery):
    with open('app/info/extraordinary_order_5.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_5_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_6")
async def extraordinary_order_6(callback: CallbackQuery):
    with open('app/info/extraordinary_order_6.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_6_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_7")
async def extraordinary_order_7(callback: CallbackQuery):
    with open('app/info/extraordinary_order_7.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_7_keyboard())
    

@router.callback_query(F.data == "extraordinary_order_8")
async def extraordinary_order_8(callback: CallbackQuery):
    with open('app/info/extraordinary_order_8.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.extraordinary_order_8_keyboard())
    

@router.callback_query(F.data == "maternity_hospital")
async def maternity_hospital(callback: CallbackQuery):
    with open('app/info/maternity_hospital.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "dermatovenerologist_analysis")
async def dermatovenerologist_analysis(callback: CallbackQuery):
    with open('app/info/dermatovenerologist_analysis.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.faq_back_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_1")
async def diagnostic_procedures_1(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_1.txt', 'r', encoding='utf-8') as file:
        answer = file.read()

    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_1_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_2")
async def diagnostic_procedures_2(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_2.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_2_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_3")
async def diagnostic_procedures_3(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_3.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_3_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_4")
async def diagnostic_procedures_4(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_4.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_4_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_5")
async def diagnostic_procedures_5(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_5.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_5_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_6")
async def diagnostic_procedures_6(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_6.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_6_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_7")
async def diagnostic_procedures_7(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_7.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_7_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_8")
async def diagnostic_procedures_8(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_8.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_8_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_9")
async def diagnostic_procedures_9(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_9.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_9_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_10")
async def diagnostic_procedures_10(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_10.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_10_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_11")
async def diagnostic_procedures_11(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_11.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_11_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_12")
async def diagnostic_procedures_12(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_12.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_12_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_13")
async def diagnostic_procedures_13(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_13.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_13_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_14")
async def diagnostic_procedures_14(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_14.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_14_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_15")
async def diagnostic_procedures_15(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_15.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_15_keyboard())
    

@router.callback_query(F.data == "diagnostic_procedures_16")
async def diagnostic_procedures_16(callback: CallbackQuery):
    with open('app/info/diagnostic_procedures_16.txt', 'r', encoding='utf-8') as file:
        answer = file.read()
    
    await callback.message.edit_text(answer, parse_mode='HTML',
                                     reply_markup=kb.diagnostic_procedures_16_keyboard())