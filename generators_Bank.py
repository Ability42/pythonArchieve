>>> class Bank(): # создаём банк, строящий торговые автоматы (ATM — Automatic Teller Machine)
...    crisis = False
...    def create_atm(self) :
...        while not self.crisis :
...            yield "$100"
>>> hsbc = Bank() # когда всё хорошо, можно получить сколько угодно денег с торгового автомата
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # пришёл кризис, денег больше нет!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # что верно даже для новых автоматов
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # проблема в том, что когда кризис прошёл, автоматы по-прежнему пустые...
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # но если построить ещё один, будешь снова в деле!
>>> for cash in brand_new_atm :
...    print cash
$100
$100
$100
$100
$100
$100
$100
$100
$100
...