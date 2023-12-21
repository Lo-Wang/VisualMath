from manim import *

class ne(MovingCameraScene):
    def construct(self):
        intro_text = Text("Выражения").scale(1.4)
        info_text = Text("арифметическое выражение - набор чисел, действий,\n порядка действий, который имеют смысл", font_size=35)
        
        equal = Tex(r"\begin{justify}" 
                    r"Например, $(()()))0--+2/6 + 1)^0 + ?$ - не является " 
                    r"выражением так как лишено смысла." 
                    r"\end{justify}", font_size = 36)
        
        equal_1 = Tex(r"\begin{justify}" 
                    r"А выражение, $(2 + 7)* 2$ - является, потому что, например," 
                    r" задает колличество двух яблок и семи помидоров на двух полках." 
                    r"\end{justify}", font_size = 36)

        # Заголовок
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.play(FadeOut(intro_text))

        # Определение
        self.wait(0.5)
        self.play(Write(info_text))
        self.wait(4)
        self.play(Unwrite(info_text))

        # Негативный пример
        self.wait(0.5)
        self.play(Write(equal))
        self.wait(3)
        self.play(FadeOut(equal, shift=DOWN))
        

        # Позитивный пример
        self.wait(0.5)
        self.play(Write(equal_1))
        self.wait(4)
        self.play(FadeOut(equal_1, shift=DOWN))
        