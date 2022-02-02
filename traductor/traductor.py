from googletrans import Translator
import googletrans
#print(googletrans.LANGUAGES)

translator = Translator()

palabra = input('Introduzca la palabra o frase que quiera traducir al espanol: ')

traduccion = translator.translate(palabra, dest='es')

print(traduccion.text)

