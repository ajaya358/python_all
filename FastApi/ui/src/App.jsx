import { BrowserRouter, Routes, Route, Link, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import Login from './pages/Login'
import Register from './pages/Register'
import Products from './pages/Products'
import Users from './pages/Users'

function Navbar() {
  const { token, logout } = useAuth()
  return (
    <nav>
      <span className="brand">FastAPI UI</span>
      <div>
        <Link to="/products">Products</Link>
        {token && <Link to="/users">Users</Link>}
        {token ? (
          <button onClick={logout}>Logout</button>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </div>
    </nav>
  )
}

function PrivateRoute({ children }) {
  const { token } = useAuth()
  return token ? children : <Navigate to="/login" />
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Navigate to="/products" />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/products" element={<Products />} />
            <Route path="/users" element={<PrivateRoute><Users /></PrivateRoute>} />
          </Routes>
        </main>
      </BrowserRouter>
    </AuthProvider>
  )
}
