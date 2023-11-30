from manim import *

class gaf(MovingCameraScene):
    def construct(self):
        intro_text = Text("Функции").scale(1.4)
        info_text = Tex(r"Функция - строго определенный набор значений $X$ по отношению к значениям $Y$", font_size=38)
        info_text_1 = Tex(r"Рассмотрим на примере - $y = f(x)$ или $y(x) = x$")
        info_text_2 = Tex(r"Всякое значение $X$ равняется $Y$. Составим таблицу значений и построим график", font_size=38)
        
        table_1 = Table([["X","1","2","3","4","5"], ["Y","1","2","3","4","5"]])
        table_2 = Table([["X","1","2","3","4","5"], ["Y","1","2","3","4","5"]]).move_to(3.5 * LEFT).scale(0.6)

        number_plane_scaled = NumberPlane(x_range=(0, 6, 1), y_range=(0,6,1), x_length=6, y_length=6).move_to(np.array([3,1,0]))
        dot_1 = Dot(0.12, color=WHITE, z_index=1).move_to(np.array([1, -1, 0]))
        dot_2 = Dot(0.12, color=WHITE, z_index=1).move_to(np.array([2, 0, 0]))
        dot_3 = Dot(0.12, color=WHITE, z_index=1).move_to(np.array([3, 1, 0]))
        dot_4 = Dot(0.12, color=WHITE, z_index=1).move_to(np.array([4, 2, 0]))
        dot_5 = Dot(0.12, color=WHITE, z_index=1).move_to(np.array([5, 3, 0]))
        line_1 = Line(- 2 * UP, 7 * RIGHT + 5 * UP, color=ORANGE)

        # Заголовок
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.play(FadeOut(intro_text))

        # Определение
        self.wait(0.5)
        self.play(Write(info_text))
        self.wait(4)
        self.play(Unwrite(info_text))

        self.wait(0.5)
        self.play(Write(info_text_1),run_time=3)
        self.wait(3)
        self.play(Unwrite(info_text_1))

        self.wait(0.5)
        self.play(Write(info_text_2),run_time=3)
        self.wait(3)
        self.play(Unwrite(info_text_2))

        # Рисуем таблицу значений
        self.play(Write(table_1))
        self.wait(3)
        self.play(TransformMatchingShapes(table_1, table_2))
        self.play(Create(number_plane_scaled))
        self.wait(3)

        # Рисуем точки
        self.play(Create(dot_1),Create(dot_2),Create(dot_3),Create(dot_4), Create(dot_5))
        self.play(Create(line_1))
        self.wait(3)