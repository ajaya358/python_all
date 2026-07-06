import { useState, useEffect } from 'react'
import api from '../api/axios'

const empty = { name: '', email: '', password: '' }

export default function Users() {
  const [users, setUsers] = useState([])
  const [form, setForm] = useState(empty)
  const [editId, setEditId] = useState(null)
  const [error, setError] = useState('')

  const load = async () => {
    try {
      const res = await api.get('/users/')
      setUsers(res.data)
    } catch (err) {
      setError('Login required to view users')
    }
  }

  useEffect(() => { load() }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    try {
      if (editId) {
        await api.put(`/users/${editId}`, form)
        setEditId(null)
      } else {
        await api.post('/users/', form)
      }
      setForm(empty)
      load()
    } catch (err) {
      setError(err.response?.data?.detail || 'Error')
    }
  }

  const handleEdit = (u) => {
    setEditId(u.id)
    setForm({ name: u.name, email: u.email, password: '' })
  }

  const handleDelete = async (id) => {
    await api.delete(`/users/${id}`)
    load()
  }

  return (
    <div>
      <h2>Users</h2>
      <form onSubmit={handleSubmit} className="row-form">
        <input placeholder="Name" value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} required />
        <input placeholder="Email" value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} required />
        <input type="password" placeholder="Password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} required={!editId} />
        <button type="submit">{editId ? 'Update' : 'Add'}</button>
        {editId && <button type="button" onClick={() => { setEditId(null); setForm(empty) }}>Cancel</button>}
      </form>
      {error && <p className="error">{error}</p>}
      <table>
        <thead>
          <tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.id}>
              <td>{u.id}</td>
              <td>{u.name}</td>
              <td>{u.email}</td>
              <td>
                <button onClick={() => handleEdit(u)}>Edit</button>
                <button onClick={() => handleDelete(u.id)} className="danger">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
