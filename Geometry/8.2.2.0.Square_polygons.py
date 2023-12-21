from manim import *

class sp(MovingCameraScene):
    def construct(self):
        intro_text = Text("Площадь параллелограма").scale(1.2)

        info_text = Tex(r"Докажем что - $S_A$$_B$$_C$$_D$ = $BH * AD$")
        info_text_1 = Tex(r"1) $\triangle$$ABH$ = $\triangle$$DCE$ \\ Так как имеют равные гипотинузы и катеты").move_to(np.array([0,-3,0]))
        info_text_2 = Tex(r"2) $ABCD$ = $HBCE$ - равновеликие \\ значит состоят из одинаковых фигур").move_to(np.array([0,-3,0]))
        info_text_3 = Tex(r"3) Значит одинаковая и площадь, тогда \\ $S_A$$_B$$_C$$_D$ = $S_H$$_B$$_C$$_E$ = $BH * AB$ = $CA * AB$").move_to(np.array([0,-3,0]))

        # Задаем точки для параллелограма
        dot_A = Dot(3.5 * LEFT + 1.5 * DOWN)
        dot_B = Dot(1.5 * LEFT + 1.5 * UP)
        dot_C = Dot(2.5 * RIGHT + 1.5 * UP)
        dot_D = Dot(0.5 * RIGHT + 1.5 * DOWN)
        dot_Main = VGroup(dot_A, dot_B, dot_C, dot_D)

        # Сдвинуть вправо на 2
        dot_H = Dot(3.5 * LEFT + 1.5 * DOWN)
        # Сдвинуть вправо на 2
        dot_E = Dot(0.5 * RIGHT + 1.5 * DOWN)

        # Задаем названия для точкек параллелограма
        label_A = always_redraw(lambda: MathTex("A").next_to(dot_A, LEFT))
        label_B = always_redraw(lambda: MathTex("B").next_to(dot_B, UP))
        label_C = always_redraw(lambda: MathTex("C").next_to(dot_C, RIGHT))
        label_D = always_redraw(lambda: MathTex("D").next_to(dot_D, DOWN))
        label_Main = VGroup(label_A, label_B, label_C, label_D)
        
        # Задаем названия точек для доп построений
        label_H = always_redraw(lambda: MathTex("H").next_to(dot_H, DOWN))
        label_E = always_redraw(lambda: MathTex("E").next_to(dot_E, DOWN))

        label_DLC = VGroup(label_H, label_E)


        # Задаем стороны для параллелограма
        line_AB = always_redraw(lambda: Line(dot_A, dot_B, color=WHITE))
        line_BC = always_redraw(lambda: Line(dot_B, dot_C, color=WHITE))
        line_CD = always_redraw(lambda: Line(dot_C, dot_D, color=WHITE))
        line_DA = always_redraw(lambda: Line(dot_D, dot_A, color=WHITE))
        line_Main = VGroup(line_AB, line_BC, line_CD, line_DA)

        # Линии начинаются в точке 1 и следуют за точкой 2

        line_BH = always_redraw(lambda: Line(dot_B, dot_H, color=BLUE))
        line_CE = always_redraw(lambda: Line(dot_C, dot_E, color=BLUE))

        line_DE = always_redraw(lambda: Line(dot_D, dot_E, color=ORANGE))
        line_AH = always_redraw(lambda: Line(dot_A, dot_H, color=ORANGE))        

        
        line_DLC = VGroup(line_CE, line_BH, line_DE, line_AH)
        
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
        self.play(Write(dot_H), Write(dot_E), Write(label_DLC), Write(line_DLC), run_time=2)
        self.wait(0.1)
        self.play(ApplyMethod(dot_E.shift, 2 * RIGHT), ApplyMethod(dot_H.shift, 2 * RIGHT))
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
        self.play(FadeOut(dot_Main, shift=DOWN), FadeOut(label_Main, shift=DOWN), FadeOut(line_Main, shift=DOWN), FadeOut(line_DLC, shift=DOWN), FadeOut(info_text_3, shift=DOWN), FadeOut(dot_H, shift=DOWN), FadeOut(dot_E, shift=DOWN), lag_ratio=0.02)
        self.wait(1)


        