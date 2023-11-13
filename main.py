from sympy import *
from sympy.plotting import plot
x, y, dy = symbols('x,y,dy')

# Inputs
input = [4*x**5+5*x**4,exp(x)*sin(x),((x**4+3*x)**-1), 3*x**2*(x**3+1)**7, cos(x)**4-2*x**2,x/(1+x**2), (x**2-1)/x, 3*x**2*(x**1/2), ln(x*exp(7*x)), (2*x**4+3*x**2-1)/(x**2), x**3*((2-x)**(1/5)), 2*x-4/sqrt(x),4*(3*x-1)**2/(x**2+7**x), sqrt(x**2+8), x/(sqrt(1-ln(x)**2)), 6/((3*x**2-pi)**4), (3*x**2-pi*x)**4/6, x/((x**2+sqrt(3*x))**5), (x*exp(x))**pi, (atan(2*x))**10, (exp(2*x)+exp(1))**(1/2), (x**6+1)**5*(4*x+7)**3,(7*x+sqrt(x**2+3))**6, (1/x+1/(x**2))/(x-1), x**Rational(2,3)-x**Rational(-1,3), ((2*x+5)/(7*x-9))**(1/2), sin(x)/cos(x), exp(x)*(x**2+3)*(x**3+4), (5*x**2-7*x)/(x**2+2), (ln(5*x**2+9))**3, ln(5*x**2+9)**3, cot(6*x), sec(x)**2*tan(x), asin(2**x), tan(cos(x)), ((x**2-1)**5-x)**3, sec(x) * sin(3*x), (x-1)**3/(x*(x+3)**4), log(3*x**2+4*x, 5)]
impInput = [x*exp(5*y)-3*y, x*y+y**2+x**3-7, sin(y)/(y**2+1)-3*x]


# Outputs
output = [diff(item, x) for item in input]
output.extend(solve(diff(item, x)+diff(item,y)*dy, dy) for item in impInput)
input.extend(impInput)

# Plotting the functions and their derivatives
plots = [plot(input[i],output[i], show=False) for i in range(len(input)-3)]
for i in range(len(plots)):
  plots[i].save(f'./plots/plot_{i+1}.png')

# Outputting to LaTeX
init_printing()
F = open('Output.tex', 'w')
F.write('\documentclass{article}\n\\usepackage{graphicx}\n\graphicspath{{./plots/}}\n\\begin{document}\n\\addtolength{\oddsidemargin}{-.875in}\n\\addtolength{\\topmargin}{-.875in}\n\\begin{table}\n\\begin{tabular}{ |c|c|c| }\n\hline\n Problem &   Function &       Derivative \\\\\n\hline\n')
for i in range(len(input)):
  F.write(f"{i+1} & $f(x)="+latex(input[i]).replace("atan",r"\arctan").replace("asin",r"\arcsin")+"$&$ f'(x)="+latex(output[i]).replace("atan",r"\arctan").replace("asin", r"\arcsin")+"$\\\\\n")
F.write('\hline\n\\bottomrule\n\end{tabular}\n\end{table}\n')
for i in range(len(plots)):
  F.write('\\begin{figure}\n\caption{The plot for f(x)=$'+ latex(input[i]).replace("atan",r"\arctan").replace("asin",r"\arcsin") + '$ and its derivative f\'(x)=$' + latex(output[i]).replace("atan",r"\\arctan").replace("asin",r"\\arcsin") + '$}\n\centering\n\includegraphics{plot_'+str(i+1)+'}\n\end{figure}')
F.close()