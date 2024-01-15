import sys
import time

import pygame
pygame.init()

W, H = 1500, 600
FPS = 30
clock_ = pygame.time.Clock()

pygame.display.set_caption('Кроссворд по теме "Информационная безопасность"')


scr = pygame.display.set_mode((W, H))
s = pygame.Surface((W - 785, 540))
s.set_alpha(90)
s.fill((255, 255, 255))
font_schet = pygame.font.Font('Fonts/Intro.ttf', 22)
font_schet1 = pygame.font.Font('Fonts/Intro.ttf', 20)
font_text_cross = pygame.font.Font('Fonts/BoredersDivide.ttf', 20)
image_fon = pygame.image.load('images/FON_FOR_CROSSWORD.png').convert_alpha()

text_for_crossword = [['1. ... объектов информатизации - комплекс организационных и технических мероприятий,',
                       '     в результате которых подтверждается соответствие системы защиты информации',
                       '     объекта информатизации требованиям, безопасности информации',],
                      ['2. ... информации - лицо, самостоятельно создавшее информацию либо получившее',
                       '    на основании закона или договора право разрешать или ограничивать доступ',
                       '    к информации, определяемой по каким-либо признакам'],
                      ['3. Режим ... - совокупность требований, правил, организационных, технических и иных мер,',
                       '    технических и иных мер, направленных на сохранность сведений, составляющих',
                       '    государственную тайну'],
                      ['4. ... имя - обозначение символами, предназначенное для адресации сайтов в сети ',
                       '    "Интернет" в целях обеспечения доступа к информации, размещенной в сети "Интернет"'],
                      ['5. ... информации - состояние защищенности информации, при котором обеспечены ее ',
                       '    конфиденциальность, доступность и целостность'],
                      ['6. ... защищаемой информации - физическое лицо или материальный объект, в том числе',
                       '    физическое поле, в которых информация находит свое отображение в виде символов,',
                       '    образов, сигналов, технических решений, процессов и количественных характеристик ',
                       '    физических величин'],
                      ['7. ... защиты информации автоматизированной системы - совокупность всех технических,',
                       ' программных и программно-технических средств защиты информации и средств контроля',
                       ' эффективности защиты информации'],
                      ['8. Секретная ... - ...,  содержащие сведения, отнесенные к государственной тайне']]


class Word:
    def __init__(self, count_letters, word, x, y):
        self.count = count_letters
        self.word = word
        self.curr_word = ''
        self.cell_size = 25
        self.x = x
        self.y = y
        self.fl = False
        self.is_current = False
        self.color_num = 'black'
        self.spisok_letters = []
        for i in range(1, len(self.word) + 1):
            s = Letter(self.x + self.cell_size * i, self.y)
            self.spisok_letters.append(s)
            spisok_all_letters.append(s)

    def draw_rects(self):
        if self.is_current:
            self.color_num = 'red'
        else:
            self.color_num = 'black'
        for i in range(1, len(self.word) + 1):
            for j in range(len(self.spisok_letters)):
                if j == len(self.curr_word) and self.is_current:
                    self.spisok_letters[j].draw('red', 2)
                else:
                    self.spisok_letters[j].draw('black', 1)
                txt_chsl = font_schet1.render(str(self.count), True, self.color_num)
                scr.blit(txt_chsl, (self.x + 10, self.y))

    def add_letter(self, key):
        if len(self.curr_word + key) <= len(self.word):
            if not self.spisok_letters[len(self.curr_word)].is_checkd:
                self.spisok_letters[len(self.curr_word)].letter = key
                self.curr_word += key
            else:
                self.curr_word += self.spisok_letters[len(self.curr_word)].letter
                self.spisok_letters[len(self.curr_word)].letter = key
                self.curr_word += key

    def del_letter(self):
        if not self.spisok_letters[len(self.curr_word) - 1].is_checkd:
            self.spisok_letters[len(self.curr_word) - 1].letter = ''
            self.curr_word = self.curr_word[:-1]
        else:
            self.spisok_letters[len(self.curr_word) - 2].letter = ''
            self.curr_word = self.curr_word[:-2]

    def proverka(self):
        if self.curr_word == self.word:
            for i in self.spisok_letters:
                i.is_checkd = True

    def proverka_full(self):
        for i in self.spisok_letters:
            if not i.is_checkd:
                return False
        return True


class Word_vert:
    def __init__(self, count_letters, word, x, y):
        self.count = count_letters
        self.word = word
        self.curr_word = ''
        self.cell_size = 25
        self.x = x
        self.y = y
        self.is_current = False
        self.color_num = 'black'
        self.spisok_letters = []

        for j in range(len(self.word)):
            s = Letter(self.x, self.y + self.cell_size * j)
            f = True
            for i in spisok_all_letters:
                if i.x == s.x and i.y == s.y:
                    self.spisok_letters.append(i)
                    f = False
            if f:
                self.spisok_letters.append(s)
                spisok_all_letters.append(s)

    def draw_rects(self):
        if self.is_current:
            self.color_num = 'red'
        else:
            self.color_num = 'black'
        for i in range(1, len(self.word) + 1):
            for j in range(len(self.spisok_letters)):
                if j == len(self.curr_word) and self.is_current:
                    self.spisok_letters[j].draw('red', 2)
                else:
                    self.spisok_letters[j].draw('black', 1)
                txt_chsl = font_schet1.render(str(self.count), True, self.color_num)
                scr.blit(txt_chsl, (self.x, self.y - 20))

    def add_letter(self, key):
        if len(self.curr_word + key) <= len(self.word):
            if not self.spisok_letters[len(self.curr_word)].is_checkd:
                self.spisok_letters[len(self.curr_word)].letter = key
                self.curr_word += key
            else:
                self.curr_word += self.spisok_letters[len(self.curr_word)].letter
                self.spisok_letters[len(self.curr_word)].letter = key
                self.curr_word += key

    def del_letter(self):
        if not self.spisok_letters[len(self.curr_word) - 1].is_checkd:
            self.spisok_letters[len(self.curr_word) - 1].letter = ''
            self.curr_word = self.curr_word[:-1]
        else:
            self.spisok_letters[len(self.curr_word) - 2].letter = ''
            self.curr_word = self.curr_word[:-2]

    def proverka(self):
        if self.curr_word == self.word:
            for i in self.spisok_letters:
                i.is_checkd = True

    def proverka_full(self):
        for i in self.spisok_letters:
            if not i.is_checkd:
                return False
        return True


class Letter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_checkd = False
        self.cell_size = 25
        self.letter = ''
        self.color = 'black'

    def draw(self, color_blocks, w):
        pygame.draw.rect(scr, color_blocks, (self.x, self.y, self.cell_size, self.cell_size), w)
        if self.letter:
            self.color = 'green' if self.is_checkd else 'black'
            txt_surf = font_schet.render(self.letter, True, self.color)
            # pygame.draw.rect(scr, 'lightblue', (self.x + 2, self.y + 2, 21, 21))
            x, y = self.x + (12.5 - txt_surf.get_width() // 2), \
                   self.y + (12.5 - txt_surf.get_height() // 2)
            scr.blit(txt_surf, (x, y))


spisok_slov = []
spisok_all_letters = []
spis_goriz = [(1, 'аттестация'), (5, "безопасность"), (3, "секретности"), (8, "информация")]
spis_coor_goriz = [(475, 250), (125, 125), (300, 175), (0, 175)]
spis_vertical = [(7, 'система'), (6, "носитель"), (4, "доменное"), (2, "обладатель")]
spis_coor_vert = [(175, 25), (225, 100), (350, 100), (500, 175)]
for i in range(len(spis_goriz)):
    spisok_slov.append(Word(spis_goriz[i][0], spis_goriz[i][1],
                            spis_coor_goriz[i][0], spis_coor_goriz[i][1]))
for i in range(len(spis_vertical)):
    spisok_slov.append(Word_vert(spis_vertical[i][0], spis_vertical[i][1], spis_coor_vert[i][0],
                                 spis_coor_vert[i][1]))

f = True
curr_word = [i for i in spisok_slov if i.count - 1 == 0][0]
index_curr_word = curr_word.count - 1
first_word = curr_word
ind_del = spisok_slov.index(first_word)
spisok_slov.insert(len(spisok_slov), first_word)
spisok_slov.pop(ind_del)
first_word.is_current = True
while f:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                first_word.proverka()
            elif event.key == pygame.K_BACKSPACE:
                first_word.del_letter()
            elif event.key == pygame.K_RIGHT:
                index_curr_word += 1
                index_curr_word %= len(spisok_slov)
                first_word.is_current = False
                first_word = [i for i in spisok_slov if i.count - 1 == index_curr_word][0]
                ind_del = spisok_slov.index(first_word)
                spisok_slov.insert(len(spisok_slov), first_word)
                spisok_slov.pop(ind_del)
                first_word.is_current = True
            elif event.key == pygame.K_LEFT:
                index_curr_word -= 1
                index_curr_word %= len(spisok_slov)
                first_word.is_current = False
                first_word = [i for i in spisok_slov if i.count - 1 == index_curr_word][0]
                ind_del = spisok_slov.index(first_word)
                spisok_slov.insert(len(spisok_slov), first_word)
                spisok_slov.pop(ind_del)
                first_word.is_current = True
            elif event.unicode in ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п',
                                   'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']:
                first_word.add_letter(event.unicode)
    scr.fill('lightblue')
    scr.blit(image_fon, (0, 0))
    scr.blit(s, (760, 20))
    co = 0
    for i in range(len(text_for_crossword)):
        y = co + 20
        for j in range(len(text_for_crossword[i])):
            co += 20
            text_cross_output = font_text_cross.render(text_for_crossword[i][j], True, 'black')
            scr.blit(text_cross_output, (770, y + j * 20))
            if j + 1 == len(text_for_crossword[i]):
                co += 15
    for i in spisok_slov:
        i.draw_rects()
    if all([i.proverka_full() for i in spisok_slov]):
        text_win = font_text_cross.render('Вы успешно выполнили кроссворд!', True, 'black')
        scr.blit(text_win, (100, 550))
    pygame.display.update()
    clock_.tick(FPS)
