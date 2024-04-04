from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' <b>Лев - пятый знак зодиака</b>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', ' virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Ви передали число з 4 цифр - {sign_zodiac}')


# def get_info_zodiac_sign(request, sign_zodiac: str):
#     description = zodiac_dict.get(sign_zodiac, None)
#     if description:  # провірить, чи змінна не пуста
#         return HttpResponse(f'<h2>{description}</h2>')
#     else:
#         return HttpResponseNotFound(f'Невідомий знак зодіака - {sign_zodiac}')

@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'

def get_info_zodiac_sign(request, sign_zodiac: str):
    # response = render_to_string('horoscope/info_zodiac.html')  # ця функція зчитує шаблон html й перетворює в її рядок
    # return HttpResponse(response)
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'my_int': 123,
        'my_float': 123.5,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3, 4, 5),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Will', 55),
        'value': [],
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):  # якщо число яке приходить на вхід більше ніж довжина списку
        return HttpResponseNotFound(f'Не правильний порядковий номер знака зодіака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("1", args=[name_zodiac])
    # return HttpResponseRedirect(f"/horoscope/{name_zodiac}")
    return HttpResponseRedirect(redirect_url)


# def index(request):
#     zodiacs = list(zodiac_dict)
#     res = ''
#     for sign in zodiacs:
#         redirect_path = reverse("1", args=[sign])
#         res += f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
#     response = f"""
#     <ol>
#         {res}
#     <ol>
#     """
#     return HttpResponse(response)

def index(request):
    zodiacs = list(zodiac_dict)
    # redirect_path = reverse('1', [])
    # rdy_redirect = f'<li> <a href="{redirect_path}"> {sign.title()} </a> </li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def zodiac_types(request):
    res = ''
    for element in types_dict:
        # redirect_path = f"/horoscope/type/{element}/"
        redirect_path = reverse("zodiac_list", args=[element])
        res += f'<li><a href="{redirect_path}">{element}</a></li>'
    response = f"""
    <ul>
        {res}
    </ul>
    """
    return HttpResponse(response)


def get_zodiac_list(request, element):
    if element in types_dict:
        zodiac_list = types_dict[element]
        res = ''
        for sign in zodiac_list:
            redirect_path = reverse("zodiac_info_by_element", args=[element, sign])
            res += f'<li><a href="{redirect_path}">{sign}</a></li>'
        response = f"""
        <ul>
            {res}
        </ul>
        """
        return HttpResponse(response)
    else:
        return HttpResponse('Invalid zodiac type')


def get_info_zodiac_sign_by_element(request, element, sign_zodiac):
    if element in types_dict:
        description = zodiac_dict.get(sign_zodiac, None)
        if description:
            return HttpResponse(description)
        else:
            return HttpResponseNotFound(f'Невідомий знак зодіака - {sign_zodiac}')
    else:
        return HttpResponse('Invalid zodiac type')
