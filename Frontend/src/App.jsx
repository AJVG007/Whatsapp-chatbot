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
    const res = await axios.get('/api/groups/');
    setGroups(res.data);
  };

  const fetchMessages = async () => {
    const res = await axios.get('/api/messages/');
    setScheduled(res.data);
  };

  const handleSchedule = async () => {
    await axios.post('/api/messages/', {
      content: message,
      scheduled_time: date.toISOString(),
      group_id: parseInt(groupId),
    });
    setMessage('');
    fetchMessages();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Programar Mensaje</h1>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Escribe el mensaje"
      />
      <br />
      <DatePicker selected={date} onChange={(d) => setDate(d)} showTimeSelect />
      <br />
      <select value={groupId} onChange={(e) => setGroupId(e.target.value)}>
        <option value="">Selecciona un grupo</option>
        {groups.map((g) => (
          <option key={g.id} value={g.id}>
            {g.name}
          </option>
        ))}
      </select>
      <br />
      <button onClick={handleSchedule}>Programar</button>

      <h2>Mensajes Programados</h2>
      <ul>
        {scheduled.map((m) => (
          <li key={m.id}>
            <strong>{m.content}</strong> → {m.group} a las {new Date(m.scheduled_time).toLocaleString()}
            {m.sent ? ' ✅' : ' ⏳'}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
