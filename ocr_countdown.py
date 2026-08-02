import easyocr
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('countdownstyle.jpg', detail=0, paragraph=True)
print('\n'.join(result))
