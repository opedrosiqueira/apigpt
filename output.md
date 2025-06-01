1. **Mensagem de boas-vindas com data atual**

   * Crie o arquivo `src/routes/03/exercicios/01/+page.server.js` que retorna um objeto com uma mensagem de boas-vindas e a data atual do servidor.
   * Em seguida, crie o componente `+page.svelte` que exibe essa mensagem e a data formatada.

2. **Mensagem personalizada com parâmetro de rota**

   * Crie a rota `src/routes/03/exercicios/02/[nome]/` que exibe uma mensagem de boas-vindas personalizada com base no valor do parâmetro de rota `nome`.

3. **Mensagem personalizada com parâmetro de consulta**

   * Crie a rota `src/routes/03/exercicios/03/` que exibe uma mensagem de boas-vindas com base no parâmetro de consulta `nome`.
   * Caso o parâmetro não seja informado, exiba uma mensagem padrão.

4. **Formulário com verificação de idade**

   * Implemente a rota `src/routes/03/exercicios/04/` com os seguintes arquivos:

     * `+page.server.js`: recebe os parâmetros de consulta `nome` e `data_nascimento`. Retorna `true` e o `nome` se a idade for maior ou igual a 18 anos; se a idade for menor que 18 anos, retorna `false`; se o nome ou a idade não foram informados, retorna `undefined`.
     * `+page.svelte`: exibe um formulário com os campos `nome` e `data_nascimento`, enviado para a própria página. Caso o servidor retorne `true`, exibe uma mensagem de boas-vindas com o nome; se `false`, exibe uma mensagem de acesso negado; se `undefined`, não exibe nenhuma mensagem.

Considere o seguinte arquivo de banco de dados somente-leitura `src/lib/server/03/produtos.js`:

    export const produtos = [
    {
        id: 1,
        titulo: 'Notebook Gamer X1',
        descricao: 'Notebook potente com placa de vídeo dedicada e tela 144Hz.',
        preco: 4999.90,
        categoria: 'informatica'
    },
    {
        id: 2,
        titulo: 'Mouse Sem Fio',
        descricao: 'Mouse ergonômico com conexão Bluetooth.',
        preco: 89.90,
        categoria: 'informatica'
    },
    {
        id: 3,
        titulo: 'Smartphone YZ Pro',
        descricao: 'Celular com câmera de 108MP e bateria de longa duração.',
        preco: 3499.00,
        categoria: 'telefonia'
    },
    {
        id: 4,
        titulo: 'Fone de Ouvido Bluetooth',
        descricao: 'Fone com cancelamento de ruído e autonomia de 30 horas.',
        preco: 299.90,
        categoria: 'audio'
    },
    {
        id: 5,
        titulo: 'TV 55" 4K UHD',
        descricao: 'Smart TV com controle por voz e suporte a HDR10.',
        preco: 2799.99,
        categoria: 'televisores'
    },
    {
        id: 6,
        titulo: 'Teclado Mecânico RGB',
        descricao: 'Teclado com switches azuis e iluminação colorida.',
        preco: 349.00,
        categoria: 'informatica'
    },
    {
        id: 7,
        titulo: 'Caixa de Som Portátil',
        descricao: 'Caixa com som estéreo potente e resistência à água.',
        preco: 199.90,
        categoria: 'audio'
    }
    ];

5. **Exibição por categoria**

   * Crie a rota `src/routes/04/produtos/[categoria]/` que exibe apenas os produtos cuja categoria corresponde ao parâmetro de rota `categoria`.

6. **Busca por texto**

   * Na página da rota acima, adicione um formulário com o campo `busca`, que filtra os produtos cujo **título** ou **descrição** contenham o texto digitado.

7. **Filtro por faixa de preço**

   * Amplie o formulário anterior adicionando os campos `min` e `max`. Ao enviar o formulário, exiba apenas os produtos cujo preço esteja entre os valores informados.
   * Se um dos campos estiver vazio, ele deve ser ignorado no filtro.