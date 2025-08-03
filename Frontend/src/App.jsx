import { useEffect, useState } from 'react';
import axios from 'axios';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import React from 'react';

function App() {
  const [contacts, setContacts] = useState([]);
  const [groups, setGroups] = useState([]);
  const [message, setMessage] = useState('');
  const [date, setDate] = useState(new Date());
  const [groupId, setGroupId] = useState('');
  const [scheduled, setScheduled] = useState([]);

  useEffect(() => {
    fetchGroups();
    fetchMessages();
  }, []);

  const fetchGroups = async () => {
    try {
      const res = await axios.get('/api/groups/');
      setGroups(res.data);
    } catch (error) {
      console.error('Error al cargar los grupos:', error);
    }
  };

  const fetchMessages = async () => {
    try {
      const res = await axios.get('/api/messages/');
      const sorted = res.data.sort(
        (a, b) => new Date(a.scheduled_time) - new Date(b.scheduled_time)
      );
      setScheduled(sorted);
    } catch (error) {
      console.error('Error al cargar los mensajes:', error);
    }
  };

  const handleSchedule = async () => {
    if (!message.trim() || !groupId || !date) {
      alert('Por favor completa todos los campos.');
      return;
    }

    try {
      await axios.post('/api/messages/', {
        content: message,
        scheduled_time: date.toISOString(),
        group_id: parseInt(groupId),
      });
      setMessage('');
      fetchMessages();
    } catch (err) {
      console.error('Error al programar el mensaje:', err);
      alert('Hubo un error al programar el mensaje.');
    }
  };

  return (
    <div style={{ padding: 20, maxWidth: 600, margin: 'auto' }}>
      <h1>📤 Programar Mensaje por WhatsApp</h1>

      <label>Mensaje:</label>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Escribe el mensaje"
        rows={4}
        style={{ width: '100%', marginTop: 8, padding: 8 }}
      />

      <label style={{ marginTop: 16, display: 'block' }}>Fecha y hora:</label>
      <DatePicker
        selected={date}
        onChange={(d) => setDate(d)}
        showTimeSelect
        dateFormat="Pp"
        style={{ width: '100%' }}
      />

      <label style={{ marginTop: 16, display: 'block' }}>Grupo:</label>
      <select
        value={groupId}
        onChange={(e) => setGroupId(e.target.value)}
        style={{ width: '100%', padding: 8 }}
      >
        <option value="">Selecciona un grupo</option>
        {groups.map((g) => (
          <option key={g.id} value={g.id}>
            {g.name}
          </option>
        ))}
      </select>

      <button
        onClick={handleSchedule}
        style={{
          marginTop: 16,
          padding: '10px 20px',
          backgroundColor: '#007bff',
          color: 'white',
          border: 'none',
          cursor: 'pointer',
        }}
      >
        Programar
      </button>

      <h2 style={{ marginTop: 40 }}>📅 Mensajes Programados</h2>
      {scheduled.length === 0 ? (
        <p>No hay mensajes programados aún.</p>
      ) : (
        <ul>
          {scheduled.map((m) => (
            <li key={m.id} style={{ marginBottom: 8 }}>
              <strong>{m.content}</strong> → {m.group} <br />
              <small>
                {new Date(m.scheduled_time).toLocaleString()} {m.sent ? '✅ Enviado' : '⏳ Pendiente'}
              </small>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
