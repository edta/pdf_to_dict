import fitz

def pdf_to_dict(file_name):
    #для получения информации из pdf используем библиотеку fitz
    doc = fitz.open(file_name)
    page = doc[0]
    page_text = page.get_text("text")
    #сначала получаем массив всех данных с pdf,обрабатываем его
    pdf_arr = list(page_text.split("\n"))
    pdf_arr.remove("")
    pdf_arr.remove(" ")
    #из массива формируем словать
    pdf_dict = dict()
    for i in pdf_arr:
        if ':' in i:
            pdf_dict[i.split(":")[0]] = i.split(":")[1]
        elif ':' not in i:
            pdf_dict[i] = ""

    return pdf_dict

#с помощью средств библиотеку получаем координаты областей файла шаблона и потом сравниваем эти координаты с координатами областей других файлов
def prepare_template(file_name):
    doc = fitz.open(file_name)
    page = doc[0]
    template = dict()
    for keys in pdf_to_dict(file_name):
        areas = page.search_for(keys)
        template[keys] = areas

    return template

#нужно добавить обратобку ошибок и нормальное сравнение сделать, но пока оставил так
def check_two_pdf(file_1, file_2):
    pdf_dict_1 = prepare_template(file_1)
    pdf_dict_2 = prepare_template(file_2)
    return "File structure is correct" if pdf_dict_1 == pdf_dict_2 else "File structure is incorrect"

