import time
import webbrowser, pyautogui
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
'robocop': 4, 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
'comments': 'n/a'},
{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
]
sources = {'wand': 776,'amulet': 826,'crystal ball': 876,'money': 926}
notas = {1:854,2:921,3:991,4:1061,5:1131}

webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
time.sleep(3)
for d in formData:
    nome = d['name']
    fear = d['fear']
    source = d['source']
    robocop = d['robocop']
    comment = d['comments']

    pyautogui.click(662, 568)
    pyautogui.write(nome)
    pyautogui.click(661, 744)
    pyautogui.typewrite(fear)
    pyautogui.click(721, 931)
    time.sleep(0.25)
    pyautogui.click(665, sources[source])
    pyautogui.scroll(-5000)
    pyautogui.click(notas[robocop], 528)
    time.sleep(1)
    pyautogui.scroll(-400)
    time.sleep(0.20)
    pyautogui.click(679, 716)
    pyautogui.typewrite(comment)
    time.sleep(0.20)
    pyautogui.scroll(-400)
    time.sleep(0.20)
    pyautogui.click(662, 793)
    time.sleep(2)
    pyautogui.click(699, 338)
    time.sleep(2)
