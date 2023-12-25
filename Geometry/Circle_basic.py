from manim import *

class cb(MovingCameraScene):
    def construct(self):
        intro_text = Text("Окружность").scale(1.4)
        info_text = Tex(r"Окружность - это набор точек, находящихся на одинаковом \\ расстоянии от одной конкретной точки", font_size=35).move_to(np.array([0,-2,0]))




        # Задаем окружность 
        circle_main = Circle(radius=2).move_to(np.array([0,1,0]))

        #Точки на окружности
        point_A = circle_main.point_at_angle(0 * DEGREES)
        point_B = circle_main.get_center()

        # Задаем точки для хорды, диаметра, радиуса
        dot_A = Dot().move_to(point_A)
        dot_B = Dot().move_to(point_B)
        dot_C = Dot()
        dot_D = Dot()
        dot_Main = VGroup(dot_A, dot_B, dot_C, dot_D)

        # Привязка линий к точкам
        line_AB = always_redraw(lambda: Line(dot_A, dot_B, color=WHITE))


        # Привязка букв к точкам
        label_A = always_redraw(lambda: MathTex("A").next_to(dot_A, RIGHT))
        label_B = always_redraw(lambda: MathTex("B").next_to(dot_B, UP))
        label_main = VGroup(label_A, label_B)

        

        # Анимации
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        self.wait(0.5)
        self.play(Write(line_AB), Write(label_main), FadeIn(dot_A, shift=UP), FadeIn(dot_B, shift=DOWN), Write(circle_main,run_time=3), lag_ratio=1)
        self.play(MoveAlongPath(dot_A, circle_main, run_time = 3))
        self.play(Write(info_text))
        self.wait(4)
        self.play(Unwrite(info_text))