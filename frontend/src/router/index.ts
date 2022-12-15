import {createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/about',
    component: Home
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router