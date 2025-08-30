# Módulo: `queue_management`

## Regras de Acesso

- **Cliente:** só vê seus próprios tickets no portal.  
- **Funcionário:** vê todos os tickets relacionados ao seu serviço.  
- **Gerente:** acessa estatísticas e relatórios gerais.  

---

## Relatórios

- **PDF de resumo diário:** total de atendimentos, tempo médio, cancelamentos.  
- **Dashboard interativo (OWL):** gráficos de desempenho em tempo real.  

---

## Lógica de Negócio

- Ticket só pode ser criado para **horários disponíveis**.  
- Se o cliente não comparecer em **X minutos**, o ticket muda para `cancelled`.  
- Operador pode **chamar o próximo ticket** da fila.  

---

# Manual de Uso

## Cliente
1. Acesse o **portal → Meus Tickets**.  
2. Escolha o **serviço e horário** desejado.  
3. Gere o ticket → um **QRCode é exibido**.  
4. No dia/hora marcada, **mostre o QRCode ao atendente**.  

---

## Funcionário
1. Acesse o menu **Gestão de Tickets**.  
2. Visualize os tickets em **Kanban**.  
3. Clique em **Chamar próximo**.  
4. Após o atendimento, marque como **Done**.  

---

## Gerente
1. Acesse o **Dashboard de Atendimento**.  
2. Visualize **estatísticas** (tempo médio, tickets atendidos, cancelamentos).  
3. Gere relatórios em **PDF**.  

---

# Conjunto de Entregas
- **Contrato do Projeto**  
-  **Workflow definido**  
- **UML (classes, estados, fluxo)**  
-  **Documentação técnica (este arquivo)**  
-  **Manual de uso**  

