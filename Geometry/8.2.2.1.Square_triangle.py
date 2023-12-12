from manim import *

class st(MovingCameraScene):
    def construct(self):
        intro_text = Text("Площадь треугольника").scale(1.2)

        info_text = Tex(r"Докажем что - $S$$_\triangle$$_A$$_B$$_D$ = $\frac{BH * AD}{2}$") 
        info_text_1 = Tex(r"Так как диагональ в парралелограмме \\ делит его на два равных треугольника").move_to(np.array([0,-3,0]))
        info_text_2 = Tex(r"То делится и площадь на две равные части").move_to(np.array([0,-3,0]))
        info_text_3 = Tex(r"Таким образом, площадь треугольника - половина площади парралелограмма \\ $S_A$$_B$$_D$ = $\frac{BH * AD}{2}$").move_to(np.array([0,-3,0]))

        # Задаем точки для параллелограма
        dot_A = Dot(3.5 * LEFT + 1.5 * DOWN)
        dot_B = Dot(1.5 * LEFT + 1.5 * UP)
        dot_C = Dot(2.5 * RIGHT + 1.5 * UP)
        dot_D = Dot(0.5 * RIGHT + 1.5 * DOWN)
        dot_Main = VGroup(dot_A, dot_B, dot_C, dot_D)

        # Сдвинуть вправо на 2
        dot_H = Dot(3.5 * LEFT + 1.5 * DOWN)

        # Задаем названия для точкек параллелограма
        label_A = always_redraw(lambda: MathTex("A").next_to(dot_A, LEFT))
        label_B = always_redraw(lambda: MathTex("B").next_to(dot_B, UP))
        label_C = always_redraw(lambda: MathTex("C").next_to(dot_C, RIGHT))
        label_D = always_redraw(lambda: MathTex("D").next_to(dot_D, DOWN))
        label_Main = VGroup(label_A, label_B, label_C, label_D)
        
        # Задаем названия точек для доп построений
        label_H = always_redraw(lambda: MathTex("H").next_to(dot_H, DOWN))

        label_DLC = VGroup(label_H)

        # Задаем стороны для параллелограма
        line_AB = always_redraw(lambda: Line(dot_A, dot_B, color=WHITE))
        line_BC = always_redraw(lambda: Line(dot_B, dot_C, color=WHITE))
        line_CD = always_redraw(lambda: Line(dot_C, dot_D, color=WHITE))
        line_DA = always_redraw(lambda: Line(dot_D, dot_A, color=WHITE))
        line_Main = VGroup(line_AB, line_BC, line_CD, line_DA)

        # Линии начинаются в точке 1 и следуют за точкой 2

        line_BH = always_redraw(lambda: Line(dot_B, dot_H, color=ORANGE))
        line_BD = always_redraw(lambda: Line(dot_B, dot_D, color=BLUE))  
        line_DLC = VGroup(line_BH,line_BD)   
        
        # Анимации
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        self.wait(0.5)
        self.play(Write(info_text))
        self.wait(4)
        self.play(Unwrite(info_text))

        self.play(Write(dot_Main), Write(label_Main), Write(line_Main), run_time=3, lag_ratio=0.1)
        self.play(Write(dot_H),  Write(label_DLC), Write(line_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_H.shift, 2 * RIGHT))
        self.play(FadeIn(info_text_1, shift=UP))
        self.wait(6)
        self.play(TransformMatchingTex(info_text_1, info_text_2))
        self.wait(5)
        self.play(TransformMatchingTex(info_text_2, info_text_3))
        self.play(ApplyMethod(dot_A.shift, 2 * RIGHT), ApplyMethod(dot_D.shift, 2 * RIGHT), Unwrite(label_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_A.shift, 2 * LEFT), ApplyMethod(dot_D.shift, 2 * LEFT), Write(label_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_A.shift, 2 * RIGHT), ApplyMethod(dot_D.shift, 2 * RIGHT), Unwrite(label_DLC), run_time=2)
        self.wait(2)
        self.play(FadeOut(dot_Main, shift=DOWN), FadeOut(label_Main, shift=DOWN), FadeOut(line_Main, shift=DOWN), FadeOut(line_DLC, shift=DOWN),  FadeOut(info_text_3, shift=DOWN), FadeOut(dot_H, shift=DOWN), lag_ratio=0.02)
        self.wait(1)


        