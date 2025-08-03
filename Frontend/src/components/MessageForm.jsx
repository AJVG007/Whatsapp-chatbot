import React, { useEffect, useState } from "react";
import axios from "axios";

const MessageForm = () => {
  const [content, setContent] = useState("");
  const [scheduledTime, setScheduledTime] = useState("");
  const [groupId, setGroupId] = useState("");
  const [groups, setGroups] = useState([]);
  const [status, setStatus] = useState("");

  useEffect(() => {
    axios.get("/api/groups/")
      .then(res => setGroups(res.data))
      .catch(err => console.error("Error loading groups", err));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/api/messages/", {
        content,
        scheduled_time: scheduledTime,
        group_id: parseInt(groupId)
      });
      setStatus("Mensaje programado correctamente.");
      setContent("");
      setScheduledTime("");
      setGroupId("");
    } catch (err) {
      console.error("Error al programar mensaje:", err);
      setStatus("Error al programar mensaje.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 space-y-4 max-w-md mx-auto">
      <h2 className="text-xl font-bold">Programar mensaje</h2>

      <textarea
        className="w-full border rounded p-2"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Escribe el mensaje aquí..."
        required
      />

      <input
        type="datetime-local"
        className="w-full border rounded p-2"
        value={scheduledTime}
        onChange={(e) => setScheduledTime(e.target.value)}
        required
      />

      <select
        className="w-full border rounded p-2"
        value={groupId}
        onChange={(e) => setGroupId(e.target.value)}
        required
      >
        <option value="">Selecciona un grupo</option>
        {groups.map((group) => (
          <option key={group.id} value={group.id}>
            {group.name}
          </option>
        ))}
      </select>

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Programar
      </button>

      {status && <p className="text-sm text-gray-600">{status}</p>}
    </form>
  );
};

export default MessageForm;
