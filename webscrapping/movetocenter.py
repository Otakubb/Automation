import pyautogui

size = pag.size()

size = str(size)

size = size.replace(',', ' ')
size = size.replace('=', ' ')
size = size.replace(')', ' ')

size = size.split(' ')

szx = size[1]
szy = size[4]

szx = int(szx)
szy = int(szy)

midx = szx/2
midy = szy/2

midx = str(midx)
midy = str(midy)

midx = midx.replace('.0', '')
midy = midy.replace('.0', '')

midx = int(midx)
midy = int(midy)

pag.moveTo(midx, midy)
