## Modelos

### `queue.service`
- **Nome do serviço**
- **Tempo médio de atendimento**
- **Ativo/Inativo**

### `queue.ticket`
- **Cliente** (`res.partner`)
- **Serviço** (`queue.service`)
- **Número do ticket** (sequência automática)
- **Estado:** `draft`, `waiting`, `called`, `done`, `cancelled`
- **Data/hora de agendamento**
- **QRCode** (campo binário)

---

## Views

- **Kanban:** operadores visualizam tickets em tempo real.  
- **Form/Tree:** gerenciamento interno de tickets.  
- **Portal OWL:** cliente gera ticket, visualiza QRCode e posição na fila.