def main():
    s_tot = 0
    q_imp = 0
    for i in range(1,501):
        if i%2 != 0:
            if i%3 == 0:
                q_imp += 1
                s_tot += i
    print(f'A soma de todos os {q_imp} números impares multiplos de 3 no intervalo [1,500] é: {s_tot}')
main()
