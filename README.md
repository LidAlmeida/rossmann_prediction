# PREVISÃO DE VENDAS - ROSSMANN DROGERIEMARKT
![Imagem de uma loja da rede Rossmann](img/loja_rossmann.jpg)


## A Rossmann Drogeriemarkt

A Rossmann Drogeriemarkt é uma rede de farmácias e drogarias alemã, fundada em 1972 por Dirk Roßmann. Atualmente, é uma das maiores redes de drogarias da Europa, com mais de 4.500 lojas em 8 países. A empresa oferece uma ampla variedade de produtos, incluindo medicamentos, produtos de higiene pessoal, beleza, bem-estar e alimentos saudáveis.

## O problema de negócio

A Rossmann Drogeriemarkt valoriza a comodidade e satisfação dos clientes. Com esse objetivo, a empresa está sempre em busca de oferecer estruturas cada vez mais completas. Investindo em melhorias que tornem a experiência de compra ainda mais agradável, como vagas de estacionamento, sistemas de ar condicionado e banheiros para clientes. Neste contexto, a previsão de vendas para as próximas seis semanas é fundamental para que o CFO possa determinar os valores a serem investidos em reformas para cada loja da rede.

Atualmente, as previsões são realizadas utilizando a média. Embora seja uma abordagem simples, ela apresenta algumas limitações. Em primeiro lugar, a média não leva em consideração as variações ou tendências sazonais das vendas. Por exemplo, as vendas podem ser maiores em um determinado dia da semana ou mês do ano. Além disso, a média pode não levar em conta outros fatores que podem afetar as vendas, como eventos externos ou mudanças nas preferências dos consumidores. Por outro lado, as técnicas de machine learning podem ajudar a modelar e prever as vendas com base em múltiplos fatores, incluindo tendências sazonais, dados demográficos, preços, promoções, entre outros. Isso pode levar a previsões mais precisas e aperfeiçoar as estratégias de negócios.

Para enfrentar essa questão, apresentamos um projeto que utiliza técnicas de Data Science para prever as vendas de cada loja de forma automática e mais precisa. Com isso, o CFO terá informações mais confiáveis e consistentes para determinar o investimento em cada loja, melhorando assim a estrutura e o atendimento ao público, , mantendo a posição de destaque da Rossmann no mercado de drogarias na Alemanha.


### Premissas
    
Foram estabelecidas as seguintes premissas para a construção da solução de previsão de vendas:

1. A disponibilidade da previsão de vendas será via aplicativo do Telegram, permitindo sua consulta a qualquer momento.

2. A previsão de vendas será feita exclusivamente para as lojas que tiveram vendas registradas na base de dados.

3. Para a realização da previsão de vendas, serão excluídos os dias em que as lojas estiveram fechadas.


## Descrição dos dados

Os dados utilizados neste projeto foram coletados a partir da plataforma Kaggle e englobam informações históricas de vendas em 1.115 lojas da rede Rossmann. As descrições iniciais dos atributos presentes nos dados estão listadas abaixo:


 Variável | Descrição
:------------|:---------
Store | ID exclusivo para cada loja
Sales | O volume de vendas de um determinado dia (variável que será prevista)
Customers | Número de clientes em um determinado dia
Open | Indicador para funcionamento da loja, aberta: 0 = fechada e 1 = aberta
StateHoliday | Feriado estadual. Normalmente todas as lojas, com poucas exceções, estão fechadas nos feriados estaduais. Todas as escolas estão fechadas nos feriados e fins de semana. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
SchoolHoliday | Indica se store e date foram afetadas pelo fechamento de escolas públicas
StoreType | Diferencia entre os 4 modelos de loja diferentes (a, b, c, d)
Assortment | Descreve um nível de sortimento (a = basic, b = extra, c = extended)
Competition_distance | Distância em metros até a loja concorrente mais próxima
Competition_open_since (_month/_year) | Fornece o ano e o mês aproximados da hora em que o concorrente mais próximo foi aberto
Promo | Indica se uma loja está realizando uma promoção naquele dia (0 = store is not participating, 1 = store is participating)
Promo2 | Promo2 é uma promoção contínua e consecutiva para algumas lojas (0 = store is not participating, 1 = store is participating)
Promo2_since(_year/_week) | Descreve o ano e a semana do calendário em que a loja começou a participar da promo2
Promo_interval | Descreve os intervalos consecutivos em que a Promo2 é iniciada, nomeando os meses em que a promoção é iniciada novamente. E.g: "Feb,May,Aug,Nov" significa que cada rodada começa em February, May, August, November de qualquer ano para essa loja.


## Estratégia de solução

![Ciclo Crisp DS](img/crisp.png)

**Passo a passo:**

1. Definição do problema: compreender o contexto do negócio e os objetivos do projeto.

2. Coletar e limpar os dados: coletar os dados e executar as etapas de limpeza e pré-processamento de dados. Incluindo: tratamento de valores ausentes, valores discrepantes e a transformação dos dados para torná-los utilizáveis para análise.

3. Explorar os dados: realizar análise exploratória de dados (EDA) para entender as características dos dados, identificar padrões e tendências e gerar hipóteses para análise posterior.

4. Feature engineering: selecionar e extrair features relevantes dos dados e criar novas features que possam melhorar o desempenho preditivo do modelo.

5. Construção de modelo: selecionar um modelo apropriado com base no problema e nos dados. Treinar e avaliar o modelo usando as métricas MAE, MAPE, RMSE.

6. Otimizar e interpretar: otimizar o modelo para melhorar seu desempenho. Interpretar os resultados do modelo e extrair insights deles.

7. Implantação: Implantar o modelo em um ambiente de produção e monitorar seu desempenho.

8. Comunicação e documentação: Comunicar os resultados do projeto aos stakeholders relevantes e documentar o processo e os resultados para referência futura.

## Ferramentas utilizadas

- Python
- Bibliotecas Python: pandas, Matplotlib, Seaborn, Numpy, sidetable e Sklearn
- Jupyter Notebook e VSCode
- Git e Github

## Técnicas utilizadas

- Análise Exploratória de Dados (EDA)
- Seleção de recursos com a utilização do Boruta
- Algoritmos de Regressão: foram testados diferentes algoritmos de regressão, incluindo Linear Regression, Lasso Regression, Random Forest e XGBoost.
- Validação Cruzada e Otimização de Hiperparâmetros
- Métricas de Desempenho: para avaliar o desempenho dos modelos, utilizamos RMSE, MAE e MAPE.


## Principais insights

Um conjunto de fatores pode afetar o desempenho das vendas nas lojas físicas de uma rede de drogarias. Para definir o objetivo da análise e identificar as variáveis relevantes, foi criado um mapa mental que trouxe clareza à estrutura da análise e permitiu a identificação de padrões e tendências.

![Mapa Mental](img/mind_map.jpg)

### A proximidade com uma loja concorrente não afeta negativamente as vendas

Ao considerarmos a presença de concorrentes próximos, é comum esperar uma redução nas vendas e no número de clientes, pois os consumidores têm mais opções de escolha e podem optar por comprar em lojas concorrentes mais próximas. No entanto, a análise de dados sugere que a distância das lojas concorrentes não tem influência na média de vendas. Outros fatores, como localização, preço e promoções, podem ter uma influência maior sobre as vendas.

É possível considerar hipóteses alternativas que explicam esse resultado, como preços mais competitivos oferecidos pela rede Rossmann em relação aos seus concorrentes. Além disso, a loja pode oferecer produtos ou serviços que se destacam dos concorrentes próximos, atraindo clientes mesmo que haja lojas concorrentes nas proximidades.

A fidelização de clientes também pode ser um fator importante, onde a loja pode ter uma base de clientes fiéis que preferem comprar naquela loja, independentemente da distância ou de outras opções de concorrentes próximos. Por fim, a localização privilegiada da loja pode compensar a proximidade dos concorrentes, atraindo um fluxo maior de clientes.

Esses fatores, combinados ou isolados, podem explicar por que a presença de concorrentes próximos não afeta as vendas e o número de clientes da rede Rossmann. Isso sugere que, ao invés de se preocupar com a presença de concorrentes próximos, as empresas podem se concentrar em oferecer preços competitivos, produtos e serviços diferenciados, fidelizar seus clientes e encontrar localizações privilegiadas para suas lojas.

![Scatter plot Sales vs Competition Distance](reports/figures/sales_vs_competitiondistance.png)


###  Lojas com promoções extendidas não vendem mais

Ao analisarmos as vendas médias ao longo das semanas do ano, é possível observar que os períodos de promoção tradicional têm as maiores médias de vendas em todas as semanas do ano, seguidos pelo período de promoção tradicional com promoção estendida. Curiosamente, quando o período de promoção é somente o estendido é que se observa a menor média de vendas.

Existem algumas possíveis hipóteses que podem explicar esses resultados. Uma delas é que a promoção tradicional pode estar mais enraizada na cultura do consumidor e portanto, os clientes estão mais inclinados a comprar durante esse período. Além disso, a promoção estendida pode levar à diminuição da importância da promoção, tornando-a menos atraente para os clientes.

A tendência de aumento nas médias de vendas nas últimas semanas do ano para o período promocional tradicional + promoção extendida e o período promocional tradicional pode estar relacionada com o fato de que muitas pessoas deixam as compras de presentes para a última hora, buscando aproveitar as promoções de última hora. Por fim, a queda nas médias de vendas observada nas últimas semanas e nas primeiras semanas do ano, tanto para o período não promocional quanto para o período promocional estendido, pode estar relacionada à redução do poder de compra do consumidor após o período de gastos durante as festas de fim de ano.

É importante notar que, apesar das promoções parecerem ter um efeito positivo nas vendas, o gráfico de linhas mostra que as quedas nas médias de vendas são coincidentes, independentemente da presença de promoções nas lojas. Isso pode indicar outras variáveis, além da promoção, que afetam o comportamento do consumidor nas últimas semanas do ano.

![Lineplot Sales and Promo](reports/figures/sales_promo_weekofyear.png)


### As vendas durante o Natal não são maiores em comparação a outros feriados

Utilizando o gráfico de boxplot para analisar as medianas das vendas para cada tipo de feriado em cada ano (2013, 2014 e 2015), podemos concluir que as vendas durante o período de Natal não apresentam diferenças significativas em relação a outros feriados. Observamos que a mediana das vendas durante o Natal é semelhante à mediana das vendas em outros feriados, como dias regulares e feriados públicos.

No entanto, o feriado de Easter Holiday (Páscoa) apresentou uma caixa mais ampla em termos de distribuição dos dados, o que sugere que houve uma maior variabilidade nas vendas nesse período. Ao analisar as medianas de vendas para cada tipo de feriado em cada ano, constatamos que em 2013 a mediana de vendas durante o feriado de Páscoa superou a do Natal. Em contrapartida, em 2014 as vendas no período de Natal foram superiores a todos os outros tipos de feriado.

Existem algumas hipóteses que podem explicar esses resultados. Primeiramente, é possível que o Natal não seja um feriado que estimule a compra de produtos em drogarias, mesmo que seja um momento importante para as famílias se reunirem e trocarem presentes. Além disso, o feriado de Páscoa pode estar associado a um maior consumo de produtos específicos, como chocolates e presentes relacionados à Páscoa, o que pode levar a uma maior variabilidade nas vendas nesse período.

Por fim, é válido destacar que as variações nas vendas entre diferentes feriados e anos podem ser influenciadas por fatores externos, como mudanças na economia ou no comportamento dos consumidores.

*Os dados das vendas durante o período de Natal de 2015 não estão disponíveis na base de dados*

![State Holiday and Sales](reports/figures/sales_stateholiday.png)


### Padrões sazonais nas vendas ao longo de três anos e possíveis fatores influenciadores

Ao analisar o gráfico de linhas referente às vendas nos anos de 2013, 2014 e 2015, é possível identificar padrões de comportamento sazonal das vendas. Em 2013, houve picos de vendas em março, julho e dezembro, com dezembro apresentando as maiores vendas. Já em 2014, houve um platô nas vendas de março a junho, seguido por uma queda até novembro, com dezembro registrando o pico de vendas. Embora os dados de 2015 não estejam completos, os primeiros sete meses do ano mostraram um comportamento semelhante ao do ano anterior, com picos de vendas em março e julho e vendas mais baixas em fevereiro e maio.

Com base nesses padrões, é possível formular hipóteses sobre os fatores que influenciam as vendas. Uma hipótese é que a sazonalidade pode ter influenciado nas vendas, com certos meses sendo mais propícios para as compras do que outros. Outra hipótese é que campanhas promocionais podem ter afetado as vendas, especialmente em períodos de pico, como dezembro. Além disso, a situação econômica do país pode ter afetado as vendas em determinados períodos, como a queda nas vendas registrada em 2014, que pode ter sido influenciada pela crise econômica que o país enfrentou na época.

![Sales in 2013, 2014 and 2015](reports/figures/sales_year.png)


## Modelos de Machine Learning

Neste projeto, uma etapa fundamental foi a modelagem de Machine Learning para a previsão de vendas em cada loja. Para isso, foram treinados cinco modelos utilizando validação cruzada de séries temporais: média, regressão linear, regressão Lasso (regressão linear regularizada), Random Forest Regressor e XGBoost Regressor.

A média das vendas era o método padrão de previsão das vendas na rede de drogarias e foi empregado como linha de base para a comparação com outros algoritmos. Para avaliar o desempenho de cada modelo, utilizou-se o Root Mean Squared Error (RMSE), uma métrica comumente utilizada para medir a precisão de modelos de regressão. Quanto menor o valor do RMSE, melhor é o desempenho do modelo.

Os resultados iniciais mostraram que todos os cinco algoritmos tiveram desempenhos diferentes. A regressão linear apresentou o pior desempenho, seguida pela regressão Lasso e pelo modelo médio. Por outro lado, os modelos de árvore (Random Forest Regressor, XGBoost Regressor) apresentaram os melhores desempenhos.

É importante ressaltar que esses resultados são apenas iniciais e que pode haver espaço para melhorias por meio de ajustes nos parâmetros dos modelos, inclusão de novas variáveis ou outras técnicas de pré-processamento de dados. O objetivo é encontrar o modelo que apresente a melhor precisão na previsão das vendas das lojas, o que pode contribuir significativamente para a tomada de decisões no âmbito do negócio.

| Modelo | MAE | MAPE | RMSE |
| :------------|:---------|:---------|:---------
| Regressão Linear | 2204.71 ± 113.73 | 0.36 ± 0.01 | 3041.01 ± 184.58 |
| Regressão Lasso | 2248 ± 90.11 | 0.37 ± 0.01 | 3133.63 ± 167.91 |
| Random Forest Regressor | 1438.87 ± 164.4 | 0.23 ± 0.02 | 2089.74 ± 245.91 |
| XGBoost Regressor | 1432.58 ± 138.61 | 0.23 ± 0.02 | 1981.86 ± 208.18 |

Existem diversas possíveis explicações para o fato do Random Forest Regressor e XGBoost Regressor terem apresentado melhor desempenho do que a Regressão Linear e Regressão Lasso, em comparação com o Modelo Médio simples. Uma possível explicação é que os algoritmos de Random Forest e XGBoost são mais complexos e flexíveis do que os algoritmos de regressão linear, permitindo que eles capturem relações mais complexas entre as variáveis de entrada e a variável de saída, neste caso, as vendas. Além disso, Random Forest e o XGBoost são algoritmos de aprendizado de máquina baseados em árvores de decisão, o que significa que eles podem capturar interações não-lineares entre as variáveis de entrada e a saída, enquanto a regressão linear é limitada a relações lineares.

Outra possível explicação é que os algoritmos de Random Forest e XGBoost são menos sensíveis a outliers e dados não-lineares do que a Regressão Linear e Regressão Lasso, o que pode ser especialmente importante em um conjunto de dados complexo como a previsão de vendas. Além disso, o XGBoost é um algoritmo baseado em gradient boosting, que é uma técnica de otimização que ajusta os pesos dos exemplos de treinamento para melhorar o desempenho do modelo, o que pode ajudar a melhorar a precisão da previsão de vendas.

O modelo **XGBoost** foi selecionado como o melhor modelo para ajuste de hiperparâmetros, pois apresentou o menor RMSE entre os modelos avaliados. Vale ressaltar que, mesmo considerando outras métricas, como o MAPE, que apontou um desempenho semelhante entre Random Forest Regressor e o XGBoost, optou-se pela utilização do XGBoost devido à sua maior eficiência.

Após o ajuste de hiperparâmetros do modelo XGBoost por meio de Random Search, observou-se uma melhoria significativa no desempenho do modelo. As alterações realizadas nos parâmetros permitiram que o modelo capturasse com maior precisão as relações não-lineares entre as variáveis de entrada e saída, o que resultou em previsões mais precisas das vendas das lojas da rede de drogarias. 

| Modelo | MAE | MAPE | RMSE |
|:------------| :------------ | :------------ | :------------ |
| XGBoost Regressor | 830 | 0.12 | 1176.15 |


## Resultados de Negócios



## Lessons Learned

## Next Steps

##  👩🏻‍💻 Autora
