from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="О Больнице",
                                     callback_data="about")
            ],
            [
                InlineKeyboardButton(text="Режим работы",
                                     callback_data="work_time")
            ],
            [
                InlineKeyboardButton(text="Адрес и схема проезда",
                                     callback_data="driveway")
            ],
            [
                InlineKeyboardButton(text="Контакты",
                                     callback_data="contacts")
            ],
            [
                InlineKeyboardButton(text="Часто задаваемые вопросы",
                                     callback_data="faq")
            ],
        ]
    )


def back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="main")
            ],
        ]
    )


def faq_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Правила госпитализации",
                                     callback_data="hospitalization_rules")
            ],
            [
                InlineKeyboardButton(text="Сроки госпитализации",
                                     callback_data="hospitalization_length")
            ],
            [
                InlineKeyboardButton(text="Правила записи на обследование",
                                     callback_data="register_rules")
            ],
            [
                InlineKeyboardButton(text="Как получить консультацию специалиста",
                                     callback_data="consultation_rules")
            ],
            [
                InlineKeyboardButton(text="Консультация травмотологов-ортопедов",
                                     callback_data="traumatology_consultation")
            ],
            [
                InlineKeyboardButton(text="О видах медицинской помощи",
                                     callback_data="about_med_help")
            ],
            [
                InlineKeyboardButton(text="О недопустимости отказа в мед. помощи",
                                     callback_data="med_help_availability")
            ],
            [
                InlineKeyboardButton(text="Права и обязанности застрахованных лиц",
                                     callback_data="rights_and_duties_1")
            ],
            [
                InlineKeyboardButton(text="Права и обязанности в здравоохранении",
                                     callback_data="health_protection_1")
            ],
            [
                InlineKeyboardButton(text="Порядок признания лица инвалидом",
                                     callback_data="disabled")
            ],
            [
                InlineKeyboardButton(text="Правила внутреннего распорядка стационара",
                                     callback_data="stationary_rules_1")
            ],
            [
                InlineKeyboardButton(text="О медпомощи во внеочередном порядке",
                                     callback_data="extraordinary_order_1")
            ],
            [
                InlineKeyboardButton(text="Что взять с собой в роддом?",
                                     callback_data="maternity_hospital")
            ],
            [
                InlineKeyboardButton(text="Как сдавать анализы дерматовенерологу?",
                                     callback_data="dermatovenerologist_analysis")
            ],
            [
                InlineKeyboardButton(text="Подготовка к диагностическим процедурам",
                                     callback_data="diagnostic_procedures_1")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="main")
            ],
        ]
    )


def rights_and_duties_1_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ▶️",
                                     callback_data="rights_and_duties_2")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def rights_and_duties_2_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 1 ◀️",
                                     callback_data="rights_and_duties_1"),
                InlineKeyboardButton(text="Стр. 3 ▶️",
                                     callback_data="rights_and_duties_3")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def rights_and_duties_3_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ◀️",
                                     callback_data="rights_and_duties_2"),
                InlineKeyboardButton(text="Стр. 4 ▶️",
                                     callback_data="rights_and_duties_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def rights_and_duties_4_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 3 ◀️",
                                     callback_data="rights_and_duties_3"),
                InlineKeyboardButton(text="Стр. 5 ▶️",
                                     callback_data="rights_and_duties_5")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def rights_and_duties_5_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 4 ◀️",
                                     callback_data="rights_and_duties_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_1_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ▶️",
                                     callback_data="health_protection_2")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_2_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 1 ◀️",
                                     callback_data="health_protection_1"),
                InlineKeyboardButton(text="Стр. 3 ▶️",
                                     callback_data="health_protection_3")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_3_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ◀️",
                                     callback_data="health_protection_2"),
                InlineKeyboardButton(text="Стр. 4 ▶️",
                                     callback_data="health_protection_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_4_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 3 ◀️",
                                     callback_data="health_protection_3"),
                InlineKeyboardButton(text="Стр. 5 ▶️",
                                     callback_data="health_protection_5")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_5_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 4 ◀️",
                                     callback_data="health_protection_4"),
                InlineKeyboardButton(text="Стр. 6 ▶️",
                                     callback_data="health_protection_6")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_6_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 5 ◀️",
                                     callback_data="health_protection_5"),
                InlineKeyboardButton(text="Стр. 7 ▶️",
                                     callback_data="health_protection_7")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_7_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 6 ◀️",
                                     callback_data="health_protection_6"),
                InlineKeyboardButton(text="Стр. 8 ▶️",
                                     callback_data="health_protection_8")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def health_protection_8_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 7 ◀️",
                                     callback_data="health_protection_7")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def stationary_rules_1_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ▶️",
                                     callback_data="stationary_rules_2")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def stationary_rules_2_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 1 ◀️",
                                     callback_data="stationary_rules_1"),
                InlineKeyboardButton(text="Стр. 3 ▶️",
                                     callback_data="stationary_rules_3")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def stationary_rules_3_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ◀️",
                                     callback_data="stationary_rules_2"),
                InlineKeyboardButton(text="Стр. 4 ▶️",
                                     callback_data="stationary_rules_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def stationary_rules_4_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 3 ◀️",
                                     callback_data="stationary_rules_3"),
                InlineKeyboardButton(text="Стр. 5 ▶️",
                                     callback_data="stationary_rules_5")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def stationary_rules_5_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 4 ◀️",
                                     callback_data="stationary_rules_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_1_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ▶️",
                                     callback_data="extraordinary_order_2")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_2_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 1 ◀️",
                                     callback_data="extraordinary_order_1"),
                InlineKeyboardButton(text="Стр. 3 ▶️",
                                     callback_data="extraordinary_order_3")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_3_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ◀️",
                                     callback_data="extraordinary_order_2"),
                InlineKeyboardButton(text="Стр. 4 ▶️",
                                     callback_data="extraordinary_order_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_4_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 3 ◀️",
                                     callback_data="extraordinary_order_3"),
                InlineKeyboardButton(text="Стр. 5 ▶️",
                                     callback_data="extraordinary_order_5")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_5_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 4 ◀️",
                                     callback_data="extraordinary_order_4"),
                InlineKeyboardButton(text="Стр. 6 ▶️",
                                     callback_data="extraordinary_order_6")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_6_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 5 ◀️",
                                     callback_data="extraordinary_order_5"),
                InlineKeyboardButton(text="Стр. 7 ▶️",
                                     callback_data="extraordinary_order_7")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_7_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 6 ◀️",
                                     callback_data="extraordinary_order_6"),
                InlineKeyboardButton(text="Стр. 8 ▶️",
                                     callback_data="extraordinary_order_8")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def extraordinary_order_8_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 7 ◀️",
                                     callback_data="extraordinary_order_7")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_1_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ▶️",
                                     callback_data="diagnostic_procedures_2")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_2_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 1 ◀️",
                                     callback_data="diagnostic_procedures_1"),
                InlineKeyboardButton(text="Стр. 3 ▶️",
                                     callback_data="diagnostic_procedures_3")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_3_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 2 ◀️",
                                     callback_data="diagnostic_procedures_2"),
                InlineKeyboardButton(text="Стр. 4 ▶️",
                                     callback_data="diagnostic_procedures_4")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_4_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 3 ◀️",
                                     callback_data="diagnostic_procedures_3"),
                InlineKeyboardButton(text="Стр. 5 ▶️",
                                     callback_data="diagnostic_procedures_5")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_5_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 4 ◀️",
                                     callback_data="diagnostic_procedures_4"),
                InlineKeyboardButton(text="Стр. 6 ▶️",
                                     callback_data="diagnostic_procedures_6")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_6_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 5 ◀️",
                                     callback_data="diagnostic_procedures_5"),
                InlineKeyboardButton(text="Стр. 7 ▶️",
                                     callback_data="diagnostic_procedures_7")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_7_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 6 ◀️",
                                     callback_data="diagnostic_procedures_6"),
                InlineKeyboardButton(text="Стр. 8 ▶️",
                                     callback_data="diagnostic_procedures_8")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_8_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 7 ◀️",
                                     callback_data="diagnostic_procedures_7"),
                InlineKeyboardButton(text="Стр. 9 ▶️",
                                     callback_data="diagnostic_procedures_9")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_9_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 8 ◀️",
                                     callback_data="diagnostic_procedures_8"),
                InlineKeyboardButton(text="Стр. 10 ▶️",
                                     callback_data="diagnostic_procedures_10")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_10_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 9 ◀️",
                                     callback_data="diagnostic_procedures_9"),
                InlineKeyboardButton(text="Стр. 11 ▶️",
                                     callback_data="diagnostic_procedures_11")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_11_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 10 ◀️",
                                     callback_data="diagnostic_procedures_10"),
                InlineKeyboardButton(text="Стр. 12 ▶️",
                                     callback_data="diagnostic_procedures_12")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_12_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 11 ◀️",
                                     callback_data="diagnostic_procedures_11"),
                InlineKeyboardButton(text="Стр. 13 ▶️",
                                     callback_data="diagnostic_procedures_13")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_13_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 12 ◀️",
                                     callback_data="diagnostic_procedures_12"),
                InlineKeyboardButton(text="Стр. 14 ▶️",
                                     callback_data="diagnostic_procedures_14")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_14_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 13 ◀️",
                                     callback_data="diagnostic_procedures_13"),
                InlineKeyboardButton(text="Стр. 15 ▶️",
                                     callback_data="diagnostic_procedures_15")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_15_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 14 ◀️",
                                     callback_data="diagnostic_procedures_14"),
                InlineKeyboardButton(text="Стр. 16 ▶️",
                                     callback_data="diagnostic_procedures_16")
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def diagnostic_procedures_16_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Стр. 15 ◀️",
                                     callback_data="diagnostic_procedures_15"),
            ],
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )


def faq_back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад",
                                     callback_data="faq")
            ],
        ]
    )