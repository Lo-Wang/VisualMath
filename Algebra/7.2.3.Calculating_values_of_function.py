from manim import *
# На правку
# Необходимо добавить  текстовое описание с объяснениями для школьников
class gaf(MovingCameraScene):
    def construct(self):  

        info_text_1 = Tex(r"\LARGE$y(x) = 2x+1$")
        self.play(FadeIn(info_text_1))
        self.wait(1.5)
        self.play(FadeOut(info_text_1))

        table_1 = Table([["X","-2","-1","0","1","2"], ["Y","-3","-1","1","3","5"]])
        self.play(Write(table_1), run_time=2)
        self.wait(2)
        self.play(Unwrite(table_1), run_time=2)
        self.wait(1)

        number_plane_scaled = NumberPlane(x_range=(-3, 3, 0.5), y_range=(-3,3,0.5), x_length=6,y_length=6)
        self.play(Create(number_plane_scaled), run_time=5)
        self.wait(1)

        dot_1 = Dot(0.1, color=WHITE, z_index=1).move_to(np.array([-1, -1.5, 0]))
        dot_2 = Dot(0.1, color=WHITE, z_index=1).move_to(np.array([-0.5, -0.5, 0]))
        dot_3 = Dot(0.1, color=WHITE, z_index=1).move_to(np.array([0, 0.5, 0]))
        dot_4 = Dot(0.1, color=WHITE, z_index=1).move_to(np.array([0.5, 1.5, 0]))
        dot_5 = Dot(0.1, color=WHITE, z_index=1).move_to(np.array([1, 2.5, 0]))
        line = Line(dot_1, dot_5)

        legend = MathTex("y=2x")
        legend.next_to(line, direction=UP + RIGHT)

        self.play(Create(dot_1),Create(dot_2),Create(dot_3),Create(dot_4), Create(dot_5), Create(line), Write(legend), run_time=2)
        self.wait(1)