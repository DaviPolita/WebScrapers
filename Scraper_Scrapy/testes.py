import re
string = ['\r\n          \r\n    \r\n            ',
          '1001 Metalurgica e Servicos Ltda',
          '         \r\n            ',
          'CNPJ:',
          ' 02751657000116 ',
          '\r\n            ',
          'Inscrição Estadual:',
          ' 049.404.036 PP ',
          '\r\n            ',
          'Razão Social:',
          '  1001 Metalurgica e Servicos Ltda  ',
          '\r\n            ',
          'Nome Fantasia:',
          ' 1001 Metalurgica \r\n            ',
          '\r\n\r\n            ',
          'Atividade Econômica:',
          '\r\n            \r\n            \r\n            ',
          'CNAE:',
          ' ',
          'C2511000',
          '\r\n            ',
          'Descrição CNAE:',
          ' ',
          'Fabricação de estruturas metálicas',
          '\r\n\r\n\r\n            ',
          'Lista de Produtos:',
          '\r\n\r\n            \r\n\r\n                    ',
          ' Estrutura metalica em geral',
          ' ',
          '\r\n\r\n                \r\n\r\n            ',
          'Lista de Insumos:',
          '\r\n\r\n            \r\n\r\n                    ',
          ' Aco carbono',
          '\r\n\r\n                \r\n\r\n                    ',
          ' Ferro',
          '\r\n'
          '\r\n'
          '                \r\n'
          '                        \r\n'
          '            ',
          'Número Total de Funcionários:',
          '\r\n\r\n            ',
          '10',
          '\r\n\r\n            ',
          '\r\n\r\n             ',
          'Quanto ao Comércio internacional, a empresa se considera:',
          '\r\n\r\n            ',
          ' Sem Interesse',
          '\r\n\r\n            ',
          '\r\n\r\n             ',
          'Contato Comercial:',
          '\r\n\r\n            ',
          'Logradouro:',
          ' ',
          'Via Urbana - Anexo 1, 2199',
          '\r\n            ',
          'Complemento:',
          ' ',
          '\r\n            ',
          'Bairro:',
          ' ',
          'CIA Sul',
          '\r\n            ',
          'Município:',
          ' ',
          'Simoes Filho',
          '\r\n            ',
          'Estado:',
          ' ',
          'BA',
          '\r\n            ',
          'CEP:',
          ' ',
          '43700-000',
          '\r\n            ',
          'Telefone:',
          ' ',
          '(71) 3594-7223  / (71) 3594-7226 / ',
          '\r\n            \r\n            ',
          'Email:',
          ' ',
          'carlosrsmiranda@uol.com.br',
          '\r\n            ',
          'Site:',
          ' ',
          ' \r\n'
          '            \r\n'
          '        \r\n'
          '        \r\n'
          '              \r\n'
          '    ']


string2 = [item.strip() for item in string]
string2 = list(filter(None, string2))
string2 = " ".join(string2)


lista_prod = re.search('Lista de Produtos:(.*)Lista de Insumos:', string2)
lista_ins = re.search('Lista de Insumos:(.*)Número Total', string2)
num_funcionarios = re.search('Total de Funcionários:(.*)Quanto ao', string2)

print(num_funcionarios.group(1))
# print(string2)

# s = 'asdf=5;iwantthis123jasd'
# result = re.search('asdf=5;(.*)123jasd', s)
# print(result.group(1))
