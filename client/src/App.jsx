import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Login from './components/login'
import SignUp from './components/signup'
import Home from './pages/Home'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path = '/' element = {<Home/>}></Route>
        <Route path = '/login' element = {<Login/>}></Route>
        <Route path = '/sign-up' element = {<SignUp/>}></Route>
      </Routes>
    </div>
  )
}

export default App