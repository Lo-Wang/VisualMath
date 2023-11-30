from manim import *

class ne(MovingCameraScene):
    def construct(self):
        intro_text = Text("Выражения").scale(1.4)
        info_text = Text("алгебраическое выражение - набор чисел, символов, действий,\n порядка действий, который имеют смысл", font_size=32)
        underline = Underline(mobject=info_text[35:43], buff=0.1, stroke_width=2, color = ORANGE)
        
        equal = Tex(r"\begin{justify}" 
                    r"Например, $yyy)))*(++x$ - не является " 
                    r"выражением так как лишено смысла." 
                    r"\end{justify}", font_size = 36)
        
        equal_1 = Tex(r"\begin{justify}" 
                    r"А выражение, $y = 2 * x + 1 $ - является, потому что " 
                    r" задает определенный график функции." 
                    r"\end{justify}", font_size = 36)

        # Определение
        self.wait(0.5)
        self.play(Write(info_text))
        self.play(Create(underline))
        self.wait(4)
        self.play(Unwrite(info_text), Uncreate(underline))

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
        