import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from "axios"
import { store, key} from "./store/store"
import '@stripe/stripe-js'

import './assets/main.css'

axios.defaults.baseURL = "http://127.0.0.1:5000"
axios.defaults.withCredentials = true

createApp(App)
.use(store, key)
.use(router)
.mount('#app')
