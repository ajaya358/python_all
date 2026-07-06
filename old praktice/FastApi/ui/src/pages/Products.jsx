import { useState, useEffect } from 'react'
import api from '../api/axios'

const empty = { name: '', price: '', description: '' }

export default function Products() {
  const [products, setProducts] = useState([])
  const [form, setForm] = useState(empty)
  const [editId, setEditId] = useState(null)
  const [error, setError] = useState('')

  const load = async () => {
    const res = await api.get('/products/')
    setProducts(res.data)
  }

  useEffect(() => { load() }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    try {
      const payload = { ...form, price: parseFloat(form.price) }
      if (editId) {
        await api.put(`/products/${editId}`, payload)
        setEditId(null)
      } else {
        await api.post('/products/', payload)
      }
      setForm(empty)
      load()
    } catch (err) {
      setError(err.response?.data?.detail || 'Error')
    }
  }

  const handleEdit = (p) => {
    setEditId(p.id)
    setForm({ name: p.name, price: p.price, description: p.description || '' })
  }

  const handleDelete = async (id) => {
    await api.delete(`/products/${id}`)
    load()
  }

  return (
    <div>
      <h2>Products</h2>
      <form onSubmit={handleSubmit} className="row-form">
        <input placeholder="Name" value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} required />
        <input placeholder="Price" type="number" step="0.01" value={form.price} onChange={e => setForm({ ...form, price: e.target.value })} required />
        <input placeholder="Description" value={form.description} onChange={e => setForm({ ...form, description: e.target.value })} />
        <button type="submit">{editId ? 'Update' : 'Add'}</button>
        {editId && <button type="button" onClick={() => { setEditId(null); setForm(empty) }}>Cancel</button>}
      </form>
      {error && <p className="error">{error}</p>}
      <table>
        <thead>
          <tr><th>ID</th><th>Name</th><th>Price</th><th>Description</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {products.map(p => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.name}</td>
              <td>₹{p.price}</td>
              <td>{p.description}</td>
              <td>
                <button onClick={() => handleEdit(p)}>Edit</button>
                <button onClick={() => handleDelete(p.id)} className="danger">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
