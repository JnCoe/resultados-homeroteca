# resultados-homeroteca
Este script simples toma como argumento uma página html salva localmente como resultado de busca da [Homeroteca Digital](http://bndigital.bn.gov.br/hemeroteca-digital/) e exporta no clipboard a contagem por edição e ano.

O arquivo "Homeroteca.html" serve de exemplo de utilização. Para testar o funcionamento do script basta rodar via linha de comando:

    python extrator.py Homeroteca.html
    
Note que isso irá sobrescrever o conteúdo da sua área de transferência com a tabela resultado.

Para utilizar para outros fins faça uma busca na homeroteca, abra o jornal de interesse nos resultados e salve o html localmente no mesmo diretório do script. Depois, basta executar o comando como explicitado acima.

Idealmente no futuro esse script irá coletar o resultado de maneira autônoma usando Selenium.