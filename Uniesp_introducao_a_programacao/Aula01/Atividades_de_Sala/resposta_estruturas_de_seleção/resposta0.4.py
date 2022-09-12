#média aritimética de duas provas do mesmo bimestre
a1 = float(input("Valor da primeira avaliação: "))
a2 = float(input("Valor da segunda avaliação: "))
soma = (a1 + a2) / 2 
if soma >= 6:
    print(f"PARABÊNS VOCÊ FOI APROVADO\nNOTA FINAL: {soma}")
if soma < 6:
    print(f"ALUNO REPROVADO\nNOTA FIANAL: {soma}\nREVISE O ASSUNTO PARA MELHORES RESULTADOS")
#O aluno será aprovado com media apartir de 6