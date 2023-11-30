from manim import *

class seuim(Scene): 
    def construct(self):

        intro_text = Tex(r"Решение неравенств \\ методом интервалов").scale(1.7)
        self.wait(0.5)
        self.play(FadeIn(intro_text))
        self.wait(0.5)
        self.play(FadeOut(intro_text))


        inequality = MathTex(r"\frac{2^x-2}{(x+1)^3} \geqslant 0")
        inequality.to_edge(2 * UP, buff=1)
        solution = MathTex(r"\frac{2^x-2^1}{(x+1)^3} \geqslant 0")
        solution_1 = MathTex(r"\frac{x-1}{x+1} \geqslant 0")
        solution.next_to(inequality, DOWN)
        self.play(Write(inequality), run_time=3)
        self.wait()
        self.play(TransformFromCopy(inequality, solution))
        self.wait()
        self.play(TransformFromCopy(solution, solution_1))
        self.wait()

        arrow= Arrow(3 * LEFT, 3 * RIGHT, tip_length=0.2,
            buff=0).set_stroke(ORANGE, 2)
        dot_1 = Dot(LEFT, color=BLACK).set_stroke(ORANGE, 2) 
        dot_2 = Dot(RIGHT, 0.09, color=ORANGE).set_stroke(BLACK, 2)        
        number_line = VGroup(arrow, dot_1, dot_2).shift(DOWN)
        self.play(Create(number_line), run_time=3)
        self.wait()     

        label = MathTex("-1", "1", "x")
        label[0].next_to(dot_1, DOWN)
        label[1].next_to(dot_2, DOWN)
        label[2].next_to(arrow, DOWN)
        label[2].align_to(arrow, RIGHT)  
        signs = MathTex("+", "-", "+").arrange(buff=1.5)
        signs.next_to(arrow, UP, buff=0.15) 
        self.play(FadeIn(label, shift=UP),
            lag_ratio=0.5, run_time=2)
        self.wait()
        self.play(FadeIn(signs, shift=DOWN),
            lag_ratio=0.5, run_time=2)
        self.wait()

        answer = Tex(r"OTBET: $(-\infty ; -1)" +
                     r"\cup [1; +\infty)$", color=WHITE)
        answer.to_edge(DOWN, buff=1)
        self.play(Write(answer), run_time=3)
        self.wait(3)