from manim import *
# На правку
# Необходимо добавить  текстовое описание с объяснениями для школьников
class gaf(MovingCameraScene):
    def construct(self):  
        
        text1 = Tex(r"\LARGE$y = 4x$")
        text2 = Tex(r"\LARGE$y = 4x+3$", color=RED)
        text3 = Tex(r"\LARGE$y = 4x-2$",color=BLUE)
        v_group = VGroup(text1, text2, text3)
        v_group.arrange(DOWN, buff=0.5)
        v_group.set_height(3)
        
        self.play(FadeIn(v_group))
        self.wait(1.5)
        self.play(FadeOut(v_group))

        number_plane_scaled = Axes(
            x_range=[-10, 10, 1], 
            y_range=[-10, 10, 1]  
        )
        self.play(Create(number_plane_scaled), run_time=5)
        self.wait(1)

        dot_1 = Dot(number_plane_scaled.coords_to_point(-2, -8))
        dot_2 = Dot(number_plane_scaled.coords_to_point(-1, -4))
        dot_3 = Dot(number_plane_scaled.coords_to_point(0, 0))
        dot_4 = Dot(number_plane_scaled.coords_to_point(1, 4))
        dot_5 = Dot(number_plane_scaled.coords_to_point(2, 8))
        group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5)
        line = Line(dot_1, dot_5)
        self.play(Create(group), Create(line), run_time=2)
        self.wait(1)
        
        legend = MathTex("y=4x")
        legend.next_to(line, direction=UP + RIGHT)
        self.play(Write(legend))
        self.wait(1)

        dot_11 = Dot(number_plane_scaled.coords_to_point(-2, -5), color=RED)
        dot_12 = Dot(number_plane_scaled.coords_to_point(-1, -1), color=RED)
        dot_13 = Dot(number_plane_scaled.coords_to_point(0, 3), color=RED)
        dot_14 = Dot(number_plane_scaled.coords_to_point(1, 7), color=RED)
        dot_15 = Dot(number_plane_scaled.coords_to_point(2, 11), color=RED)
        group1 = VGroup(dot_11, dot_12, dot_13, dot_14, dot_15)
        line1 = Line(dot_11, dot_15, color=RED)
        self.play(Create(group1), Create(line1), run_time=2)
        self.wait(1)
        
        legend1 = MathTex("y=4x+3", color = RED)
        legend1.next_to(line1, direction=UP + RIGHT)
        self.play(Write(legend1))
        self.wait(1)

        dot_21 = Dot(number_plane_scaled.coords_to_point(-2, -10), color=BLUE)
        dot_22 = Dot(number_plane_scaled.coords_to_point(-1, -6), color=BLUE)
        dot_23 = Dot(number_plane_scaled.coords_to_point(0, -2), color=BLUE)
        dot_24 = Dot(number_plane_scaled.coords_to_point(1, 2), color=BLUE)
        dot_25 = Dot(number_plane_scaled.coords_to_point(2, 6), color=BLUE)
        group2 = VGroup(dot_21, dot_22, dot_23, dot_24, dot_25)
        line2 = Line(dot_21, dot_25, color=BLUE)
        self.play(Create(group2), Create(line2), run_time=2)
        self.wait(1)
        
        legend2 = MathTex("y=4x-2", color=BLUE)
        legend2.next_to(line2, direction=UP + RIGHT)
        self.play(Write(legend2))
        self.wait(1)