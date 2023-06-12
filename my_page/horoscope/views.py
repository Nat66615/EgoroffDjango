from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

element = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "pisces", "scorpio"]}


def index(request):
    zodiacs = list(zodiac_dict)  # создаем список из ключей словаря
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=[sign])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)


#закоментированна полностью ниже редактированная на теме про шаблон
#def get_zodiac_sign(request, zodiac_sign: str):
#    description = zodiac_dict.get(zodiac_sign, None)
    # обращаемся к словарю с помощью метода get, куда передаем ключ. Или ключ будет найден, или вернется None
    # ключ будет приходит с роута и если ключ найдется,то вернется описание этого ключа
    # это описание будет помещено в переменную description
#    if description:  # если эта переменная не пустая
#        return HttpResponse(description)  # то содержание этой переменной вернется
#    else:
#        return HttpResponseNotFound(f'Знака с названием {zodiac_sign} не существует')

def get_zodiac_sign(request, zodiac_sign: str):
    return render(request, 'horoscope/info_zodiac.html')



def get_zodiac_sign_by_number(request, zodiac_sign: int):
    zodiacs = list(zodiac_dict)  # создаем список из ключей словаря
    if zodiac_sign > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака - {zodiac_sign}')
    name_zodiac = zodiacs[zodiac_sign - 1]  # получаем имя зодиака путем обращения к списку по индексу
    redirect_url = reverse('horoscope_name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)  # URL из основного приложения


def type(request):
    type_list = list(element)  # создаем список из ключей словаря стихий
    li_elements = ''
    for elem in type_list:  # получаем каждую стихию
        #signs_in_type = element(elem)

        li_elements += f"<li><a>{elem.title()}</a></li>"  # строим список из названий стихий, каждый элемент должен быть ссылкой на значение словаря(в котором три знака)
    response = f"""    
        <ol>
            {li_elements}
        </ol>
    """  # оборачиваем готовый список в теги,для вывода списка Html
    return HttpResponse(response)


def get_sign_for_element(request, one_element):
    check = element.get(one_element, None)
    if check:
        # если эта переменная не пустая, в ней список из знаков, подвластных этой стихии, нужно вывести список, оформленный тегами
        element_type = ''
        for sign in check:
            redirect_path = reverse('horoscope_name', args=[sign])
            element_type += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
        response = f"""
            <ul>
                {element_type}
            </ul>
            """
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'Стихии с названием {one_element} не существует')

