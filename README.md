<body>
    <h1>Lista Encadeada Simples em Python</h1>
    <p>Este projeto implementa uma <strong>rede de atendimento hospitalar</strong> baseada em uma <strong>lista encadeada simples</strong>, priorizando pacientes de acordo com seu nível de urgência e número de identificação.</p>

   <h2>🏥 Funcionalidades</h2>
    <ul>
        <li><strong>Adicionar pacientes à fila de espera</strong>:
            <ul>
                <li>Pacientes com prioridade: <strong>A - Amarelo</strong>.</li>
                <li>Pacientes sem prioridade: <strong>V - Verde</strong>.</li>
            </ul>
        </li>
        <li><strong>Organizar a lista de pacientes</strong>:
            <ul>
                <li>Pacientes com prioridade (A) têm precedência.</li>
                <li>Pacientes sem prioridade (V) são atendidos por ordem de chegada.</li>
            </ul>
        </li>
        <li><strong>Mostrar a lista de espera</strong>: Exibe os pacientes na fila com suas prioridades e números.</li>
        <li><strong>Atender pacientes</strong>: Remove o primeiro paciente da fila (baseado em prioridade).</li>
        <li><strong>Encerrar o programa</strong>: Finaliza o sistema de forma segura.</li>
    </ul>

   <h2>⚙️ Regras do Sistema</h2>
    <ol>
        <li><strong>Prioridades</strong>:
            <ul>
                <li><strong>A - Amarelo</strong>: Pacientes com prioridade.</li>
                <li><strong>V - Verde</strong>: Pacientes sem prioridade.</li>
            </ul>
        </li>
        <li><strong>Numeração</strong>:
            <ul>
                <li>Pacientes <strong>com prioridade (A)</strong>: números a partir de <strong>201</strong>.</li>
                <li>Pacientes <strong>sem prioridade (V)</strong>: números a partir de <strong>1</strong>.</li>
            </ul>
        </li>
    </ol>

   <h2>📋 Menu do Programa</h2>
    <p>O sistema apresenta o seguinte menu interativo:</p>
    <ol>
        <li><strong>Adicionar paciente à fila</strong>: Insere um paciente com prioridade e número definido pelo usuário.</li>
        <li><strong>Mostrar pacientes na fila</strong>: Exibe a lista de espera atual.</li>
        <li><strong>Chamar paciente</strong>: Remove e chama o próximo paciente da fila.</li>
        <li><strong>Sair do sistema</strong>: Finaliza o programa.</li>
    </ol>

   <h2>💻 Como Executar o Código</h2>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://github.com/seu-usuario/ListaEncadeadaSimples-Python.git</code></pre>
        </li>
        <li>Navegue até o diretório do projeto:
            <pre><code>cd ListaEncadeadaSimples-Python</code></pre>
        </li>
        <li>Execute o programa:
            <pre><code>python lista_encadeada.py</code></pre>
        </li>
    </ol>

   <h2>📊 Exemplos de Saída</h2>

   <h3>1. Inserindo Pacientes com Prioridade Amarela</h3>
    <p>Pacientes prioritários têm números começando em 201.</p>
    <img src="https://github.com/user-attachments/assets/3c6a2a3a-6673-41d4-97c8-0677147ab978" alt="Inserindo Paciente Amarelo">

   <h3>2. Inserindo Pacientes com Prioridade Verde</h3>
    <p>Pacientes não prioritários têm números começando em 1.</p>
    <img src="https://github.com/user-attachments/assets/e7c74b5f-85f6-49fe-a42b-bc80d1f0e2d0" alt="Inserindo Paciente Verde">

   <h3>3. Exibindo a Lista de Pacientes</h3>
    <p>A lista é exibida com pacientes organizados por prioridade.</p>
    <img src="https://github.com/user-attachments/assets/58f2cbc8-e89d-4041-8159-2822d9756de8" alt="Imprimindo Lista de Pacientes">

   <h3>4. Chamando o Próximo Paciente</h3>
    <p>O próximo paciente na fila (com prioridade mais alta) é chamado.</p>
    <img src="https://github.com/user-attachments/assets/2523da19-66ef-4538-a2b6-42d7977c0c6b" alt="Chamando Paciente">

   <h3>5. Finalizando o Programa</h3>
    <p>O sistema é encerrado de forma segura.</p>
    <img src="https://github.com/user-attachments/assets/a3c092ff-b2c7-46c1-9255-511b8d1916b6" alt="Finalizando Programa">

   <h2>🛠️ Estrutura do Código</h2>
    <p>O projeto é composto pelas seguintes classes e funções:</p>

   <h3>Classes</h3>
    <ul>
        <li><code>elementoLista</code>: Representa um elemento da lista encadeada.</li>
        <li><code>ListaEncadeada</code>: Implementa a estrutura de dados com suporte a inserções e remoções.</li>
    </ul>

   <h3>Funções Principais</h3>
    <ul>
        <li><code>inserir</code>: Adiciona um paciente à lista com ou sem prioridade.</li>
        <li><code>inserirComPrioridade</code>: Insere pacientes com prioridade no início da fila.</li>
        <li><code>imprimirListaEspera</code>: Exibe os pacientes na lista.</li>
        <li><code>atenderPaciente</code>: Remove o próximo paciente da fila.</li>
        <li><code>menu</code>: Menu interativo para navegar pelas funcionalidades do sistema.</li>
    </ul>
</body>
