import math


def citire_lista():
    lista = []
    string_lista = input('Dati elementele listei, separate printr-un spatiu: ')
    string_elemente = string_lista.split(sep=' ')
    for string_element in string_elemente:
        element = int(string_element)
        lista.append(element)
    return lista


def is_prime(n):
    """
    verifica daca un numar este prim
    :param n: numarul pt care verificam primalitatea
    :return: rezultatul verificarii
    """
    if n < 2:
        return False
    if n == 2:
        return True
    d = 2
    while d <= int(math.sqrt(n)) + 1:
        if n % d == 0:
            return False
        d += 1
    return True


def sum_list_is_prime(lista):
    """
    Verifica daca suma elementelor unei liste este prima
    :param lista: lista ce contine elementele de adunat
    :return: rezultatul verificarii
    """
    s = sum(lista)
    return is_prime(s)


def get_longest_sum_is_prime(lista):
    """
    Gaseste si returneaza cea mai lunga subsecventa a listei pt care suma elementelor ei este un nr prim
    :param lista: lista in care va cauta subsecventa cu proprietatea ceruta
    :return: secventa maxima care indeplineste proprietatea ceruta
    """
    secventa_maxima = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if sum_list_is_prime(lista[start:end]):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala


def test_get_longest_sum_is_prime():
    """
    Testeaza get_longest_sum_is_prime() - cateva teste utile
    """
    assert (get_longest_sum_is_prime([1, 1, 1, 2])) == [1, 1, 1, 2]
    assert (get_longest_sum_is_prime([1, 1, 1, 1, 1, 1, 1, 3])) == [1, 1, 1, 1, 1, 1, 1]
    assert (get_longest_sum_is_prime([11])) == [11]
    assert (get_longest_sum_is_prime([1, 2, 3, 4, 5])) == [1, 2]
    assert (get_longest_sum_is_prime([4, 6, 8, 10])) == []
    assert (get_longest_sum_is_prime([2, 4, 6, 8, 10])) == [2]


def numar_cifre(n):
    """
    Calculeaza numaruld de cifre al unui numar
    :param n: numaru pt care vrem sa aflam nr de cifre
    :return: nr de cifre a lui n
    """
    m = n
    nr = 0
    while m:
        nr += 1
        m //= 10
    return nr


def ordine_descrescatoare(lista):
    """
    Verifica daca elementele unei liste au numarul de cifre in ordine descrescatoare
    :param lista: lista care contine elementele de veificat
    :return: rezultatul verificarii
    """
    for i in range(1, len(lista)):
        if numar_cifre(lista[i - 1]) < numar_cifre(lista[i]):
            return False
    return True


def get_longest_digit_count_desc(lista):
    """
    Gaseste si returneaza cea mai lunga subsecventa a listei pt care num??rul de cifre este ??n ordine descresc??toare
    :param lista: lista in care va cauta subsecventa cu proprietatea ceruta
    :return: secventa maxima care indeplineste proprietatea ceruta
    """
    secventa_maxima = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if ordine_descrescatoare(lista[start:end]):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([765, 43, 2, 1, 56]) == [765, 43, 2, 1]
    assert get_longest_digit_count_desc([8]) == [8]
    assert get_longest_digit_count_desc([1, 2, 56, 898]) == [1, 2]
    assert get_longest_digit_count_desc([3, 12, 356]) == [3]
    assert get_longest_digit_count_desc([1, 34, 1000, 99, 3000, 1234, 456, 34, 7, 9]) == [3000, 1234, 456, 34, 7, 9]


def ordine_crescatoare(n):
    """
    Verifica daca cifrele din n sunt in ordine crescatoare
    -consider ordine crescatoare oricare a,b cu a <= b
    :param n: n
    :return: rezultatul verificarii
    """
    m = n
    while m:
        if m % 10 < (m // 10) % 10:
            return False
        m //= 10
    return True


def concatenare_lista(lista):
    """
    Concateneaza elementele unei liste
    :param lista: lista- o lista de int-uri
    :return: concatenare - lista concatenata ca un int
    """
    str_conc = ''
    for element in lista:
        str_conc = str_conc + str(element)
    concatenare = int(str_conc)
    return concatenare


def get_longest_concat_digits_asc(lista):
    """
    Gaseste si returneaza cea mai lunga subsecventa a listei pt care concatenarea numerelor din subsecven???? are
     cifrele ??n ordine cresc??toare.
    :param lista: lista in care va cauta subsecventa cu proprietatea ceruta
    :return: secventa maxima care indeplineste proprietatea ceruta
    """
    secventa_maxima = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            numar = concatenare_lista(lista[start:end])
            if ordine_crescatoare(numar):
                secventa_maxima.append(lista[start:end])
    secventa_maxima_finala = []
    for lista_elemente in secventa_maxima:
        if len(lista_elemente) > len(secventa_maxima_finala):
            secventa_maxima_finala = lista_elemente
    return secventa_maxima_finala


def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([1, 2, 45, 567]) == [1, 2, 45, 567]
    assert get_longest_concat_digits_asc([7, 23, 67]) == [23, 67]
    assert get_longest_concat_digits_asc([81, 23, 45, 890]) == [23, 45]
    assert get_longest_concat_digits_asc([987, 122, 2, 22, 7]) == [122, 2, 22, 7]
    assert get_longest_concat_digits_asc([1, 23, 45, 5, 1, 7, 35, 555, 5, 7, 9]) == [35, 555, 5, 7, 9]
    assert get_longest_concat_digits_asc([45, 566, 78, 98, 1, 24, 67]) == [45, 566, 78]
    assert get_longest_concat_digits_asc([879]) == []


def main():
    lista = []
    while True:
        print("""
        1.Citire lista
        2.Determinarea celei mai lungi subsecvente pentru care suma numerelor este num??r prim.
        3.Determinarea celei mai lungi subsecvente pentru care num??rul de cifre este ??n ordine descresc??toare 
            (consideram ca respecta proprietate si urmatoarele tipuri de liste:
             -->exemple: [abc, ab, ad, gf, e, r, k, i] sau [a, b, c], o litera reprezinta o cifra)
        4.Determinarea celei mai lungi subsecvente pentru care concatenarea numerelor din subsecven???? are cifrele 
            ??n ordine cresc??toare.
        5.Exit
        """)
        obtiune = input('Alege optiunea: ')
        if obtiune == '1':
            lista = citire_lista()
        elif obtiune == '2':
            print(get_longest_sum_is_prime(lista))
        elif obtiune == '3':
            print(get_longest_digit_count_desc(lista))
        elif obtiune == '4':
            print(get_longest_concat_digits_asc(lista))
        elif obtiune == '5':
            break
        else:
            print('Obtiune invalida')


test_get_longest_digit_count_desc()
test_get_longest_sum_is_prime()
test_get_longest_concat_digits_asc()
main()
