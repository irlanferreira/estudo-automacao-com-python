import pyautogui

#Movendo Mouse
pyautogui.moveTo(500, 500)
#Movendo Mouse relativo a posição atual
pyautogui.moveRel(20, 20)
#Obtendo posição do mouse
pyautogui.position()
#Clicar (Pode-se passar como argumento a posição e o botão do mouse)
pyautogui.click()
#Clicar mantendo pressionado e soltar
pyautogui.mouseDown()
pyautogui.mouseUp()
#Clique duplo
pyautogui.doubleClick()
#Arrastar mouse
pyautogui.dragTo(100,100)
pyautogui.dragRel(20,20)