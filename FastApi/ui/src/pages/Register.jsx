import { useState } from 'react'
import api from '../api/axios'
import { useNavigate, Link } from 'react-router-dom'

export default function Register() {
  const navigate = useNavigate()
  const [form, setForm] = useState({ name: '', email: '', password: '' })
  const [msg, setMsg] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    try {
      await api.post('/users/', form)
      setMsg('Registered! Please login.')
      setTimeout(() => navigate('/login'), 1500)
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed')
    }
  }

  return (
    <div className="card">
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input placeholder="Name" value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} required />
        <input placeholder="Email" value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} required />
        <input type="password" placeholder="Password" value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} required />
        <button type="submit">Register</button>
      </form>
      {msg && <p className="success">{msg}</p>}
      {error && <p className="error">{error}</p>}
      <p>Have account? <Link to="/login">Login</Link></p>
    </div>
  )
}
