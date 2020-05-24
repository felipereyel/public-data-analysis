from numpy import polyfit, poly1d, arange
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 12)


def create_disper_graph(result, result_headers, regiao):
    x = result[result_headers[0]].to_numpy().astype('float64')
    y = result[result_headers[1]].to_numpy().astype('float64')

    z = polyfit(x, y, 1)
    p = poly1d(z)

    plt.plot(x,p(x),"r-")
    plt.scatter(x,y, s=4)

    rsqr_score = r2_score(y, p(x))
    title = f"{regiao}\n" + \
            f"Coeficiente {float(p[1]):.2f} porcento por hora aula\n" + \
            f"R2 Score: {rsqr_score:.4f}"

    plt.title(title)
    plt.savefig(f'../q2/{regiao}.png')
    plt.clf()
  

def create_bar_graph(data, key, result_key, ratio, regiao, opt_order):
    objects = data[key].to_numpy()
    y_pos = arange(len(objects))
    performance = data[result_key].to_numpy().astype('float64')

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.title(
        f'A {key} {opt_order[0]} tem influência de' + \
        f'\n{(ratio*100 - 100):.2f}% sobre o TDI em relação\n' + \
        f'a {key} {opt_order[1]}, no {regiao}'
    )
    plt.savefig(f'../q1/{regiao}.png')
    plt.clf()