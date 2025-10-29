class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        new_text = ''
        for alpha in original_text.lower():
            if alpha in self.alphabet:
                new_index = (self.alphabet.index(alpha) +
                             shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
            else:
                new_text += alpha
        return new_text.capitalize()

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        new_text = ''
        for alpha in cipher_text.lower():
            if alpha in self.alphabet:
                new_index = (self.alphabet.index(alpha) -
                             shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
            else:
                new_text += alpha
        return new_text.capitalize()


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=3
))

cipher_master = CipherMaster()
print(cipher_master.decipher(
    cipher_text='сжргйжю узеябзу тулрво тусзнх ф тзуесёс угкг, ф хзш тсу в зёс дсбфя',
    shift=3
))
