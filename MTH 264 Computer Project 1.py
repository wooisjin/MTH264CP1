import math


class Riemann:
    def __init__(self, function, range, problem):
        self.raw_function = function
        self.function = Function(function)
        self.range = range
        self.delta = 0
        self.problem = problem

    def lower_sum(self, n):
        total_area = 0
        for x in range(n):
            xL = self.range[0] + self.delta * x
            total_area += self.function.final_calculate(xL)
        return total_area * self.delta

    def upper_sum(self, n):
        total_area = 0
        for x in range(n):
            xL = self.range[0] + self.delta * (x+1)
            total_area += self.function.final_calculate(xL)
        return total_area * self.delta

    def midpoint(self, n):
        total_area = 0
        for x in range(n):
            xL = self.range[0] + self.delta * x + self.delta/2
            total_area += self.function.final_calculate(xL)
        return total_area * self.delta

    def trapezoid(self, n):
        total_area = 0
        for x in range(n+1):
            xL = self.delta * x + self.range[0]
            if xL != self.range[0] and xL != self.range[1]:
                total_area += 2*self.function.final_calculate(xL)
            else:
                total_area += self.function.final_calculate(xL)
        return (total_area * self.delta)/2

    def write_file(self):
        f = open("calculus_project1.txt", "a+")
        f.write("_______________________________\n"
        + self.raw_function+"  "+self.problem+"\n_______________________________\nRange: "+str(self.range)+"\n")
        f.write("     n:    |    Lower Sum    |    Upper Sum    |     Midpoint    |    Trapezoid    |\n")
        n_list = [2, 10, 100, 1000, 10000]
        for n in n_list:
            self.delta = (self.range[1] - self.range[0]) / n
            lower_sum = str(round(self.lower_sum(n), 12)).ljust(15)
            upper_sum = str(round(self.upper_sum(n), 12)).ljust(15)
            midpoint = str(round(self.midpoint(n), 12)).ljust(15)
            trapezoid = str(round(self.trapezoid(n), 12)).ljust(15)
            n_number = str(n).ljust(6)
            total_line = "n = "+n_number+" | "+lower_sum+" | "+upper_sum+" | "+midpoint+" | "+trapezoid+" | \n"
            f.writelines(total_line)
        f.close()


class Function:
    def __init__(self, function):
        self.function = function
        self.trig_list = ["cos", "sin", "tan", "sec", "csc", "cot"]
        self.state = ""
        self.new_function = ""
        self.new_x = 0

    def trigonometry_check(self):
        for trig_func in self.trig_list:
            if trig_func in self.function:
                if trig_func == "cos":
                    self.state = "cos"
                    break
                elif trig_func == "sin":
                    self.state = "sin"
                    break
                elif trig_func == "tan":
                    self.state = "tan"
                    break
                elif trig_func == "sec":
                    self.state = "sec"
                    break
                elif trig_func == "csc":
                    self.state = "csc"
                    break
                elif trig_func == "cot":
                    self.state = "cot"
                    break

    def solve_x(self, x):
        self.new_x = self.function.replace(self.state, "")
        final_x = self.new_x.replace("x", str(x))
        return eval(final_x)

    def calculate_trig(self, x):
        if self.state == "cos":
            return math.cos(self.solve_x(x))
        elif self.state == "sin":
            return math.sin(self.solve_x(x))
        elif self.state == "tan":
            return math.tan(self.solve_x(x))
        elif self.state == "sec":
            return 1/math.cos(self.solve_x(x))
        elif self.state == "csc":
            return 1/math.sin(self.solve_x(x))
        elif self.state == "cot":
            return 1/math.tan(self.solve_x(x))

    def final_calculate(self, x):
        self.trigonometry_check()
        trig_answer = self.calculate_trig(x)
        if self.state != "":
            final_function = self.function.replace(self.state + str(self.new_x), str(trig_answer))
            return eval(final_function)
        else:
            final_function = self.function.replace("x", str(x))
            return eval(final_function)


def run_problems():
    problem1 = Riemann("4/((x**2)+1)", [0, 1], "Problem A")
    problem2 = Riemann("sin(x**2)", [0, math.pi/2], "Problem B")
    problem3 = Riemann("2*(e**(-x**2))".replace("e", str(math.e)), [1, 2], "Problem C")
    problem1.write_file()
    problem2.write_file()
    problem3.write_file()
    print("Task Completed")


run_problems()

