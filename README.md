## Web Crawler TriMania

Este projeto contém um web crawler em Python para extrair os resultados do sorteio da TriMania do site: [https://www.trimania.com.br/vale/](https://www.trimania.com.br/vale/).

### Requisitos

- Python 3.6 ou superior
- beautifulsoup4==4.9.3
- requests==2.25.1

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/trimania_crawler.git
```

2. Acesse o diretório do projeto:

```bash
cd trimania_crawler
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Como usar

1. Abra o arquivo trimania_crawler.py e altere a variável url para a data do sorteio desejada, seguindo o padrão do exemplo:

```python
url = "https://www.trimania.com.br/vale/?DtSorteio=2021-05-23&ordem=bola#resultado"
```

2. Execute o script:

```bash
python trimania_crawler.py
```

O script extrairá e imprimirá os resultados do sorteio da TriMania para a data especificada no link fornecido.

### Observações

O funcionamento correto deste web crawler depende da estrutura do site da TriMania. Se a estrutura do site mudar, será necessário atualizar o código de acordo.

### Contribuições

Se você encontrar algum problema no código ou quiser propor melhorias, sinta-se à vontade para abrir uma Issue ou enviar um Pull Request para este repositório.

### Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

### Suporte

Se você tiver alguma dúvida ou precisar de suporte, entre em contato com o desenvolvedor através do e-mail darioajr@gmail.com.

### Créditos

Este projeto foi desenvolvido por Dario Alves Junior. Agradecemos a todos os colaboradores e contribuintes deste projeto.