from manim import *

class gaf(MovingCameraScene):
    def construct(self):  

        info_text = Tex(r"\Huge$\frac{x_{1}}{x_{2}} = \frac{y_{1}}{y_{2}}$", font_size=38)
        info_text_1 = Tex(r"\LARGE$y = 2x$")

        self.play(FadeIn(info_text))
        self.wait(1.5)
        self.play(FadeOut(info_text))

        self.play(FadeIn(info_text_1))
        self.wait(1.5)
        self.play(FadeOut(info_text_1))


        table_1 = Table([["X","-2","-1","0","1","2"], ["Y","-4","-2","0","2","4"]])
        self.play(Write(table_1))
        self.wait(3)
        self.play(Unwrite(table_1))
        
        number_plane_scaled = Axes(
            x_range=[-5, 5, 1], 
            y_range=[-5, 5, 1]  
        )
        self.play(Create(number_plane_scaled), run_time=3)
        self.wait(1)

        dot_1 = Dot(number_plane_scaled.coords_to_point(-2, -4))
        dot_2 = Dot(number_plane_scaled.coords_to_point(-1, -2))
        dot_3 = Dot(number_plane_scaled.coords_to_point(0, 0))
        dot_4 = Dot(number_plane_scaled.coords_to_point(1, 2))
        dot_5 = Dot(number_plane_scaled.coords_to_point(2, 4))
        group = VGroup(dot_1, dot_2, dot_3, dot_4, dot_5)
        line = Line(dot_1, dot_5)
        
        label_1 = Tex(r"\scriptsize$(-2, -4)$").next_to(dot_1, LEFT)
        label_2 = Tex(r"\scriptsize$(-1, -2)$").next_to(dot_2, LEFT)
        label_3 = Tex(r"\scriptsize$(0, 0)$").next_to(dot_3, UP+LEFT)
        label_4 = Tex(r"\scriptsize$(1, 2)$").next_to(dot_4, LEFT)
        label_5 = Tex(r"\scriptsize$(2, 4)$").next_to(dot_5, LEFT)
        labels = VGroup(label_1, label_2, label_3, label_4, label_5)
    
        legend = MathTex("y=2x")
        legend.next_to(line, direction=UP + RIGHT)

        self.play(Create(group), Create(line), Create(labels), Write(legend), run_time=2)
        self.wait(1)